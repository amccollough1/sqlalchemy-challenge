# Import the dependencies.
from flask import Flask, jsonify
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session= Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    #List of all available api routes.
    return (
        f"Aloha! Please choose one of the available routes below to explore the climate anaylsis of Honolulu, Hawaii!<br/>"
        f"***************************************************************************************<br/>"
        f"Available Routes:<br/>"
        f" "
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/<start><br/>"
        f"/api/v1.0/start-end/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipation():
    #Retrieve the last 12 months of data 
    results= session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').\
    filter(Measurement.date <= '2017-08-23').all()

    session.close()
    #Create a dictionary from the row data and append to a list of all_precipitation
    all_precipitation = []
    for date, prcp in results:
        prcp_dict= {}
        prcp_dict["date"] = date
        prcp_dict["prcp"]= prcp
        all_precipitation.append(prcp_dict)
    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
#Return a JSON list of stations from the dataset 
def stations():
    results = session.query(Station.station).all()
    session.close()
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    return jsonify(all_stations) 


@app.route("/api/v1.0/tobs")
def tobs():
    #Query the dates and temperature observations of the most-active station for the previous year of data
    results= session.query(Measurement.date, Measurement.tobs, Measurement.prcp).filter(Measurement.date >= '2016-08-23').\
    filter(Measurement.date  <= '2017-08-23').\
    filter (Measurement.station == 'USC00519281').all()
    session.close()
    all_tobs = []
    for date, tobs, prcp in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"]= tobs
        tobs_dict["prcp"] = prcp
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs) 

@app.route("/api/v1.0/start/<start>")
#Return a JSON of the min, max, and average temperatures for a specified start date 
def start_date(start):
    results= session.query(func.min(Measurement.tobs),
    func.max(Measurement.tobs),
    func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close() 

    start_date_temp=[]
    for min, max, avg in results:
        start_date_temp_dict = {}
        start_date_temp_dict["min temp"]=min
        start_date_temp_dict["max temp"]= max
        start_date_temp_dict["avg temp"]= avg
        start_date_temp.append(start_date_temp_dict)
    return jsonify(start_date_temp)    

@app.route("/api/v1.0/start-end/<start>/<end>")
#Return a JSON of the min, max, and average temperatures for a specified start and end date 
def start_end_date(start, end):
    results=session.query(func.min(Measurement.tobs),
    func.max(Measurement.tobs),
    func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    start_end_date_temp=[]
    for min, max, avg in results:
        start_end_date_temp_dict = {}
        start_end_date_temp_dict["min temp"]=min
        start_end_date_temp_dict["max temp"]= max
        start_end_date_temp_dict["avg temp"]= avg
        start_end_date_temp.append(start_end_date_temp_dict)
    return jsonify(start_end_date_temp) 

if __name__ == '__main__':
    app.run(debug=True)