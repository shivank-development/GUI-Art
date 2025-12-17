import overpy

api = overpy.Overpass()

city = input("Enter the city name: ")

q = f"""
area[name="{city}"]->.a;
(
  way["waterway"="river"](area.a);
);
out body;
"""

result = api.query(q)

for way in result.ways:
    print(way.tags.get("name", "Unnamed River"))
