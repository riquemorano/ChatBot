#UFT-8
import logging
from chatterbot import ChatBot

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

chatbot = ChatBot('Chatbot')

print("Chatbot: Olá")

while True:
    
    try:
        entrada = input("Você: ").lower()
        if(entrada == "sair" or entrada == "exit" or entrada == "tchau"):
            break    
        saida = chatbot.get_response(entrada.capitalize())
        if float(saida.confidence) > 0.8:

            print('Chatbot: ', saida)
        else:
            print('Chatbot: Não Entendi')
    except(KeyboardInterrupt, EOFError, SystemExit):
        break