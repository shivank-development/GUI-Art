import matplotlib.pyplot as plt

def draw_google_logo():
    fig, ax = plt.subplots(figsize=(9, 2))
    ax.set_facecolor("white")
    ax.axis("off")

    # Google logo colors
    colors = {
        "G": "blue",
        "o1": "red",
        "o2": "yellow",
        "g": "blue",
        "l": "green",
        "e": "red",
        "!": "blue"
    }

    # Draw letters
    ax.text(0.05, 0.5, "G", fontsize=120, color=colors["G"], weight="bold", va="center")
    ax.text(0.25, 0.5, "o", fontsize=120, color=colors["o1"], weight="bold", va="center")
    ax.text(0.42, 0.5, "o", fontsize=120, color=colors["o2"], weight="bold", va="center")
    ax.text(0.59, 0.5, "g", fontsize=120, color=colors["g"], weight="bold", va="center")
    ax.text(0.75, 0.5, "l", fontsize=120, color=colors["l"], weight="bold", va="center")
    ax.text(0.82, 0.5, "e", fontsize=120, color=colors["e"], weight="bold", va="center")
    ax.text(0.95, 0.5, "!", fontsize=120, color=colors["!"], weight="bold", va="center")

    plt.show()

draw_google_logo()
