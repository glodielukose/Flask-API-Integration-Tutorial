from flask import Flask, render_template, request
import json
import urllib


def get_weather(query):
  api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e20f1fb921b19bded4f8ddd7134a9486"
  
  query = urllib.parse.quote(query)
  url = api_url.format(query)
  data = urllib.request.urlopen(url).read()
  parsed = json.loads(data)
  weather = None
  
  if parsed['weather']:
    weather = {
      'description': parsed['weather'][0]['description'],
      'temperature': parsed['main']['temp'],
      'city': parsed['name'],
      'country': parsed['sys']['country']
    }
  
  return weather

app = Flask(__name__)

@app.route("/")
def index():
  city = request.args.get('city')
  if not city:
    city = "London,Uk"

  return render_template(
    "home.html",
    weather=get_weather(city)
    )
