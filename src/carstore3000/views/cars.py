from flask import request, jsonify, abort
from flask_restful import Resource, reqparse

from carstore3000.models.cars import CarModel, CarSchema

parser = reqparse.RequestParser()
parser.add_argument("car_id", type=int)
parser.add_argument("color_slug", type=str)
parser.add_argument("door_count", type=int)
parser.add_argument("engine_displacement", type=int)
parser.add_argument("engine_power", type=int)
parser.add_argument("fuel_type", type=str)
parser.add_argument("maker", type=str)
parser.add_argument("manufacture_year", type=int)
parser.add_argument("mileage", type=int)
parser.add_argument("model", type="str")
parser.add_argument("price_eur", type=float)
parser.add_argument("seat_count", type=int)
parser.add_argument("transmission", type=str)


class CarsRoutes(Resource):

    # TODO authentication
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        return jsonify({"status": "success"})

    def get(self):
        # TODO: force json even for empty query
        # request.get_json(force=True)
        args = parser.parse_args()
        args = {k: v for k, v in args.items() if v is not None}

        schema = CarSchema()
        if args:
            cars = CarModel.query.filter_by(**args).all()
        else:
            cars = CarModel.query.all()

        if not cars:
            res = {}
        else:
            res = [schema.dump(i) for i in cars]

        return jsonify(res)

    # TODO authentication
    def put(self):
        return jsonify({"status": "success"})

    # TODO authentication
    def delete(self):
        return jsonify({"status": "success"})
