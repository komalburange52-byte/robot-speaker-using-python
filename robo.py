import win32com.client as wincil

if __name__ == "__main__":
    print("welcome to robot speaker 1.1, created by komal")
    speaker=wincil.Dispatch("SAPI.SpVoice")      #windows

    while True:
        x=input("enter what you want me to speak :")

        if x.lower()=="q":
            speaker.Speak("bye bye freind")
            break
        speaker.speak(x)
