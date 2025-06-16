import requests
from django.conf import settings

params = {
    "unitGroup": "metric",
    "elements": "datetime,tempmax,tempmin,temp",
    "key": settings.WEATHER_API_KEY,
    "include": "days",
    "contentType": "json",
}

def create_weather_url(location: tuple[str], date_min: str, date_max: str) -> str:
    """
    Creates the url
    Args:
        location (tuple[str]): (City, State, Country)
        date_min (str): "year-month-day"
        date_max (str): "year-month-day"
    Returns:
        url (str): returns a full url in string format
    """
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    return f"{base_url}/{location}/{date_min}/{date_max}"


def get_weather(incoming_dict: dict):
    """
    Returns the weather in the current country
    """
    # Grabs from the form
    location = (incoming_dict["state"], incoming_dict["country"])
    date_min = incoming_dict["date_from"]
    date_max = incoming_dict["date_to"]

    # 3 arguments, date_min, date_max, location
    url = create_weather_url(location=location, date_min=date_min, date_max=date_max)

    # use requests.get and add the params created earlier, for base
    response = requests.get(f"{url}", params=params)

    if response.status_code == 200:
        res = response.json()
        days = res["days"]
        return days
    elif response.status_code == 404:
        return None
    else:
        return None
