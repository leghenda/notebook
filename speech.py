import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    r_speach = r.recognize_google(audio,language="ru-RU")
    print('вы скозали:' + r_speach)

