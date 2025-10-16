from flask import request, jsonify
from flask_restful import Resource
from models import db, Item

class ItemResource(Resource):
    # GET todos los ítems
    def get(self, item_id=None):
        if item_id:
            item = Item.query.get(item_id)
            if item:
                return jsonify({"id": item.id, "name": item.name, "description": item.description})
            else:
                return jsonify({"message": "Item no encontrado"}), 404
        else:
            items = Item.query.all()
            return jsonify([{"id": i.id, "name": i.name, "description": i.description} for i in items])

    # POST nuevo ítem
    def post(self):
        data = request.get_json()
        new_item = Item(name=data['name'], description=data.get('description'))
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item creado", "id": new_item.id})

    # PUT actualizar ítem
    def put(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return jsonify({"message": "Item no encontrado"}), 404
        data = request.get_json()
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        db.session.commit()
        return jsonify({"message": "Item actualizado"})

    # DELETE eliminar ítem
    def delete(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return jsonify({"message": "Item no encontrado"}), 404
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item eliminado"})
