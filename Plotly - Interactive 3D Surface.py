import plotly.graph_objects as go
import numpy as np

# Create data
x = y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis')])

# Customize layout
fig.update_layout(title="3D Surface", scene=dict(
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    zaxis_title='Z Axis'
))

# Display the figure
fig.show()
