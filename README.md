# sqlalchemy-challenge

Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

1.Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

2.Use the SQLAlchemy create_engine() function to connect to your SQLite database.

3.Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

4.Link Python to the database by creating a SQLAlchemy session.

5.Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

# Precipitation Analysis
1.Find the most recent date in the dataset.

2.Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3.Select only the "date" and "prcp" values.

4.Load the query results into a Pandas DataFrame. Explicitly set the column names.

5.Sort the DataFrame values by "date".

6.Plot the results by using the DataFrame plot method, as the following image shows:
![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/5b2fc43d-538e-4ded-a22d-0e6b302cc5af)

7.Use Pandas to print the summary statistics for the precipitation data.

# Station Analysis
1.Design a query to calculate the total number of stations in the dataset.

2.Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

3.List the stations and observation counts in descending order.

4.Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

    Filter by the station that has the greatest number of observations.

    Query the previous 12 months of TOBS data for that station.

    Plot the results as a histogram with bins=12, as the following image shows:
![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/c789f002-594c-44ce-8553-1fba1aa37e1b)

5.Close your session.

# Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1./

  Start at the homepage.

  List all the available routes.
  
![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/03164d98-9a7f-4e15-ae16-9b1b334575c7)


2./api/v1.0/precipitation

  Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

  Return the JSON representation of your dictionary.

  ![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/063ac9f5-e259-4e25-af7e-29bad60cf668)


3./api/v1.0/stations

  Return a JSON list of stations from the dataset.

  ![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/afb7360c-6af5-46d9-bfe6-6384b7cce264)

  
4./api/v1.0/tobs

  Query the dates and temperature observations of the most-active station for the previous year of data.

  Return a JSON list of temperature observations for the previous year.

![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/25d8d2bc-0ee1-4228-b249-4b3fc99a474b)


5./api/v1.0/<start> and /api/v1.0/<start>/<end>

  Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

  For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

  date used: 2010-01-01

  ![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/fc56c4f4-6408-40e4-8380-c22f1a5666a0)


  For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

  dates used: 2010-01-01/2011-01-01
  
  ![image](https://github.com/amccollough1/sqlalchemy-challenge/assets/133404805/b03b2377-c99a-4dfb-81c5-db19d041b3fa)

