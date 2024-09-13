from main import app
from httpxfetch import fetch
from flask import render_template, request


@app.route("/", methods=['GET', 'POST'])
def homepage():
  
  if request.method== 'POST':
    search = request.form['name_city']
    print("bbbb")
  # else:
  #   print('aaaaaaaaaa')
  #   print(request)
    
    
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={search}&limit=&appid=2f46b3a61e35d2b19e849c0c610d9f17&units=metric&lang=pt_br'
    print(url)
    options = {
    'method': 'get', #obter valores existentes
    'headers': {'Content-Type': 'application/json'},
}

    response = fetch(url,options).json()
    name = response ['name']
    temp = response["main"] ['temp']
    country = response ["sys"]["country"]
    weather = response['weather'][0]["description"]
    tem_min= response ["main"]["temp_min"]
    tem_max= response ["main"]["temp_max"]
    humidity= response["main"]["humidity"]
    wind = response["wind"] ['speed']
    
    
    # city_lat = response[0]['lat']
    # city_lon = response[0]['lon']  
    print(response)
  
    return render_template('homepage.html',nome=name, temperatura=temp,pais=country,clima=weather,temp_min=tem_min,temp_max=tem_max,humidade=humidity,vento=wind)
  return render_template('homepage.html')


