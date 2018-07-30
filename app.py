


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify
import pandas as pd


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///surfsup.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
# Passenger = Base.classes.passenger

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# http://localhost:5000/
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/startdate/enddate <br/>"
        f"/api/v1.0/startdate"
    )

# http://localhost:5000/api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    # Query all passengers
    stations = pd.read_sql("SELECT station FROM stations", engine)  
    dfList = stations['station'].tolist()
 

   # Convert list of tuples into normal list
    return jsonify(dfList)


# http://localhost:5000/api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of tempatures from prior year"""
    # Query all passengers
    measure = pd.read_sql("SELECT tobs FROM measurement WHERE SUBSTR(date,1,4)='2017'", engine)
    dfList = measure['tobs'].tolist()
 
    # Convert list of tuples into normal list
    return jsonify(dfList)

# http://localhost:5000/api/v1.0/<start>
@app.route("/api/v1.0/<start>")
def temp(start):
    """Return a minimum temperature, the average temperature, and the max temperature for a given start date"""
    # Query all passengers
    qry = ("""
        SELECT 
              date,
              tobs
         FROM measurement 
         ;
       """
      )
    
    df = pd.read_sql(qry, engine)
    df1=df[(df['date'] >= start) ]
    avg=df1.mean()
    minimum=df1.min()
    maximum=df1.max()
    
    # Convert results into dictionary
    
    result_dict = {
        "average": avg[0],
        "min":minimum[1],
        "max":maximum[1]
    }

    # return jsonify(dfList)
    return jsonify(result_dict)


# http://localhost:5000/api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>/<end>")
def temp2(start,end):
    """Return a minimum temperature, the average temperature, and the max temperature for a given start date"""
    # Query all passengers
    qry = ("""
        SELECT 
              date,
              tobs
         FROM measurement 
         ;
       """
      )
    
    df = pd.read_sql(qry, engine)
    df1=df[(df['date'] >= start)& (df['date'] < end) ]
    avg=df1.mean()
    minimum=df1.min()
    maximum=df1.max()
    
    # Convert results into dictionary
    
    result_dict = {
        "average": avg[0],
        "min":minimum[1],
        "max":maximum[1]
    }

    # return jsonify(dfList)
    return jsonify(result_dict)



if __name__ == '__main__':
    app.run(debug=True)


