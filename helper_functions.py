from models import db, User, City, Visit
import numpy


def create_new_visit(db, user, city_id):
    visit = Visit(user, city_id)
    db.session.add(visit)
    db.session.commit()
    return visit


def get_cities_by_ids(city_ids):
    city_list = []
    for city_id in city_ids:
        city_list.append(City.query.get(city_id))

    return city_list


def get_all_cities_by_user(user):
    visits = Visit.query.filter_by(user_id=user).all()
    city_ids = []
    for visit in visits:
        city_ids.append(visit.city_id)

    return city_ids


def has_user_visited_city(user, city):
    city_visits = get_all_cities_by_user(user)
    if city in city_visits:
        return True
    return False


def does_user_exist(user):
    user = User.query.get(user)
    if user == None:
        return False

    return True


def query_nearest_cities(radius, long, lat):
    lats = calculate_min_max_latitude(radius, lat)
    longs = calculate_min_max_longitude(radius, lat, long)
    min_lat = lats[0]
    max_lat = lats[1]
    min_long = longs[0]
    max_long = longs[1]
    cities = City.query.filter(City.latitude <= max_lat, City.latitude >= min_lat, City.longitude <= max_long, City.longitude >= min_long).all()
    return cities


def calculate_min_max_latitude(radius, lat):
    radius = radius * 1.609344
    minLat = lat - numpy.rad2deg(radius/6371)
    maxLat = lat + numpy.rad2deg(radius/6371)
    return (minLat, maxLat)


def calculate_min_max_longitude(radius, lat, long):
    radius = radius * 1.609344
    minLong = long - numpy.rad2deg(radius/6371/numpy.cos(numpy.deg2rad(lat)))
    maxLong = long + numpy.rad2deg(radius/6371/numpy.cos(numpy.deg2rad(lat)))
    return (minLong, maxLong)


def is_state_valid(state):
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA","HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD","MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ","NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if state.upper() in states:
        return True
    return False


def is_city_valid(state, city):
    cities = City.query.filter_by(state=state.upper()).all()
    for current_city in cities:
        if current_city.name == city.capitalize():
            return True
    return False


def jsonify_cities(cities):
    json_cities = []
    for city in cities:
        json_cities.append({'name':city.name, 'id':str(city.id), 'state':city.state, 'status':city.status, 'latitude':str(city.latitude), 'longitude':str(city.longitude)})
    return json_cities