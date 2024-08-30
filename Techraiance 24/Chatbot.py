from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time


time.clock = time.time()

chatbot = ChatBot("My Bot")
Trainer = ChatterBotCorpusTrainer(chatbot)

Trainer.train("chatterbot.corpus.english")

while True:
    try:
        inp = input("You>>> ")
        res = chatbot.get_response(inp)
        print(f"My Bot>>> {res}")
    except:
        if KeyboardInterrupt() or SystemExit():
            break