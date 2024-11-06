# Importación de módulos necesarios
from flask_restx import fields  # Importa los tipos de campos de flask_restx
from extensions import api  # Importa el objeto api definido en extensions.py

# Definición del modelo de datos para una tarea
task_model = api.model('Task', {
    'id': fields.Integer(readonly=True, description='ID de la tarea'),
    'title': fields.String(required=True, description='Título de la tarea'),
    'description': fields.String(description='Descripción de la tarea')
})
