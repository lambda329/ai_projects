#Program to monitor and predict the weather 
import requests
import time
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import json

# Configurations
API_KEY = 'your_api_key' # Replace with your weather API key
LOCATION = 'your_location' # Set your location for the weather API
SENSOR_UPDATE_INTERVAL = 60 # seconds

# Function to get data from sensors
def get_sensor_data():
    # Replace with actual sensor reading code
    temperature = 20.0 # Mock temperature data
    humidity = 50.0 # Mock humidity data
    pressure = 1013.25 # Mock pressure data
    return temperature, humidity, pressure

# Function to get weather data from an API
def get_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving weather data")
        return None

# Function to process weather data and store it for predictions
def process_weather_data(weather_data):
    main = weather_data['main']
    return {
        'temperature': main['temp'] - 273.15, # Convert Kelvin to Celsius
        'humidity': main['humidity'],
        'pressure': main['pressure']
    }

# Collect data for prediction
def collect_data():
    data = []
    for _ in range(10): # Collect data every minute for 10 minutes
        sensor_data = get_sensor_data()
        weather_data = get_weather_data()
        if weather_data:
            weather = process_weather_data(weather_data)
            data.append([sensor_data[0], sensor_data[1], sensor_data[2], weather['temperature'], weather['humidity'], weather['pressure']])
        time.sleep(SENSOR_UPDATE_INTERVAL)
    return np.array(data)

# Prediction model setup
def train_prediction_model(data):
    X = data[:, :3] # Sensor data
    y = data[:, 3:] # Weather data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model trained with score:", model.score(X_test, y_test))
    return model

# Main loop
def main():
    print("Starting IoT Weather Monitoring Device")
    data = collect_data()
    model = train_prediction_model(data)
    while True:
        temperature, humidity, pressure = get_sensor_data()
        prediction = model.predict(np.array([[temperature, humidity, pressure]]))
        print("Predicted Weather Conditions:")
        print(f"Temperature: {prediction[0][0]:.2f}°C")
        print(f"Humidity: {prediction[0][1]:.2f}%")
        print(f"Pressure: {prediction[0][2]:.2f} hPa")
        time.sleep(SENSOR_UPDATE_INTERVAL)

if __name__ == '__main__':
    main()
