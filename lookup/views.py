from django.shortcuts import render

zipcode = '89129'
MY_API_KEY = 'C621724F-00B6-42C0-81C7-490E58F4E8FC'
URL_TEMPLATE = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={}&distance=5&API_KEY={}"


def home(request):
    import json
    import requests

    global zipcode

    def get_description(api):
        if api[0]['AQI'] < 51:
            descr = '(0 - 50) : Air quality is considered satisfactory, and air pollution poses little or no risk.'
            clr = 'good'
        elif api[0]['AQI'] < 101:
            descr = '(51 - 100) : Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            clr = 'moderate'
        elif api[0]['AQI'] < 151:
            descr = '(101-150) : Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            clr = 'usg'   
        elif api[0]['AQI'] < 201:
            descr = '(151 - 200) : Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            clr = 'unhealthy'
        elif api[0]['AQI'] < 301:
            descr = '(201 - 300) : Health alert: everyone may experience more serious health effects.'
            clr = 'veryunhealthy'
        else:
            descr = '(301 - 500) : Health warnings of emergency conditions. The entire population is more likely to be affected.'
            clr = 'hazardous'

        return clr, descr


    if request.method == "POST":
        zipcode = request.POST['zipcode']

    api_request = requests.get(URL_TEMPLATE.format(zipcode, MY_API_KEY))

    try:
        content = api_request.content
        api = json.loads(content)
        clr, descr = get_description(api)
        # return render(request, 'home.html', {'api': api, 'category_description': descr, 'category_color': clr})
    except Exception as e:
        api = "Error..."
        return render(request, 'home.html', {'api': api, })

    # clr, descr = get_description(api)
    return render(request, 'home.html', {'api': api, 'category_description': descr, 'category_color': clr})

def about(request):
    return render(request, 'about.html', {})