import plotly.express as px

# Load sample dataset
df = px.data.gapminder()

# Create choropleth map
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Global Life Expectancy Over Time"
)

# Show the chart
fig.show()
