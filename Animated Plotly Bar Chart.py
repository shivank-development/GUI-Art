import plotly.express as px
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019] * 3,
    "Country": ["USA"] * 5 + ["China"] * 5 + ["India"] * 5,
    "GDP": [18, 18.5, 19, 19.5, 20, 11, 12, 13, 14, 15, 2, 2.5, 3, 3.5, 4]
})

# Create animated bar chart
fig = px.bar(df, 
             x="Country", 
             y="GDP", 
             animation_frame="Year", 
             color="Country", 
             title="GDP Growth (2015–2019)")

# Show the figure
fig.show()
