import speech_recognition as sr
from nltk import word_tokenize, corpus
import json

def start():
    micro = sr.Recognizer()
    palavras_de_parada = set(corpus.stopwords.words('portuguese'))
    with sr.Microphone() as fonte_audio:
        micro.adjust_for_ambient_noise(fonte_audio)
        
        print("Escuta...")        
        fala = micro.listen(fonte_audio, timeout=5, phrase_time_limit=5)

        try:
            comandos = micro.recognize_google(fala, language="pt-BR")
            print(f'você falou: {comandos}')
        except sr.UnknownValueError:
            print("Não entendi")

    
 # aqui temos as palavras em array
    tokenizador = word_tokenize(comandos, 'portuguese')
    comando_filtrado = []
    for comando in tokenizador:
        if comando not in palavras_de_parada:
            comando_filtrado.append(comando)

# ja temos as palavras filtradas
    return comando_filtrado

def buscar_config():

    with open('config.json', "r") as comandos_configuracao:
        obj_config = []
        try:
            config = json.load(comandos_configuracao)
            comandos_configuracao.close()
        except:
            print('Não localizei o config')
        return config
     
def executar_assistente(config, comando):
    nome_assistente = config["nome"]
    acoes = config['acoes']
    nome_assistente_chamado = comando[0]
    comando_acao_chamado = comando[1]
    comando_objeto_chamado = comando[2]

    acao_validada = False
    objeto_validado = False

    #obter e comparar nome do assistente
    if nome_assistente.lower() == nome_assistente_chamado.lower():
            for acao in acoes:
                if acao['nome'] in comando_acao_chamado:
                    acao_validada = True
                    print(f'Entendi a ação: {comando_acao_chamado}')
            if acao_validada == True:
                for objeto in acoes:
                    if objeto['objetos'] == comando_objeto_chamado:
                        objeto_validado = True
                if objeto_validado == True:
                    print(f'Ação {comando_acao_chamado} {comando[2]} executada com sucesso...')
                else:
                    print(f'Ainda não temos o objeto {comando_objeto_chamado}')    
            else:
                return print('Ainda não aprendi essa ação...')        
    else:
        print(f'Não conheco nenhum {comando[0]}')


def __main__():
    config = buscar_config()
    comando = start()
    
    executar_assistente(config, comando)
      
__main__()