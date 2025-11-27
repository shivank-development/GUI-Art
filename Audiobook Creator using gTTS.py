from gtts import gTTS

# Read text file
with open("clcoding.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Convert to audio
clcoding = gTTS(text=text, lang="en")

# Save audiobook
clcoding.save("audiobook.mp3")

print("Audiobook created: audiobook.mp3")
