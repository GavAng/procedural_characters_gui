#modules
import requests
from bs4 import BeautifulSoup





def getTableData(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup.find("tbody")




def getNames():

    nameTable = getTableData("https://www.ssa.gov/oact/babynames/decades/century.html")
    #get all the table data that is not a numerical figure
    nameElements = nameTable.find_all(
        "td", string = lambda text : not str(text)[0].isdigit()
    )


    #gets just the strings of names
    names = [
        nameElement.text for nameElement in nameElements[:-2]
    ]
    
    return names





def getLastNames():

    nameTable = getTableData("https://www.thoughtco.com/most-common-us-surnames-1422656")
    nameElements = nameTable.find_all("td")

    lastNames = [
        nameElement.text for nameElement in nameElements[1::4]
    ]


    return lastNames





def getJobs():

    jobTable = getTableData("https://www.careeronestop.org/Toolkit/Careers/careers-largest-employment.aspx?pagesize=50&currentpage=1&nodata=")
    #get all the table data
    jobElements = jobTable.find_all("td")


    #gets just the singular job titles from the list
    jobTitles = list({
        #return the job title without the s at the end
        jobTitle[:-1]
        if jobTitle[-3:-1] != "ie" 
        #if job title ends in "ies" return it with a "y" instead
        else jobTitle[:-3] + "y"

        #for every 5th element in the last starting at element 2
        for jobElement in jobElements[1::5] 
        if (jobTitle := jobElement.text.split(", ", 1)[0].split(" and ", 1)[0].split(" of ", 1)[0])[-1] == "s"
    })


    return jobTitles





def getCountries():

    countryTable = getTableData("https://www.worldometers.info/geography/alphabetical-list-of-countries/")
    #get all the table data that is not a numerical figure
    countryElements = countryTable.find_all("td")


    #gets just the current country names from the list where the population is greater than 3,000,000
    countryNames = [
        countryElements[index + 1].text.split(" (", 1)[0]
        for index in range(0,len(countryElements),5)
        if int(countryElements[index + 2].text.replace(",","")) > 3000000
    ]
    
    
    return countryNames





if __name__ == "__main__":

    print(getNames())
    print(getLastNames())
    print(getJobs())
    print(getCountries())
