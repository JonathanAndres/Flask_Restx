from flask_restx import Resource
from flask import request
from models import task_model
from extensions import api  # Import the api from extensions

# Simulación de una base de datos simple
tasks = {}

class TaskResource(Resource):
    @api.marshal_with(task_model)
    def get(self, id=None):
        """
        Obtiene una tarea específica por su ID o todas las tareas si no se proporciona ID.
        @api.marshal_with serializa la respuesta según el modelo task_model.
        """
        if id is None:
            return list(tasks.values()), 200
        if id in tasks:
            return tasks[id], 200
        api.abort(404, f"Tarea con id {id} no encontrada")

    @api.expect(task_model)
    @api.marshal_with(task_model)
    def post(self):
        """
        Crea una nueva tarea.
        @api.expect valida los datos de entrada según task_model.
        @api.marshal_with serializa la respuesta según task_model.
        """
        new_task = api.payload
        new_id = max(tasks.keys() or [0]) + 1
        new_task['id'] = new_id
        tasks[new_id] = new_task
        return new_task, 201

    @api.expect(task_model)
    @api.marshal_with(task_model)
    def put(self, id):
        """
        Actualiza una tarea existente.
        @api.expect valida los datos de entrada según task_model.
        @api.marshal_with serializa la respuesta según task_model.
        """
        if id in tasks:
            task = tasks[id]
            task.update(api.payload)
            task['id'] = id  # Aseguramos que el ID no cambie
            return task, 200
        api.abort(404, f"Tarea con id {id} no encontrada")

    def delete(self, id):
        """
        Elimina una tarea específica por su ID.
        """
        if id in tasks:
            del tasks[id]
            return '', 204
        api.abort(404, f"Tarea con id {id} no encontrada")
