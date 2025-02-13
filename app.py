import streamlit as st
import requests

# Your API key
api_key = '608b7680c5f1fd94cc00147dab8789e0'

# Function to get weather data
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

# Streamlit app
st.title('Weather Information System')
city = st.text_input('Enter city name')

if st.button('Get Weather'):
    weather = get_weather(city)
    if weather:
        st.subheader(f"{weather['city']}, {weather['country']}")
        st.write(f"Temperature: {weather['temperature']}°C")
        st.write(f"Weather: {weather['description']}")
        st.write(f"Humidity: {weather['humidity']}%")
        st.write(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        st.write('City not found')

# Run the app with:
# streamlit run app.py
