# Import the dependencies.
import numpy as np
import pandas as pd
from datetime import date
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()
Base.prepare(autoload_with=engine)

# Reflect the database tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate App!<br/><br/>"
        f"Available Routes:<br/><br/>"
        f"Precipitation data for the last 12 months of data:<br/>"
        f"/api/v1.0/precipitation<br/><br/>"
        f"A list of stations from the database:<br/>"
        f"/api/v1.0/stations<br/><br/>"
        f"A list of the dates and temperature observations of the most-active station for the previous year of data:<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"Temperature statistics for the start date of the dataset: (2010-01-01):<br/>"
        f"/api/v1.0/2010-01-01<br/><br/>"
        f"Temperature statistics for the start date to end date of the dataset: (2010-01-01 to 2017-08-23):<br/>"
        f"/api/v1.0/2010-01-01/2017-08-23"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    """Return the precipitation data for the last 12 months"""
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year = dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year).order_by(Measurement.date).all()
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route('/api/v1.0/stations')
def stations():
    """Return a list of all stations"""
    results = session.query(Station.station).all()
    stations = [station[0] for station in results]
    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def tobs():
    """Return the date and temperature observations for the most active station in the previous year of the data"""
    active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == active_station, Measurement.date >= one_year_ago).order_by(Measurement.date).all()
    temperature_data = [{"date": date, "temperature": tobs} for date, tobs in results]
    return jsonify(temperature_data)

@app.route('/api/v1.0/<start>')
def temp_start(start):
    """Return the min, avg, and max temps for the start date (2010-01-01)"""
    if start != "2010-01-01":
        return jsonify({"error": "Only the start date 2010-01-01 is supported."}), 400
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    if results and None not in results[0]:
        temp_data = {"Start Date": start, "TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}
        return jsonify(temp_data)
    else:
        return jsonify({"error": f"No data found for the start date: {start}."}), 404

@app.route('/api/v1.0/<start>/<end>')
def temp_start_end(start, end):
    """Return the min, avg, and max temps for the start to end date (2010-01-01 to 2017-08-23)"""
    if start != "2010-01-01" or end != "2017-08-23":
        return jsonify({"error": "Only the date range 2010-01-01 to 2017-08-23 is supported."}), 400
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    if results and None not in results[0]:
        temp_data = {"Start Date": start, "End Date": end, "TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}
        return jsonify(temp_data)
    else:
        return jsonify({"error": f"No data found for the date range {start} to {end}."}), 404

if __name__ == '__main__':
    app.run(debug=True)
