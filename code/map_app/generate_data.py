from app.models import WayPoints
from app import db

def send_to_db():

    list_of_coordinates = [
        (41.150402, 34.671801),
        (40.652129, 31.503621),
        (41.059300, 29.705200),
        (41.685870, 27.544193),
        (41.882479, 25.839118),
        (41.092428, 23.892344),
        (40.091346, 21.550062),
        (40.627122, 19.460466),
        (40.860184, 16.248333)
    ]
    for coor in list_of_coordinates:
        way_point = WayPoints(coor[0],coor[1])
        db.session.add(way_point)
        db.session.commit()

    return "successfully added way points"


send_to_db()
