from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def weather_info(city):
    city = city.replace(" ", "+")
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    res = requests.get(f"https://www.google.com/search?q={city}+Weather", headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    location = soup.select('#wob_loC')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    try:
        Print(location.encode('unicode_escape').decode())
        print(time.encode('unicode_escape').decode())
        print(info.encode('unicode_escape').decode())
        print(weather.encode('unicode_escape').decode() + "°C")
    except UnicodeEncodeError:
        print("Unable to print the weather information due to encoding issues.")

weather_info("US Weather")
