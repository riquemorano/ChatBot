import logging
import os.path
from os import system, name
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class Bot:

    def __init__(self, nome_bot="Chatbot"):
        self.nome_bot = nome_bot

    def clear(self):

        if name == 'nt':
            _ = system('cls')

        else:
            _ = system('clear')

    def conversar(self):

        logger = logging.getLogger()
        logger.setLevel(logging.CRITICAL)

        chatbot = ChatBot(self.nome_bot)

        self.clear()

        print(f'{self.nome_bot}: Olá')

        while True:
            try:
                entrada = input("Você: ").lower()
                if(entrada == "sair" or entrada == "exit" or entrada == "tchau"):
                    break
                saida = chatbot.get_response(entrada.capitalize())
                if float(saida.confidence) > 0.8:
                    print(f'{self.nome_bot}: {saida}')
                else:
                    print(f'{self.nome_bot}: Não Entendi')
            except(KeyboardInterrupt, EOFError, SystemExit):
                break

    def treinar(self):
        
        while True:
            try:
                nome_arquivo = input("\nDigite o nome do arquivo: ").lower()
                caminho = ("Conversas" + '/' + nome_arquivo + '.txt')
                print(
                    f'\nProcurando arquivo no seguinte caminho: {caminho}')
                if (nome_arquivo == "exit" or nome_arquivo == "sair"):
                    break

                elif (os.path.exists(caminho)):
                    print(f'\nArquivo {nome_arquivo} encontrado')
                    chatbot = ChatBot(self.nome_bot)
                    trainer = ListTrainer(chatbot)
                    treino = open(caminho, 'r', encoding="utf8")
                    trainer.train(treino.readlines())
                else:
                    print(f'\nArquivo {nome_arquivo} não encontrado')
                    break
                self.clear()
            except(KeyboardInterrupt, EOFError, SystemExit):
                break


bot = Bot()


bot.conversar()
bot.treinar()
