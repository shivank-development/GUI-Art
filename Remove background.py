from withoutbg import WithoutBG

# Load open-source background remover
clcoding = WithoutBG.opensource()

# Remove background
result = clcoding.remove_background("bird.jpg")

# Save output
result.save("output.png")

print("Background removed successfully! Saved as output.png")
