import speech_recognition as sr

rObject = sr.Recognizer() 
audio = ''

with sr.Microphone(device_index=0) as source: 
    print("Speak...") 
    rObject.adjust_for_ambient_noise(source, duration=1)  
    audio = rObject.listen(source, phrase_time_limit = 0) 
    print("Stop.")
    try: 
        text = rObject.recognize_google(audio) 
        print("You : "+ text)  
        # reco des mots
        if text=="start":
            print("start the robot")
        elif text=="order":
            print("robot do the order")
        elif text=="stop":
            print("stop the robot")

            
    except: 
        print("Could not understand your audio...PLease try again !")

