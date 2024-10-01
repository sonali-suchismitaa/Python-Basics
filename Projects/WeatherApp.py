import requests

city = input("Enter your city : ")

url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

r = requests.get(url)
print(r.text)
print(type(r.text))