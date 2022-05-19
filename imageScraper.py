#modules
import random
import os
import glob
import requests
from bs4 import BeautifulSoup
from PIL import Image



#this script visits a website that contains AI generated faces
#and saves them based on a made up character's attributes created in the characterRandomise.py script





#sorts the characters by their attributes
def characterSorter(characters):

    #creates a dictionary of the characters grouped by their sex and age
    sortedCharacters = {}
    for character in characters:
        #creates dictionary keys in the format "sex/ageStr" and appends characters that match those attributes to the value list
        sortedCharacters.setdefault(f"{character['sex']}/{'young-adult' if character['age'] < 35 else ('adult' if character['age'] < 50 else 'elderly')}",[]).append(character)


    return getImages(sortedCharacters)



#retrieves the image from the website
def getImages(sortedCharacters):

    wipeImages()
    finalCharacters = []


    for query, characters in sortedCharacters.items():

        page = requests.get(f"https://generated.photos/faces/front-facing/joy/{query}")
        soup = BeautifulSoup(page.content, "html.parser")

        imageGrid = soup.find_all("div", class_="grid-photos")[0]
        images = imageGrid.find_all("img")
        

        for character in characters:
            #names image and creates address for save location
            imgPath = f"media/{len(finalCharacters)}{character['firstName']}{character['lastName']}.jpg"

            #picks, removes, and saves a random image from the images retrieved
            image_url = images.pop(random.randrange(len(images)))["src"]
            image = Image.open(requests.get(image_url, stream=True).raw)
            image.save(imgPath)
            
            #adds reference to image in the character dictionary
            character["imgAdr"] = imgPath
            finalCharacters.append(character)


    #shuffle the characters into random order to prevent noticable patterns
    random.shuffle(finalCharacters)
    return finalCharacters



def wipeImages():

    files = glob.glob("media/*.jpg")
    if len(files) != 0:
        for image in files:
            os.remove(image)




if __name__ == "__main__":
    wipeImages()