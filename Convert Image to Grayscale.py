from PIL import Image

img = Image.open("LM.jpg")
gray = img. convert("L")
gray. save("LM_gray.jpg")
gray