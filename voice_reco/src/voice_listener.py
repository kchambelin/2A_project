#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String

import random

import speech_recognition as sr
import re
import nltk
from nltk.tokenize import word_tokenize

def talker(list):
    pub = rospy.Publisher('voice_reco', String, queue_size=10)
    msg=""
    for i in list:
        msg=msg +str(i) + ","
    time.sleep(0.1)
    pub.publish(String(msg))




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
            text = str(rObject.recognize_google(audio))
            print("You : "+ text)  
            return text

        except : 
            print("Could not understand your audio...PLease try again !")
            time.sleep(1)
            text =''
            return text


def Voice_recognition():
    text = voice_reco()
    if text!=None:
        text_token = word_tokenize(text)
        print(text_token)
        text_token = re.sub(r"[^a-zA-Z0-9]", " ", str(text.lower()))
        text_token_lower = text_token.split()
        print(text_token_lower)
        filtered_list = []
        spe_words = ["begin", "initialise", "go", "stop","reproduce", "blue", "red", "green", "square", "triangle", "cylinder", "star","pick"]
        for word in text_token_lower:
            if word in spe_words:
                filtered_list.append(word)            
        rospy.loginfo(filtered_list)
        if filtered_list == [] :
            print('Unknown order.')
            time.sleep(1)
            Voice_recognition()
        else:		 
            talker(filtered_list)

def callback(data):
    if data.data == 'Initialize' :
        Voice_recognition()
    elif data.data == 'Waiting for order...' :
        Voice_recognition()

def listener():
    rospy.init_node('voice_listener', anonymous=True)
    rospy.Subscriber("main_voice_reco", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        

if __name__ == '__main__':
    try:
        print('Voice_listener here')
        listener()
    except rospy.ROSInterruptException:
        pass
