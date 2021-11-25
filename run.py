import speech_recognition as sr
from nltk import word_tokenize, corpus
import json

IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"
CAMINHO_CONFIGURACAO = "config.json"

def iniciar():
    global reconhecedor
    global palavras_de_parada
    global nome_assistente
    global acoes


# Record Audio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale alguma coisa!")
    audio = r.listen(source)

try:
    print("Você falou: " + r.recognize_google(audio,language='pt-BR'))
except sr.UnknownValueError:
    print("Não entendi o que você falou... Por favor, repita a frase novamente")
except sr.RequestError as e:
    print("Não consegui reconhecer este comando.; {0}".format(e))