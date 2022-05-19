#modules
import json
import random
#files
import webScraper
import imageScraper





def main():
    characters = characterCreator()
    finalCharacters = imageScraper.characterSorter(characters)
    jsonWriter(finalCharacters)





def jsonWriter(characters):

    with open("characterData.json", "w") as writeFile:
        json.dump(characters, writeFile, indent=4)





def characterCreator():

    firstNames = webScraper.getNames()
    lastNames = webScraper.getLastNames()
    jobs = webScraper.getJobs()
    countries = webScraper.getCountries()

    #creates a dictionary for a random character
    characters = [
        {
            "firstName" : firstNames[randomIndex],
            "lastName" : random.choice(lastNames),
            "age" : random.randrange(25,66),
            "sex" : "female" if randomIndex % 2 else "male",
            "occupation" : random.choice(jobs),
            "location" : random.choice(countries),
        }
        for index in range(30)
        if (randomIndex := random.randrange(len(firstNames)))
    ]

    
    return characters





if __name__ == "__main__":
    
    main()