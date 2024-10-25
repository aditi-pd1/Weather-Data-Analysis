# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Enter city name
city = "Kolkata"

# Creating URL and making requests instance
url = "https://www.google.com/search?q=" + "weather " + city
html = requests.get(url).content

# Getting raw data using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extracting the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# Extracting the time and sky description
str_ = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str_.split('\n')
time = data[0]
sky = data[1]

# Getting all div tags with the specific class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# Debugging: Print all divs to see their content
for index, div in enumerate(listdiv):
    print(f"Div {index}: {div.text}")

# Extracting other required data
# Adjust the indices based on actual HTML structure
try:
    humidity = listdiv[0].text  # Adjust this index based on your inspection
    wind_speed = listdiv[1].text  # Adjust this index based on your inspection
except IndexError:
    humidity = "N/A"
    wind_speed = "N/A"

# Storing the data in a dictionary
weather_data = {
    "Temperature": temp,
    "Humidity": humidity,
    "Wind Speed": wind_speed,
    "Time": time,
    "Sky Description": sky,
    "Other Data": "N/A"
}

# Printing the extracted weather data
print(weather_data)

# Preparing data for plotting
labels = list(weather_data.keys())

# Remove the degree symbol and 'C' character for temperature
temperature_value = float(temp.replace('°', '').replace('C', '').strip())

# Handle humidity and wind speed, making sure to clean the strings
try:
    humidity_value = float(humidity.replace('%', '').strip())  # Assuming humidity is in percentage
except ValueError:
    humidity_value = 0  # Default value if conversion fails

# Assuming wind speed is in format '10 km/h', extract the numeric part
try:
    wind_speed_value = float(wind_speed.split()[0])  # Extract the numeric part
except (ValueError, IndexError):
    wind_speed_value = 0  # Default value if conversion fails

# Create a list of values to plot
values = [temperature_value, humidity_value, wind_speed_value]

# Plotting the data using matplotlib
plt.bar(labels[:3], values)  # Plot only the first three values (Temperature, Humidity, Wind Speed)
plt.title("Weather Data for " + city)
plt.xlabel("Weather Parameters")
plt.ylabel("Values")
plt.show()

# Storing the data in a text file with UTF-8 encoding
with open("weather_data.txt", "w", encoding="utf-8") as file:
    file.write("Weather Data for {}\n".format(city))
    file.write("=================================\n")
    for key, value in weather_data.items():
        file.write(f"{key}: {value}\n")
