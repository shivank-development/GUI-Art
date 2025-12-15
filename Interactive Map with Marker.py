import folium

# Create a base map centered on New Delhi
m = folium.Map(location=[28.61, 77.23], zoom_start=5)

# Add a marker for New Delhi
folium.Marker([28.61, 77.23],
              popup="New Delhi").add_to(m)

# Save the map as an HTML file
m.save("map.html")

print("✅ Map saved as 'map.html' — open it in your browser to view.")
