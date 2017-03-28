import webbrowser
import time

count=0
print "The prog started at "+time.ctime()
while(count<3):
    #sleep for 10 sec
    time.sleep(5*60) 
    #webbrowser will open and directed to the link given
    webbrowser.open("www.youtube.com") 
    count=count+1
print "The prog ended at "+time.ctime() #ctime prints current time
print "Done"
