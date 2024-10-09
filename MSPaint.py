import os
import subprocess

img = "aPicture.jpg"

path = os.path.join(img, "your_image.jpg")

while True:
    file = input("Enter the name of your .jpg image file: ")
    if os.path.exists(file) and os.path.splitext(file)[1] == ".jpg":
        path = file
        break
    else:
        print("Invalid file name or format. Please try again.")

subprocess.run(['mspaint', path])
