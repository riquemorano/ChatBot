import logging
import os.path
from os import system, name
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

palavras_sair = ("sair", "tchau", "exit", "bye")


def sair():

    try:
        limpa_tela()
        print("Realmente quer sair?\n")
        print("1 - Sim\n2 - Não\n")
        resposta = int(input("Digite a Opção desejada: "))

        if resposta == 1:
            return True

        elif resposta == 2:
            return False
    except(KeyboardInterrupt, EOFError, SystemExit):
        exit()


def limpa_tela():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def pausa():
    if name == 'nt':
        _ = system('pause')
    else:
        _ = system("read -n1 -r -p 'Press any key to continue...' key")


class Bot:

    def __init__(self, nome_bot="Chatbot"):

        self.nome_bot = nome_bot

    def conversar(self):

        logger = logging.getLogger()
        logger.setLevel(logging.CRITICAL)
        chatbot = ChatBot(self.nome_bot)
        limpa_tela()
        print(f'{self.nome_bot}: Olá')
        while True:
            try:
                entrada = input("Você: ").lower().lstrip(' ')
                if(entrada in palavras_sair):
                    if sair():
                        break
                else:
                    saida = chatbot.get_response(entrada.capitalize())
                    if float(saida.confidence) > 0.8:
                        print(f'{self.nome_bot}: {saida}')
                    else:
                        print(f'{self.nome_bot}: Não Entendi')
            except(KeyboardInterrupt, EOFError, SystemExit):
                if sair():
                    break

    def treinar(self):

        while True:
            try:
                limpa_tela()
                nome_arquivo = input(
                    "Digite o nome do arquivo: ").lower().lstrip(' ')
                caminho = ("Treinamentos" + '/' + nome_arquivo + '.txt')
                if (nome_arquivo in palavras_sair):
                    if sair():
                        break
                elif (os.path.exists(caminho)):
                    print(
                        f'\nProcurando arquivo no seguinte caminho: {caminho}')
                    print(f'\nArquivo {nome_arquivo} encontrado')
                    chatbot = ChatBot(self.nome_bot)
                    trainer = ListTrainer(chatbot)
                    treino = open(caminho, 'r', encoding="utf8")
                    trainer.train(treino.readlines())
                    pausa()
                else:
                    print(f'\nArquivo {nome_arquivo} não encontrado')
                    pausa()
                    limpa_tela()
            except(KeyboardInterrupt, EOFError, SystemExit):
                if sair():
                    break


bot = Bot()
while True:
    try:
        limpa_tela()
        print("1 - Treinar\n2 - Conversar\n3 - Sair")
        resposta = int(input("\nDigite a Opção desejada: "))
        if resposta == 1:
            bot.treinar()
        elif resposta == 2:
            bot.conversar()
        elif resposta == 3:
            if sair():
                break
        else:
            print("Resposta Inválida")
            pausa()
    except(KeyboardInterrupt, EOFError, SystemExit):
        if sair():
            break
