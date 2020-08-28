from os import system, name
import logging
from chatterbot import ChatBot

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


chatbot = ChatBot('Ramona')

clear()
print("Ramona: Olá")

while True:

    quest = input("Você: ").capitalize()
    if(quest == "sair".capitalize()):
        break
    response = chatbot.get_response(quest)
    print('Ramona: ', response)
