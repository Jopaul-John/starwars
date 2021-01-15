import requests
from bs4 import BeautifulSoup
import wikia

urls = {
    "https://www.cnet.com/pictures/star-wars-spaceships-ranked-by-power-speed/": "h2",
    "https://en.wikipedia.org/wiki/List_of_Star_Wars_spacecraft": "h3"
}

# reads the html page from url
def getPage(pageName: str) -> str:
    pageData = requests.get(pageName)
    return pageData.text

# get the soup page of corresponding html page
def getSoupPage(pageData: str) -> BeautifulSoup:
    soup = BeautifulSoup(pageData, 'html.parser')
    return soup

# tags to get the shipnames from their respective urls
def filterTags(soupPage: BeautifulSoup, tag: str, shipNames: list) -> list:
    if tag == "h3":
        print("reading wiki")
        headertags = soupPage.find_all(tag)
        for headertag in headertags:
            spans = headertag.find_all("span")
            if len(spans) > 2:
                if spans[0].text == "":
                    shipNames.append(spans[1].text.encode('ascii', 'ignore').decode("utf-8"))
                else:
                    shipNames.append(spans[0].text.encode('ascii', 'ignore').decode("utf-8"))
    else:
        print("reading cnet")
        headertags = soupPage.find_all("h2", {"class": "c-gallerySlide_hed"})
        for headertag in headertags[1:]:
            try:
                shipNames.append(headertag.text.split(". ")[1].encode('ascii', 'ignore').decode("utf-8"))
            except:
                pass
    return shipNames

# extracts the html tags from soup
def getFeaturesFromStarwar(starpagesoup: BeautifulSoup) -> list:
    features = starpagesoup.findAll(
        "div", {"class": "pi-item pi-data pi-item-spacing pi-border-color"})
    hyperdriveRating = "100"
    hyperdriveRatingBackup = "100"
    for index, feature in enumerate(features):
        if "rating" in feature.text:
            try:
                listTags = feature.find_all("li")
                hyperdriveRating = listTags[0].text.split("[")[0].split(" ")[1]
                hyperdriveRatingBackup = listTags[1].text.split("[")[0].split(" ")[1]
            except:
                try:
                    hyperdriveRating = feature.text.split("\n")[
                        2].split("[")[0].split(" ")[1]
                    hyperdriveRatingBackup = None
                except:
                    print("Cannot find hyper drive rating ")

    return [hyperdriveRating, hyperdriveRatingBackup]

# parse the wiki page and converts the corresponding soup page for extracting the html tags
def readRating(wikiPage: wikia.wikia.WikiaPage, shipName: str, wikiPagesId: list) -> list:
    alternateName = None
    listRatings = None
    if not wikiPage.pageid in wikiPagesId:
        wikiPagesId.append(wikiPage.pageid)
        soupPage = getSoupPage(wikiPage.html())
        listRatings = getFeaturesFromStarwar(soupPage)
    else:
        alternateName = "exists"
    return alternateName, listRatings

# goes to starwars fandom wiki page and reads the page with corresponding ship name
def getHyperDriveRating(ship: str, wikiPagesId: list) -> dict:
    wikiPage = None
    alternateName = None
    datas = None
    try:
        wikiPage = wikia.page("starwars", ship)
    except:
        try:
            trimmedName = ship.split(" (")
            wikiPage = wikia.page("starwars", trimmedName[0])
        except:
            try:
                wikiPage = wikia.page("starwars", trimmedName[1][:-2])
            except:
                pass
    if wikiPage:
        alternateName, datas = readRating(wikiPage, ship, wikiPagesId)    
    return alternateName, datas

# returns list of ships
def getShipNames() -> list:
    shipNames = []
    for url, header in urls.items():
        requestPage = getPage(url)
        soupPage = getSoupPage(requestPage)
        shipNames = filterTags(soupPage, header, shipNames)
    return shipNames

# to run as a python service
# def main():
    # wikiPagesId = []
    # shipNames = []
    # for url, header in urls.items():
    #     requestPage = getPage(url)
    #     soupPage = getSoupPage(requestPage)
    #     shipNames = filterTags(soupPage, header, shipNames)
    # print(shipNames)
    # print(len(shipNames))
    # data = getHyperDriveRating(shipNames)
    # print(data)


# if __name__ == "__main__":
#     main()
