import py3Dmol
import random

v = py3Dmol.view(width=400, height=400)

for _ in range(100):
    v.addSphere({
        "center": {
            "x": random.uniform(-2, 2),
            "y": random.uniform(-2, 2),
            "z": random.uniform(-2, 2)
        },
        "radius": 0.3,
        "color": "gold"
    })

v.setBackgroundColor("black")
v.zoomTo()
v.show()
