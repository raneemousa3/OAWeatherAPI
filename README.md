# OAWeatherAPI
Weather in germany

Overview
This Python program fetches hourly temperature data for Germany (specifically for Berlin) from the Open-Meteo API. It visualizes the temperature changes over a specified number of days using Matplotlib.

Features
Retrieves current and hourly temperature data for the specified number of days.
Organizes temperature data by date.
Plots the hourly temperature for each day using a line graph.
Requirements
To run this program, you'll need:

Python 3.x
requests library for API calls
matplotlib library for plotting
You can install the required libraries using pip:

bash
Copy code
pip install requests matplotlib
Usage
Instantiate the WeatherinGermany Class: Create an instance of the WeatherinGermany class by specifying the number of days for which you want to retrieve the temperature data.

python
Copy code
weather = WeatherinGermany(7)  # Retrieves data for 7 days
Fetch Temperature Data: Call the get_temp method to retrieve and store the hourly temperature data.

python
Copy code
weather.get_temp()
Get Time Data: Call the get_time method to organize the timestamps for the temperature data.

python
Copy code
weather.get_time()
Graph the Data: Call the graph_it method to generate a line graph that displays the hourly temperatures for each day.

python
Copy code
weather.graph_it()
Code Explanation
Class Initialization: The __init__ method sets up the API URL with the specified number of days and initializes attributes to hold temperature and time data.

API Response: The get_response method retrieves the JSON response from the Open-Meteo API.

Temperature Processing: The get_temp method processes the API response to extract and organize hourly temperature data by date.

Time Processing: The get_time method organizes the timestamps corresponding to the temperature data.

Graphing: The graph_it method uses Matplotlib to plot the hourly temperature for each day, labeling axes and rotating the x-axis labels for better readability.

