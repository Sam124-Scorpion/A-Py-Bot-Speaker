import time
import win32com.client as winner

speak = winner.Dispatch("SAPI.SpVoice")

print(("***************Welcome to RoboSamSpeaker 2.0*************"))
print("\t\t\t press 'q' for quiet")

speak.Speak("Welcome boss  and other users !!!!!  myself Robosam 2.0 made with love by sam !")

speak.Speak("please order me to speak anything by the script write that given below ")
while True:
    text = input("enter the text that u want to speak :: ")

    if text == 'q':
        speak.Speak(f"goodbye Boss!! see you soon!")
        time.sleep(0.002)
        print("\t\t\t\t Made with Love By THeSam ")
        break


    speak.Speak(f"{text} ") #using f-string#

    #time.sleep(0.10)

    #speak.Speak("that's really awesomw u know it!!")

