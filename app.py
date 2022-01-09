from flask import Flask, render_template, request
app = Flask(__name__)

# Importing chatterbot
from chatterbot import ChatBot
 
# Create object of ChatBot class with Logic Adapter
bot = ChatBot('Buddy')

# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])
#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()


    
"""
#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english






from flask import Flask
app = Flask(__name__)

# Importing chatterbot
from chatterbot import ChatBot
 
# Create object of ChatBot class with Logic Adapter
bot = ChatBot('Buddy')

# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

@app.route("/get")
#function for the bot response
def get_bot_response():
    #userText = request.args.get('msg')
    return str(bot.get_response("hi"))

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

"""
