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
'When will Chandan be available to start working?',
'Chandan is available for an internship in the summer/fall of 2022 & for full time employment in May 2023.',
'How can I contact Chandan?',
'Please email Chandan at cchandel@uwo.ca',
'Is Chandan looking for an internship or a job right now?',
'Chandan is actively searching for internships at this point in time.',
'Where can I find Chandan resume?',
'There is a link available in the Nav bar',
'Where is Chandan CV?',
'There is a link available in the Nav bar',
'Where is Chandan resume?',
'There is a link available in the Nav bar',
'What school did Chandan go to?',
'Chandan completed his Undergrad at Western University and is working on his Masters at the same school.',
'When is Chandan available for an interview?',
'Chandan is typically busy between 8am and 5pm EST on business days, but can make time during the afternoon (typically 11am-12pm). Please contact Chandan for more information.',
'What project is Chandan most proud of?',
'Please take a look at some of the project links shown above and feel free to check out my Github.',
'Where can I find a link to Chandans Github?',
'Please check out the top of the page where an icon linking to my Github is available.',
'Where can I find a link to Chandans LinkedIn?',
'Please check out the top of the page where an icon linking to my LinkedIn is available.',
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
