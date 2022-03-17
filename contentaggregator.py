from selenium import webdriver
from bs4 import BeautifulSoup




driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


def run_scrapper_google(searchKey):

    q = searchKey.replace("+", " ")
    driver.get("https://www.google.com/search?q="+ q +"&oq="+ q +"&aqs=chrome.2.69i57j0i512l9.7037j0j7&sourceid=chrome&ie=UTF-8")
    soup = BeautifulSoup(driver.page_source)
    for a in soup.findAll('a',href=True):
        if a["href"][0] != "/":
            print(a["href"])    



def run_scrapper_stackoverflow(searchKey):
    q = searchKey.replace("+", " ")

    driver.get("https://stackoverflow.com/search?q=" + q)

    soup = BeautifulSoup(driver.page_source)

    # /questions
    for a in soup.findAll('a',href=True):
        if len(a["href"]) > 10 and a["href"][:10] == "/questions":
            print("https://stackoverflow.com/"+a["href"])   




if __name__ == "__main__":
    

    userinput = input("Enter search key: ")

    print("Searching google .....")
    run_scrapper_google(searchKey=userinput)
    print("Finished searching google")

    answer = input("Would you like me to search stackoverflow? [yes/no]: ")
    while answer != "yes" and answer != "no":
        answer = input("I guess there is a typo! Would you like me to search stackoverflow? [yes/no]: ")


    print("Searching stackoverflow ......")
    run_scrapper_stackoverflow(searchKey=userinput)
    print("Finished searching stackoverflow")