import numpy as np
import pandas as pd
import sqlalchemy

from flask import Flask, jsonify
from sqlalchemy import create_engine, func

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

from datetime import timedelta

engine = create_engine("sqlite:///titanic.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)



Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)
@app.route("/")
def Home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def percipitation():
    session = Session(engine)
    recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date= dt.datetime.strptime(recent[0],'%Y-%m-%d')
    yr_of_Rec_date = dt.date(recent_date.year - 1, recent_date.month, recent_date.day)
    retrive= (Measurement.date, Measurement.prcp)
    retrive_date_pre= session.query(*retrive).filter(Measurement.date >= yr_of_Rec_date).all()
    return jsonify(retrive_date_pre)
    session.close()

@app.route("/api/v1.0/stations")
def stations():
session  = Session(engine)
  stations_results = session.query(Station.station, Station.name).all()
  return jsonify(stations_results)


@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/temp/<start>")

@app.route("/api/v1.0/temp/<start>/<end>")
