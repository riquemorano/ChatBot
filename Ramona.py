import logging 

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

from chatterbot import ChatBot
chatbot = ChatBot('Ramona')

while True:
    quest = input("Você: ").capitalize()
    response = chatbot.get_response(quest)
    print('Ramona: ', response)