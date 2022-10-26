from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()




#AIAI
#AskItAnswerIt questions and answers web app
#Writter and released by Georgios Zacharidis
#-thank you for reading this code
