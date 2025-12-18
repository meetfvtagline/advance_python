import requests

def get_weather(city):
    api_key='29a4e31ee58450ea687296ea985d3c23'
    base_url='http://api.openweathermap.org/data/2.5/weather?'
    complete_url=base_url+'&q='+city+'&APPID='+api_key
    response=requests.get(complete_url)
    print("Status Code:",response.status_code)
    print("Headers:",response.headers['Content-Type'])
    print("Url",response.url)
    with open(f'weather_response_{city}','wb') as f:
        f.write(response.content)

    list_of_data=['weather','main','wind','sys','name']
    for key,value in response.json().items():
        if key in list_of_data:
            print(f"{key}:{value}")
    return response.json()

if __name__=='__main__':
    city=input("Enter city name: ")
    weather_data=get_weather(city)
    print(weather_data)
