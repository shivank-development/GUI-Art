import py3Dmol
import random

v = py3Dmol.view(width=400, height=400)

# Center sphere
v.addSphere({
    "center": {"x": 0, "y": 0, "z": 0},
    "radius": 0.6,
    "color": "gold"
})

# Random surrounding particles
for _ in range(80):
    v.addSphere({
        "center": {k: random.uniform(-4, 4) for k in "xyz"},
        "radius": 0.2,
        "color": "cyan",
        "opacity": 0.5
    })

v.setBackgroundColor("black")
v.zoomTo()
v.show()
