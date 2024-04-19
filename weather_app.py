import streamlit as st
import requests

def geocode(address):
    """Use Nominatim API to geocode an address with improved error handling."""
    params = {'q': address, 'format': 'json'}
    try:
        response = requests.get('https://nominatim.openstreetmap.org/search', params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon']), data[0]['display_name']
        else:
            return None, None, None
    except requests.RequestException as e:
        st.error(f"Failed to geocode the address due to: {str(e)}")
        return None, None, None

def get_weather(lat, lon):
    """Use Weather.gov API to get the weather by latitude and longitude with improved error handling."""
    endpoint = f'https://api.weather.gov/points/{lat},{lon}'
    try:
        point_response = requests.get(endpoint)
        point_response.raise_for_status()
        forecast_url = point_response.json()['properties']['forecast']
        weather_response = requests.get(forecast_url)
        weather_response.raise_for_status()
        forecast_data = weather_response.json()
        return forecast_data['properties']['periods'][0]['detailedForecast']
    except requests.RequestException as e:
        st.error(f"Failed to retrieve weather data due to: {str(e)}")
        return "Weather data not available."

def main():
    st.title('Weather Lookup App')
    st.write("Enter a location (e.g., 'New York', '1600 Pennsylvania Ave NW, Washington, DC') as accurately as possible.")
    address = st.text_input('Location', placeholder='Type here...')
    if address:
        lat, lon, display_name = geocode(address)
        if lat is not None:
            weather_report = get_weather(lat, lon)
            if weather_report:
                st.write(f"Weather for {display_name}:")
                st.write(weather_report)
            else:
                st.error("Failed to retrieve weather data.")
        else:
            st.error("Failed to geocode the address. Please try a different location.")

if __name__ == '__main__':
    main()
