import requests
from django.conf import settings 

#For use outside of website?
if not settings.configured:
    settings.configure(WEATHER_API_KEY = "ZYYAWLARZCNN2MC67V4K5HA3L")


def create_weather_url(location: tuple[str], date_min:str, date_max:str) -> str:
    '''
    Creates the url
    Args:
        location (tuple[str]): (City, State, Country)
        date_min (str): "year-month-day"
        date_max (str): "year-month-day"
    Returns:
        url (str): returns a full url in string format
    '''
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    return f"{base_url}/{location}/{date_min}/{date_max}"


def get_weather():
    """
    Returns the weather in the current country
    """
    params = {
    "unitGroup": "metric", 
    "elements": "datetime,tempmax,tempmin,temp",
    "key": settings.WEATHER_API_KEY,
    "include":'days',
    "contentType":"json",
    }
    #Grab this from POST request of front-end
    date_min = "2025-06-14"
    date_max = "2025-06-16"
    date_range = date_min + date_max

    #And this + city
    state = "Sydney"
    country = "Australia"
    location = state,country

    url = create_weather_url(location=location, date_min=date_min, date_max=date_max)
    response = requests.get(f'{url}', params = params)

    if response.status_code == 200:
        res = response.json()
        for i in res.items():
            if i[0] == "days":
                print("days:")
                for j in i[1]:
                    print(j)
            else:
                print(i)
    else:
        print(response.status_code)
        print(response.url)

if __name__ == "__main__":
    get_weather()