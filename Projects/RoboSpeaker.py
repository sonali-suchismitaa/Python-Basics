import pyttsx3
if __name__ == '__main__':
    print("Welcome to RoboSpeaker version 0.1 by Kaykobad : ")
    while True:
        x = input("Enter what you want the system to speak: ")
        if(x=='q'):
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()   