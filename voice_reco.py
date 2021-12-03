import speech_recognition as sr

def voice_reco():
    rObject = sr.Recognizer() 
    audio = ''

    with sr.Microphone(device_index=0) as source: 
        print("Speak...") 
        rObject.adjust_for_ambient_noise(source, duration=2)  
        audio = rObject.listen(source, phrase_time_limit = 0) 
        rObject.pause_threshold = 0.8 
        print("Stop.")
        try: 
            text = rObject.recognize_google(audio) 
            print("You : "+ text)  
            return text

        except: 
            print("Could not understand your audio...PLease try again !")
            return
            

while True:

    if voice_reco()=="start":
       print("start the robot")

    elif voice_reco()=="order":                
        print("robot do the order")

    elif voice_reco()=="stop":
        break  
    else :
        print("anything")