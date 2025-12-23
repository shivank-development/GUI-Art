from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = "Data Science AI Python Visualization Art Creativity ML " * 20

# Generate the WordCloud
wc = WordCloud(
    width=800,
    height=400,
    background_color="black",
    colormap="plasma",
    contour_color='cyan',
    contour_width=2
).generate(text)

# Display the WordCloud
plt.figure(figsize=(8, 4))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title("Artistic Word Cloud", fontsize=16, color='cyan')
plt.show()
# Save the WordCloud to a file
wc.to_file("artistic_wordcloud.png")