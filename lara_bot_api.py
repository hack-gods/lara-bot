from flask import Flask,jsonify
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import lara_bot as lb


# flask config
app = Flask(__name__)


@app.route("/")
def index():
    return 'conected'


@app.route("/bot")
def first_message():
    return jsonify(lb.first_lara_message())


@app.route('/bot/<message>')
def get_message_and_return_json(message):
    response = lb.get_user_message(message)
    return jsonify(response)


if __name__ == '__main__':
    ## enter the IP and port of your choice
    app.run('192.168.1.202', 5000)
