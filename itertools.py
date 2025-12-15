import itertools
colors = ["red", "blue", "green"]
cycle_colors = itertools.cycle(colors)
result = [next(cycle_colors) for _ in range(5)]
print(result[-1], len(result))