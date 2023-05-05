#modules
import re
import requests
from bs4 import BeautifulSoup



def getTableData(url):

    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find("tbody")



def getNames():

    nameTable = getTableData("https://www.ssa.gov/oact/babynames/decades/century.html")
    #get all the table data that is not a numerical figure
    nameElements = nameTable.find_all(
        "td", string = lambda text : not str(text)[0].isdigit()
    )

    #gets just the strings of names
    return [nameElement.text for nameElement in nameElements[:-2]]



def getLastNames():

    nameTable = getTableData("https://www.thoughtco.com/most-common-us-surnames-1422656")
    nameElements = nameTable.find_all("td")

    return [nameElement.text for nameElement in nameElements[1::4]]



def getJobs():

    jobTable = getTableData("https://www.careeronestop.org/Toolkit/Careers/careers-largest-employment.aspx?pagesize=50&currentpage=1&nodata=")
    #get all the table data
    jobData = jobTable.find_all("td")

    # Only accept job titles (every 5th cell in the table) where the title (cut down) ends in an 's'
    return list({jobTitle[:-1] 
            if jobTitle[-3:-1] != "ie" 
            else jobTitle[:-3] + "y"
            for jobElement in jobData[1::5]
            if (jobTitle := re.split(",| and | of ", jobElement.text.strip())[0])[-1] == "s"
    })



def getCountries():

    countryTable = getTableData("https://www.worldometers.info/geography/alphabetical-list-of-countries/")
    countryElements = countryTable.find_all("td")

    #gets just the current country names where the population is greater than 3,000,000
    countryNames = [
        countryElements[index + 1].text.split(" (", 1)[0]
        for index in range(0,len(countryElements),5)
        if int(countryElements[index + 2].text.replace(",","")) > 10_000_000
    ]
    return countryNames



if __name__ == "__main__":

    #print(getNames())
    #print(getLastNames())
    #print(getJobs())
    print(getCountries())
