from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from helper_functions import *

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(status='404', message='Not Found. The URI requested is invalid or the resource requested does not exists.'), 404

class CityByState(Resource):
    def get(self, state):
        if not is_state_valid(state):
            return {'status':'400', 'message': 'Bad Request. Valid state required.'}, 400

        cities = City.query.filter_by(state=state.upper()).all()
        jsonified_cities = jsonify_cities(cities)
        return {'status':'200', 'result': jsonified_cities}, 200


class NearestCity(Resource):
    def get(self, state, city):
        if not is_state_valid(state):
            return {'status':'400', 'message': 'Bad Request. Valid state required.'}, 400
        elif not is_city_valid(state, city):
            return {'status':'400', 'message': 'Bad Request. Valid city required.'}, 400
        else:
            parser.add_argument('radius', type=int, location='args')
            args = parser.parse_args()
            radius = args['radius']
            city = City.query.filter_by(state=state.upper(), name=city.capitalize()).first()
            jsonified_cities = jsonify_cities(query_nearest_cities(radius, city.longitude, city.latitude))
            return {'status':'200', 'result': jsonified_cities}, 200


class UserVisit(Resource):
    def get(self, user):
        if not does_user_exist(user):
            return {'status':'404', 'message': 'Not Found. Enter valid user id.'}, 404
        city_ids = get_all_cities_by_user(user)
        cities = get_cities_by_ids(city_ids)
        jsonified_cities = jsonify_cities(cities)
        return {'status': '200', 'result': jsonified_cities}

    def post(self, user):
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        args = parser.parse_args()
        city = City.query.filter_by(state=args['state'].upper(), name=args['city'].capitalize()).first()
        if has_user_visited_city(user, city.id):
            return {'status':'409', 'message': 'Conflict. User has visited city.'}, 409
        visit = create_new_visit(db, user, city.id)
        return {'status':'200', 'result': {'id': visit.id}}, 200

api.add_resource(CityByState, '/v1/states/<string:state>/cities', '/v1/states/<string:state>/cities/')
api.add_resource(NearestCity, '/v1/states/<string:state>/cities/<string:city>', '/v1/states/<string:state>/cities/<string:city>/')
api.add_resource(UserVisit, '/v1/users/<int:user>/visits', '/v1/users/<int:user>/visits/')

if __name__ == '__main__':
    app.run(debug=True)