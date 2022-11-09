from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# the chrome version for this application is chrome 107
def setbrowserOS():
        macPath = '/Users/edgargranadosperez/Desktop/Git Projects/senior_project/src/chromedriver'
        windowsPath = 'C:\\Users\\myPC\\iCloudDrive\Desktop\\Git Projects\\senior_project\\src\\chromedriver.exe'
        browser = None
        while True:
            os = input("which operating system are you running this code on? mac or windows: ")
            if os in ("mac","windows"):
                if os == "mac":
                    browser = webdriver.Chrome(executable_path= macPath)
                    return browser
                elif os == "windows":
                    browser = webdriver.Chrome(executable_path=windowsPath)
                    return browser
            else :
                print("please type the correct os either \"mac\" or \"windows\"")

def convertAdvanced(symptom:str):
    advancedString: str  = "({}[Title/Abstract])".format(symptom)
    return advancedString


def symptomsAdvancedQuery (browser: webdriver, site: str, symptoms: list[str]):
    advancedSearch: str = ''
    for i, line in enumerate(symptoms):
        if i ==  len(symptoms)-1: 
            last = convertAdvanced(symptom= line)
            advancedSearch += last
            advancedSearch += " AND (gene[Text Word])"
            print(advancedSearch)
            break
        sym = convertAdvanced(symptom= line)
        advancedSearch +=  "{} AND ".format(sym)
        
    
    browser.get(site)
    e = browser.find_element("id",'id_term')
    e.send_keys(advancedSearch)
    e.send_keys(Keys.ENTER)

def individualQuery(browser: webdriver, site: str, symptoms: list[str]):
    for i in symptoms:
        sepSearch = convertAdvanced(i) + " AND (gene[Text Word])"
        browser.get(site)
        e = browser.find_element("id",'id_term')
        e.send_keys(sepSearch)
        e.send_keys(Keys.ENTER)
def symptomQuestion():
    symptom = input("What is a symptom of the disease?: ")
    return symptom
    

def symptomList():
    list = []
    symptom = symptomQuestion()
    list. append(symptom)
    while True:
        userResponse = input("Would you like add a symptom. yes or no: ")
        if userResponse in ["yes", "no"]:
            if userResponse == "yes":
                symptom = symptomQuestion()
                list.append(symptom)
            elif userResponse == "no":
                return list
                break
        else: 
            print("type yes or no")


def startwebcrawler():
    global browser
    browser = setbrowserOS()
    symptoms = symptomList()
    pubmed ='https://pubmed.ncbi.nlm.nih.gov/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    symptomsAdvancedQuery(browser=browser, site= pubmed, symptoms= symptoms)
    individualQuery(browser=browser, site= pubmed, symptoms= symptoms)


