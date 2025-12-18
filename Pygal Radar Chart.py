import pygal
from IPython.display import display, SVG

# Create Radar chart
radar = pygal.Radar()
radar.title = "Country Comparison"

# Labels for the axes
radar.x_labels = ["GDP", "Population", "CO2", "Internet"]

# Add data for each country
radar.add("USA", [21, 331, 5000, 88])
radar.add("China", [14, 1393, 10000, 65])
radar.add("India", [3, 1380, 2500, 45])

# Render and display chart in Jupyter Notebook
display(SVG(radar.render()))
