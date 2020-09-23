import Main
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

while True:
    try:
        nome = input("Digite o nome do arquivo: ").lower()
        if (nome == "exit" or nome == "sair"):
            break
        else:
            chatbot = ChatBot('Ramona')
            trainer = ListTrainer(chatbot)
            treino = open("Conversas" + '/' + nome + '.txt', 'r', encoding="utf8")
            trainer.train(treino.readlines())
    except(KeyboardInterrupt, EOFError, SystemExit):
        break