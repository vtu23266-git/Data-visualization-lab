import pandas as pd
import folium

df_geo = pd.read_csv("locations.csv")
m = folium.Map(location=[df_geo['Latitude'].mean(), df_geo['Longitude'].mean()], zoom_start=5)

for _, row in df_geo.iterrows():
    folium.CircleMarker(location=[row['Latitude'],row['Longitude']],
                        radius=5, popup=row['Place']).add_to(m)

m.save("map_output.html")
print("Map saved as map_output.html")
