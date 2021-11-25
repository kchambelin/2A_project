# import speech_recognition
# import pyttsx3

# recognizer=speech_recognition.Recognizer()

# while True:

#     try:
#         with speech_recognition.Microphone() as mic:
#             print('test')

#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio=recognizer.listen(mic)

#             text=recognizer.recognize_google(audio)
#             text=text.lower()

#             print(text)
    
#     except :

#         recognizer=speech_recognition.Recognizer()
#         continue

import speech_recognition as sr
rObject = sr.Recognizer() 
audio = ''
with sr.Microphone(device_index=0) as source: 
    print("Speak...") 
    rObject.adjust_for_ambient_noise(source, duration=5)  
    audio = rObject.listen(source, phrase_time_limit = 0) 
    print("Stop.")
    try: 
        text = rObject.recognize_google(audio, language ='fr-FR') 
        print("You : "+ text)  
    except: 
        print("Could not understand your audio...PLease try again !") 