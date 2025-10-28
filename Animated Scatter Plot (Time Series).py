import plotly.express as px
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Time": list(range(10)) * 3,
    "Value": np.random.randint(1, 20, 30),
    "Category": ["A"] * 10 + ["B"] * 10 + ["C"] * 10
})

fig = px.scatter(
    df,
    x="Time",
    y="Value",
    color="Category",
    title="Scatter Plot of Random Values Over Time"
)

fig.show()
fig.write_html("animated_scatter_plot.html")
print("Animated scatter plot created and saved as HTML.")