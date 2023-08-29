import time , winsound

timeSecond = int(input("please enter the time in second : ")) 

while timeSecond > 0 :
    mins , secs = divmod(timeSecond , 60)
    hours , mins1 = divmod (mins , 60)
    timer = str(hours) + ":" + str(mins1) + ":" + str(secs)
    print(timer, end="\r")
    time.sleep(1)
    timeSecond -= 1
winsound.Beep(2500,1000)