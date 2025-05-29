from flask import jsonify, request
from app.eventscrap import Scrap

scrap_controller = Scrap()

class ScrapView:

    def do_scrap():
        try:
            scrap_controller.hacerscrap()
            return jsonify({'mensaje': 'El scrap ejecutó correctamente.'}), 200
        except Exception as e:
            # Manejar la excepción y devolver un mensaje de error adecuado
            return jsonify({'error': str(e)}), 500