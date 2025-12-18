import pydeck as pdk
import pandas as pd
df = pd.DataFrame({
    'lat': [37.7749, 34.0522, 40.7128],
    'lon': [-122.4194, -118.2437, -74.0060],
    'value': [100, 200, 150]
})

layer = pdk.Layer("ScatterplotLayer", df, get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius='value*1000', pickable=True)
view_state = pdk.ViewState(latitude=37.77, longitude=-122.41, zoom=3)
r = pdk.Deck(layers=[layer],
    initial_view_state=view_state)
r.to_html("deck_map.html")