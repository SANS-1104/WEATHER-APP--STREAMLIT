import streamlit as st
import requests

def get_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

st.title('Weather Information App')
location = st.text_input('Enter a location:')

if st.button('Get Weather'):
    if location:
        api_key = 'b8114d666184008512032410bf565905'
        
        weather_data = get_weather_data(api_key, location)
        # st.write(weather_data)
        if weather_data.get('cod') != 200:
            st.error(f"Error: {weather_data.get('message')}")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Location:** {weather_data['name']},{weather_data['sys']['country']}")
                st.write(f"**Minimum Temperature:** {weather_data['main']['temp_min']}°C")
                st.write(f"**Maximum Temperature:** {weather_data['main']['temp_max']}°C")
                st.write(f"**Weather:** {weather_data['weather'][0]['description'].capitalize()}")
                st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
                st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s")
                
            with col2:
                if('clouds' in weather_data['weather'][0]['description']):
                    st.image('images/clouds.png', use_column_width=True)
                elif('thunderstorm' in weather_data['weather'][0]['description']):
                    st.image('images/thunderstorm.webp', use_column_width=True)
                elif('rain' in weather_data['weather'][0]['description']):
                    st.image('images/rain.jpg', use_column_width=True)
                elif('clear' in weather_data['weather'][0]['description']):
                    st.image('images/clear.jpg', use_column_width=True)
                elif('mist' in weather_data['weather'][0]['description']):
                    st.image('images/mist.jpg', use_column_width=True)
                elif('snow' in weather_data['weather'][0]['description']):
                    st.image('images/snow.webp', use_column_width=True)
                
    else:
        st.error("Please enter a location.")
