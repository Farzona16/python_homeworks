import requests

api_key = "api_key"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid={api_key}&units=metric"

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    
    print(f"Location: {city}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print(f"Xatolik yuz berdi: {response.status_code}")
    