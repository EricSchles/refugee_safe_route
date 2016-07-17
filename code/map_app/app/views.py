from app import app
from app import db
from flask import render_template,request
from app.models import *
import json

def define_pgm_model():
    """
    This model will define a pgm that infers how likely a given waypoint is dangerous.
    We'll make use of proximity to a dangerous node, whether the area is considered war torn.
    """
    

def get_locations():
    """
    This will need to be a list of locations that end up on the map
    """
    return [(way_point.longitude,way_point.latitude) for way_point in WayPoints.query.all()]
    
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

def to_geojson(coordinates):
    dicter = {}
    dicter["type"] = "Feature"
    dicter["properties"] = {}
    dicter["geometry"] = {
        "type":"Point",
        "coordinates":[float(coordinates[0]), float(coordinates[1])]
        }
    return dicter

@app.route("/map_visual",methods=["GET","POST"])
def map_visual():
    locations = get_locations()
    locations = [to_geojson(location) for location in locations]
    return render_template("map_visual.html",locations=json.dumps(locations))

