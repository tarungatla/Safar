import folium

raigad_fort_location = [18.2313, 73.4541]
rajyabhishek_mandap_location = [18.2320, 73.4560]
maha_darwaja_location = [18.2312, 73.4539]
takmak_tok_location = [18.2298, 73.4537]
hirkani_buruj_location = [18.2314, 73.4547]

map_raigad_fort = folium.Map(location=raigad_fort_location, zoom_start=15)


folium.Marker(
    location=raigad_fort_location,
    popup='Raigad Fort',
    icon=folium.Icon(color='green', icon='star', prefix='fa')
).add_to(map_raigad_fort)

folium.Marker(
    location=rajyabhishek_mandap_location,
    popup='Rajyabhishek Mandap',
    icon=folium.Icon(color='blue', icon='university', prefix='fa')
).add_to(map_raigad_fort)

folium.Marker(
    location=maha_darwaja_location,
    popup='Maha Darwaja',
    icon=folium.Icon(color='red', icon='archway', prefix='fa')
).add_to(map_raigad_fort)

folium.Marker(
    location=takmak_tok_location,
    popup='Takmak Tok',
    icon=folium.Icon(color='cadetblue', icon='flag', prefix='fa')
).add_to(map_raigad_fort)

folium.Marker(
    location=hirkani_buruj_location,
    popup='Hirkani Buruj',
    icon=folium.Icon(color='orange', icon='tower', prefix='fa')
).add_to(map_raigad_fort)

# Display the map
map_raigad_fort
map_raigad_fort.save('raigad_map.html')