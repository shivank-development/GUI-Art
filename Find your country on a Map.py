import plotly.express as px

country_codes = {
    "South Africa": "ZAF",
    "India": "IND",
    "United States": "USA",
    "France": "FRA"
}

country_name = input("Enter the country name: ")

iso_code = country_codes.get(country_name.title(), None)
if not iso_code:
    print("Country not found!")
    exit()

data = {
    'ISO_Code': [iso_code],
    'Values': [100]
}

fig = px.choropleth(
    data,
    locations='ISO_Code',
    locationmode='ISO-3',
    color='Values',
    color_continuous_scale='Inferno',
    title=f'Country Map Highlighting {country_name.title()}'
)

fig.show()