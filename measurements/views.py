# from django.shortcuts import render

# # Create your views here.

from django.shortcuts import render, get_object_or_404
from numpy import save

from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo
import folium
# Create your views here.
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form=MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')
    ip='103.230.154.107'
    country, city, lat, lon = get_geo(ip)
    # print('location country',country)
    # print('location city',city)
    # print('location lat,lon',lat,lon)

    location = geolocator.geocode(city)
    # print('###',location)
    # importing geopy library
    
    l_lat = 30.3408
    l_lon = 78.0440
    pointA = (l_lat, l_lon)
    

# initial folium map
    m = folium.Map(width=1000, height=800, zoom_start=8,location=pointA)
    # location marker
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        # print(destination)
        d_lat = destination.latitude
        d_lon=destination.longitude

         # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)

        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)
        #folium map modification
        m = folium.Map(width=800, height=600, zoom_start=12,location=pointB)
       
        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)
        # destination marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
                    icon=folium.Icon(color='red',icon='cloud')).add_to(m)

        instance.location=location
        instance.distance=distance
        instance.save()

    m = m._repr_html_()

    context = {
        'distance' : obj,
        'form':form,
        'map':m
       
    }

    return render(request, 'measurements/main.html', context)
