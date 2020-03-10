from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C621724F-00B6-42C0-81C7-490E58F4E8FC"
        )
        # "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C621724F-00B6-42C0-81C7-490E58F4E8FC"

    try:
        content = api_request.content#.decode('UTF-8')
        api = json.loads(content)
    except Exception as e:
        api = list("Error...")

    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=C621724F-00B6-42C0-81C7-490E58F4E8FC
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})