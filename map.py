import folium
# Coordinates for Shanivar Wada, Pune
shanivar_wada_location = [18.5196, 73.8553]
location2 = [18.5187, 73.8565]
location3 = [18.5190, 73.8573]

# Create a map centered on Shanivar Wada
map_shanivar_wada = folium.Map(location=shanivar_wada_location, zoom_start=15)

# Add markers
folium.Marker(
    location=shanivar_wada_location,
    popup='Shanivar Wada',
    icon=folium.Icon(color='red', icon='info-sign',icon_size=(30, 30))
).add_to(map_shanivar_wada)


folium.Marker(
    location=location2,
    popup='Lal Mahal',
    icon=folium.Icon(color='blue', icon='info-sign', prefix='custom',icon_size=(25, 25))
).add_to(map_shanivar_wada)

folium.Marker(
    location=location3,
    popup='Kasba Ganpati',
    icon=folium.Icon(color='blue', icon='info-sign', prefix='custom',icon_size=(25, 25))
).add_to(map_shanivar_wada)

# Display the map
map_shanivar_wada
map_shanivar_wada.save('shanivar_wada_map.html')