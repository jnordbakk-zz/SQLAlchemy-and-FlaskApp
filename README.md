## Script 1 - data_engineering.ipynb

Uses Pandas to read,inspect and clean in the measurement and station CSV files as DataFrames.

- - -

## Script 2 - database_engineering.ipynb

Uses SQLAlchemy to model the table schemas and creates a sqlite database for the tables. 

Uses the `engine` and connection string to create a database called `hawaii.sqlite`.

## Script 3 - climate_analysis.ipynb

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Loads the query results into a Pandas DataFrame and plots the results

* Uses Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

* Design a query to retrieve the last 12 months of temperature observation data (tobs) and plot the results as a histogram 


### Temperature Analysis

* Wrote a function called `calc_temps` that accepts a start date and end date  and returns the minimum, average, and maximum temperatures for that range of dates.



## Script 4 - Climate App

Designed a Flask API based on the queries that were just developed.


### Routes


* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

  * Returns a JSON list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

 
