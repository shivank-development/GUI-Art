from skyfield.api import load
import plotly.graph_objects as go

# Time scale
ts = load.timescale()

# Load ISS TLE data
satellites = load.tle_file(
    "https://celestrak.org/NORAD/elements/stations.txt"
)
sat = satellites[0]   # ISS

# Time range (90 minutes, every 5 minutes)
times = ts.utc(2026, 1, 1, range(0, 90, 5))

xs, ys, zs = [], [], []

# Compute positions
for t in times:
    pos = sat.at(t).position.km
    xs.append(pos[0])
    ys.append(pos[1])
    zs.append(pos[2])

# 3D plot
fig = go.Figure(
    go.Scatter3d(
        x=xs,
        y=ys,
        z=zs,
        mode="lines",
        line=dict(width=4)
    )
)

fig.update_layout(
    title="ISS Orbit Around Earth",
    scene=dict(
        xaxis_title="X (km)",
        yaxis_title="Y (km)",
        zaxis_title="Z (km)"
    )
)

fig.show()
