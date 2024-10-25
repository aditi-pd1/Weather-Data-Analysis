# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Enter city name
city = "Kolkata"

# Creating URL and making requests instance
url = "https://www.google.com/search?q=" + "weather" + city
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

# Extracting other required data
strd = listdiv[5].text
pos = strd.find('Wind')
other_data = strd[pos:]

# Printing the extracted weather data
print("Temperature is:", temp)
print("Time:", time)
print("Sky Description:", sky)
print(other_data)
