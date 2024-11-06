# Importaciones necesarias
from flask import Flask  # Framework web para Python
from flask_restx import Api
from extensions import api  # Importación del objeto api definido en extensions.py
from resources import TaskResource  # Importación del recurso TaskResource
from flask_restx import Resource

# Creación de la aplicación Flask
app = Flask(__name__)  # Inicialización de la aplicación Flask

# Configuración de Swagger UI
swagger_ui_config = {
    'swagger_ui_config': {
        'displayRequestDuration': True,
        'docExpansion': 'list',
        'defaultModelsExpandDepth': 3,
        'defaultModelExpandDepth': 3,
        'deepLinking': True,
        'displayOperationId': True,
        'filter': True,
    },
    'swagger_ui_theme': 'flattop',  # Tema verde
}

# Inicialización de la API con configuraciones adicionales
api.init_app(app)
api.version = '1.0'
api.title = 'API de Gestión de Tareas'
api.description = 'Una API RESTful para gestionar tareas con operaciones CRUD'
api.contact = {'name': 'Tu Nombre', 'email': 'tu@email.com', 'url': 'https://www.tuwebsite.com'}
api.license = {'name': 'MIT', 'url': 'https://opensource.org/licenses/MIT'}
api.doc('/docs/')  # URL para la documentación Swagger

# Aplicar la configuración de Swagger UI
for key, value in swagger_ui_config.items():
    setattr(api, key, value)

# Definición del espacio de nombres (namespace)
ns = api.namespace('tareas', description='Operaciones de tareas', path='/')

# Agregación del recurso TaskResource a las rutas especificadas
ns.add_resource(TaskResource, '/tareas', '/tareas/<int:id>')

# Información adicional para Postman
@api.route('/info')
class CustomDocumentation(Resource):
    @api.doc(
        params={'server_url': {'description': 'URL base para Postman', 'default': 'http://localhost:5000'}},
        description='Información para usar en Postman'
    )
    def get(self):
        """
        Proporciona información adicional para usar la API en Postman.
        
        Para usar esta API en Postman:
        1. Configura la URL base como: http://localhost:5000
        2. Usa '/tareas' para acceder a la lista de tareas
        3. Usa '/tareas/<id>' para operaciones en tareas específicas
        """
        return {
            'message': 'Bienvenido a la API de Gestión de Tareas',
            'base_url': 'http://localhost:5000',
            'endpoints': {
                'GET /tareas': 'Obtener todas las tareas',
                'POST /tareas': 'Crear una nueva tarea',
                'GET /tareas/<id>': 'Obtener una tarea específica',
                'PUT /tareas/<id>': 'Actualizar una tarea',
                'DELETE /tareas/<id>': 'Eliminar una tarea'
            }
        }

# Bloque principal para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)  # Ejecución de la aplicación en modo debug
    # El modo debug permite recargar automáticamente cuando se hacen cambios
    # y proporciona un debugger interactivo en caso de errores

