import urllib
def readText():
    #open function returns object of type file, open internally calls a constructor i.e init function
    data=open(r"C:\Users\Dell\Desktop\python\DirtyWordCHeckInDoc\ProfanityCheck.txt")
    contentsOfFile=data.read()
    #print(contentsOfFile)
    data.close()
    checkProfanity(contentsOfFile)
def checkProfanity(textToCheck):
    #connection to website on internet
    #urllib.urlopen connects to the website given
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+textToCheck)
    #reads the result on web page 
    result=connection.read()
    #print(result)
    connection.close()
    if result=="true":
        print "Profanity Alert"
    elif "false" in result:
        print "There is no curse word in doc"
    else:
        print "cannot open doc"
    
readText()
