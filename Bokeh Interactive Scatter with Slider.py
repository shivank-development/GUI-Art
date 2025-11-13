from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Slider, CustomJS
from bokeh.layouts import column  # ✅ fixed typo: 'layouts' not ' layouts'
# Data
x = list(range(10))
y = [i ** 2 for i in x]
source = ColumnDataSource(data=dict(x=x, y=y))

# Plot
p = figure(title="Interactive Scatter with Slider",
           x_axis_label="x", y_axis_label="y")
p.circle("x", "y", size=10, source=source, color="green")

# Slider
slider = Slider(start=1, end=5, value=1, step=1, title="Multiplier")

# JS callback
callback = CustomJS(args=dict(source=source, slider=slider), code="""
    const data = source.data;
    const f = slider.value;
    const x = data['x'];
    data['y'] = x.map(v => v * v * f);  // apply multiplier
    source.change.emit();
""")

slider.js_on_change("value", callback)

# Layout and show
layout = column(slider, p)
show(layout)
