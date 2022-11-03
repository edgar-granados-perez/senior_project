from selenium import webdriver

# the chrome version for this application is chrome 107
def setbrowserOS():
        macPath = '/Users/edgargranadosperez/Desktop/Git Projects/senior_project/src/chromedrivermac'
        windowsPath = 'C:\\Users\\myPC\\iCloudDrive\Desktop\\Git Projects\\senior_project\\src\\chromedriver.exe'
        browser = None
        while True:
            os = input("which operating system are you running this code on? mac or windows: ")
            if os in ("mac","windows"):
                if os == "mac":
                    browser = webdriver.Chrome(executable_path= macPath)
                    print("chose mac")
                    return browser
                elif os == "windows":
                    browser = webdriver.Chrome(executable_path=windowsPath)
                    print("chose windows")
                    return browser
            else :
                print("please type the correct os either \"mac\" or \"os\"")

def startwebcrawler():
    pubmed ='https://pubmed.ncbi.nlm.nih.gov/'
    browser = setbrowserOS()
    browser.get(pubmed)

startwebcrawler()
