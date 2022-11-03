from selenium import webdriver

# the chrome version for this application is chrome 107
class webcrawler:
    macPath = ''
    windowsPath = 'C:\\Users\\myPC\\iCloudDrive\Desktop\\Git Projects\\senior_project\\src\\chromedriver.exe'
    url= 'https://pubmed.ncbi.nlm.nih.gov/'
    browser = webdriver.Chrome(executable_path= windowsPath)



    def setbrowserOS():
         while True:
            os = input("which operating system are you running this code on? mac or windows: ")
            if os in ("mac","windows"):
                break
            else :
                print("please type the correct os either \"mac\" or \"os\"")
        
         print("chose the correct value")
        
