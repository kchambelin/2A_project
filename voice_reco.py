import speech_recognition as sr

rObject = sr.Recognizer() 
audio = ''

with sr.Microphone(device_index=0) as source: 
    print("Speak...") 
    rObject.adjust_for_ambient_noise(source, duration=2)  
    audio = rObject.listen(source, phrase_time_limit = 0) 
    print("Stop.")
    try: 
        text = rObject.recognize_google(audio) 
        print("You : "+ text)  
        # reco des mots
        if text=="hello":
            print("yes")

            
    except: 
        print("Could not understand your audio...PLease try again !")

