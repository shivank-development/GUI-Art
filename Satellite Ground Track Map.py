from skyfield.api import load
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Load ISS TLE
sat = load.tle_file(
    "https://celestrak.org/NORAD/elements/stations.txt"
)[0]

# Time scale
ts = load.timescale()
times = ts.utc(2026, 1, 1, range(0, 90, 5))

lats, lons = [], []

# Compute subpoints
for t in times:
    geo = sat.at(t).subpoint()
    lats.append(geo.latitude.degrees)
    lons.append(geo.longitude.degrees)

# Plot map
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.plot(lons, lats, color="red", linewidth=2)

plt.title("ISS Ground Track")
plt.show()
