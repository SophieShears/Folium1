import folium
import pandas as pd
import os

states = os.path.join('data', 'us-states.json')
recurse_data = os.path.join('data', 'recurse.csv')
state_data = pd.read_csv(recurse_data)

m = folium.Map(location=[48, -102], zoom_start=3)

choropleth = folium.Choropleth(
 geo_data=states,
 name='choropleth',
 data=state_data,
 columns=['State','Recursers'],
 nan_fill_color='grey',
 nan_fill_opacity=0.4,
 key_on='feature.id',
 fill_color='YlGn',
 legend_name='# of Recursers',
 highlight = True,
 fill_opacity=0.5
).add_to(m)

folium.LayerControl().add_to(m)

# Display Region Label
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'], labels=True)
)

# TODO: How to get the number of Recursers as the tool tip?


m.save('index.html')
