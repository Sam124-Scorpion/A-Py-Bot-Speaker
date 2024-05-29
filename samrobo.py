import time

import win32com.client as w

speak = w.Dispatch("SAPI.SpVoice")

text = "Hey! is everything alright ?"
speak.Speak(text)
time.sleep(1)
text2  = input("enter text :: ")
speak.Speak(print(f"hello mr {text2}"))