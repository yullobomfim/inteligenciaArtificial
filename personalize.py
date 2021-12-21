from chatterbot import ChatBot
import json

class Personalize:
    def main(self): 
        robo = ChatBot('Personalize')
        
        while True:
            question = input('Olá, eu sou o robo de atendimento da Personalize Festas. Me faça uma pergunta:')
            answer = robo.get_response(question)
            
            if answer.confidence > 0.6:
                print(answer.text)
            else:
                print('Este assunto deve ser tratado pessoalmente... Por favor, me faça outra pergunta:  ')
                
p = Personalize()

p.main()
