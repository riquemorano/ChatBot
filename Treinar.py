from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

while True:

    nome = input("Digite o nome do arquivo: ")
    if (nome == "exit"):
        break
    else:
        chatbot = ChatBot('Ramona')
        trainer = ListTrainer(chatbot)
        treino = open("Conversas" + '/' + nome + '.txt', 'r', encoding="utf8")
        trainer.train(treino.readlines())




