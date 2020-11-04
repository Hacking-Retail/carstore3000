from flask import request, jsonify, abort
from flask_restful import Resource, reqparse

from carstore3000.extensions import auth
from carstore3000.models.users import UserModel, UserSchema


get_parser = reqparse.RequestParser()
get_parser.add_argument("username", type=str)
get_parser.add_argument("password", type=str)

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", type=str, required=True)
post_parser.add_argument("password", type=str, required=True)

# common with post parser
put_parser = reqparse.RequestParser()
put_parser.add_argument("new_password", type=str, required=True)


class UsersRoutes(Resource):

    def post(self):
        request.get_json(force=True)
        args = post_parser.parse_args()
        username = args["username"]
        password = args["password"]
        db_user = UserModel.query.filter_by(username=username).first()

        if db_user is not None:
            abort(400, "User already exists")
        password = UserModel.set_password(password)

        UserModel(username=username, password=password).save()
        return jsonify({"status": "success"})

    # TODO: Only admin should access
    @auth.login_required
    def get(self):
        # TODO: force json even for empty query
        # request.get_json(force=True)
        args = get_parser.parse_args()
        args = {k: v for k, v in args.items() if v is not None}

        schema = UserSchema()
        if args:
            users = UserModel.query.filter_by(**args).all()
        else:
            users = UserModel.query.all()

        if not users:
            res = {}
        else:
            res = [schema.dump(i) for i in users]

        return jsonify(res)

    # TODO: authentication
    def put(self):
        request.get_json(force=True)
        args = post_parser.parse_args()
        username = args["username"]
        password = args["password"]
        db_user = UserModel.query.filter_by(username=username).first()
        # TODO: verify password before update

        if db_user is None:
            abort(400, "User not found")

        db.session.update(db_user)
        db.session.commit()

        return jsonify({"status": "success"})

    # TODO: authentication
    def delete(self):
        request.get_json(force=True)
        args = post_parser.parse_args()
        username = args["username"]
        password = args["password"]
        db_user = UserModel.query.filter_by(username=username).first()

        if db_user is None:
            abort(400)

        db_user.delete()
        return jsonify({"status": "success"})
