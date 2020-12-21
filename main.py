import os
import pytesseract
import cv2

# Creating a list of the Covid related keywords to check the later data on comparing to them
covidRelatedWords = ["covid", "covid19", "corona", "virus", "coronavirus"]

# Declaring the path of the image source
imagePath = "src/"

# Reading all the images existing in the given path:
for i in os.listdir(imagePath):

    # Checking every image existing the given path with the Teseract and extracting the text
    img = cv2.imread(f"{imagePath}/{i}")
    imgData = pytesseract.image_to_string(img).split()
    print(imgData)

    # Checking if the texts extracted from the given images are included in the keywords or not
    for j in imgData:
        for z in covidRelatedWords:
            if z in j.lower():
                print(f"Image {i} included a {z} word, which is COVID related and in image it is in the word {j}!")

# Wordlist can be extended/shortened to a better and much more accurate data based on the request.