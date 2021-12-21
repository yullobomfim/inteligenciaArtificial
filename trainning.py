from os import close
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSATIONS_PATH = [
    'config/greetings.json',
    'config/loja_info.json',
    'config/questions.json'
]

class Trainning:
    def __init__(self):
        self.robo = ChatBot('Personalize')
        self.trainer = ListTrainer(self.robo)

    def main(self):
        conversations = self.load_conversations()
        
        if conversations:
            self.train(self, conversations)

    @staticmethod
    def load_conversations():
        conversations = []

        for config_file in CONVERSATIONS_PATH:
            with open(config_file, 'r') as file:
                info = json.load(file)
                conversations.append(info['conversations'])

                file.close()

        return conversations

    @staticmethod
    def train(self, conversations):
        for conversation in conversations:
            for messages_answers in conversation:
                messages = messages_answers['messages']
                answers = messages_answers['answers']
                
                print('robo training... : ', messages, ' /// ',answers)
                for message in messages:
                    self.trainer.train([message, answers])
                    
t = Trainning()

t.main()