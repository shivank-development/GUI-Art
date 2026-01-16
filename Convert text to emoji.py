import emoji

def text_to_emoji(text):
    return emoji.emojize(text, language="alias")

text = "I love Python :snake:"
print(text_to_emoji(text))
