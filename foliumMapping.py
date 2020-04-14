import folium
import pandas
import io, codecs, json

db = pandas.read_csv("usa.txt")

lan = list(db["LAT"])
lon = list(db["LON"])
elev = list(db["ELEV"])


def color_marker(elevation):
    if (elevation < 1000):
        return "green"
    elif (elevation >= 1000 and elevation < 2500):
        return "yellow"
    elif (elevation >= 2500 and elevation < 500):
        return "red"
    else:
        return "black"


map = folium.Map(location=[38.58, -90.09], zoom_start=6)

fgv = folium.FeatureGroup(name="USA.txt")

for la, lo, el in zip(lan, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[la, lo], popup=str(el) + " m", fill=True, fill_color=color_marker(el),
                                      color='grey', radius=6, fill_opacity=0.7))

fgw = folium.FeatureGroup(name="world.json")
fgw.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig')))

# fgw.add_child(folium.GeoJson("world.json", style_function=lambda x: {"fillColour": "yellow"}))

map.add_child(fgv)
map.add_child(fgw)
map.add_child(folium.LayerControl())

map.save("Map1.html")
