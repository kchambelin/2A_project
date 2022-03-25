import speech_recognition as sr
import re
import nltk
from nltk.tokenize import word_tokenize


def voice_reco():
    rObject = sr.Recognizer() 
    audio = ''

    with sr.Microphone(device_index=0) as source: 
        print("Speak...") 
        rObject.adjust_for_ambient_noise(source, duration=0.5)  
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
    
    text = voice_reco()
    if text!=None:
        text_token = word_tokenize(text)
        print(text_token)
        text_token = re.sub(r"[^a-zA-Z0-9]", " ", str(text.lower()))
        text_token_lower = text_token.split()
        print(text_token_lower)
        filtered_list = []
        spe_words = ["begin", "stop","reproduce", "blue", "red", "green", "square", "triangle", "cylinder", "star"]
        for word in text_token_lower:
            if word.casefold() in spe_words:
                filtered_list.append(word)
        print(filtered_list)
        
        if filtered_list!=[]:

            if "begin" in filtered_list:
                print("start the robot")

            elif "reproduce" in filtered_list:                
                print("robot do the order")
                
            elif "blue" and "star" in filtered_list:                
                print("robot do the order")

            elif "stop" in filtered_list:
                break