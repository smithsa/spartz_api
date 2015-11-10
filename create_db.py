import csv
from models import db, User, City

db.create_all()
with open('data/cities.csv', 'rb') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    for row in filereader:
        city = City(unicode(row[1], 'utf-8'), unicode(row[2], 'utf-8'), 1, row[4], row[5])
        city.id = row[0]
        db.session.add(city)

with open('data/users.csv', 'rb') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    for row in filereader:
        user = User(unicode(row[1], 'utf-8'), unicode(row[2], 'utf-8'))
        user.id = row[0]
        db.session.add(user)

db.session.commit()


