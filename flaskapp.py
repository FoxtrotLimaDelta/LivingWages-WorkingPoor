# BEGINNING MY APP.PY STARTER CODE!
 # Flask Routes

@app.route("/")
def welcome():
    
    """List all available API routes."""
    
    return (
        f"Welcome to your Living Wages Dashboard!:<br/>"
        f"/api/v1.0/about<br/>"
        f"/api/v1.0/visualization1<br/>"
        f"/api/v1.0/visualization2<br/>"
        f"/api/v1.0/pagename3<br/>"
        f"/api/v1.0/pagename4<br/>"
        f"/api/v1.0/pagename5<br/>"
        f"/api/v1.0/data<br/>"
        f"/api/v1.0/contact"
    )
    
      
@app.route("/api/v1.0/about")

def about():
   name = "Flynn LLC"
   location = "Arizona"
   
   return f"We are {name} and we are located in sunny {location}."

# /api/v1.0/precf"/api/v1.0/precipitation<br/>"precipitation
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/visualization1")
def visualization1():
    # Create our session (link) from Python to the DB
    #session = Session(engine)

    """Return a list of all visualization1"""
    # Query all measurements
    #results = session.query(measurement.date, measurement.prcp).all()

    # Convert list of tuples into normal list
    #all_precipitation = list(np.ravel(results))

    return jsonify(all_visualization1)

# /api/v1.0/visualization2
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/visualization2")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all visualization2"""
    # Query all stations
    #results = session.query(station.station).all()

    # Convert list of tuples into normal list
   # all_stations = list(np.ravel(results))

    return jsonify(all_visualization2)

# Query for the date and precipitation (max, mean, min) 
# for all dates in the year
# Sort the result by date


@app.route("/api/v1.0/visualization3")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all visualization3"""
    # Query all observations
    #results = session.query(measurement.tobs).filter(measurement.station =="USC00519281").all()

    # Convert list of tuples into normal list
    #all_tobs = list(np.ravel(results))

    return jsonify(all_visualization3)

# /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max
# temperature for a given start or start-end range.
@app.route("/api/v1.0/visualization4")
#def tobs_start(start=None):
    
   #sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
   # results = session.query(*sel).filter(measurement.date>=start).all()
   # all_tobs = list(np.ravel(results))
    return jsonify(all_visualization4)
    
@app.route("/api/v1.0/visualization5")
def visualization4(start=None, end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all visualization5"""
    # Query all observations
   # sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
   # results = session.query(*sel).filter(measurement.date>=start).filter(measurement.date<=end).all()

    #session.close()

    # Convert list of tuples into normal list
   # all_tobs = list(np.ravel(results))

    return jsonify(all_visualization5)

@app.route("/api/v1.0/comparison")


@app.route("/api/v1.0/data")


@app.route("/api/v1.0/contact")
def contact():
   email = "Flynnworking@gmail.com"
     
   return f"Questions, Comments, Complaints? Send an email to {email}."

if __name__ == "__main__":
    
 app.run(debug=True)
 
 # END MY APP.PY STARTER CODE!
