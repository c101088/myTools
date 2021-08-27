from flask import Flask

from src.FileSaveService import *


app = Flask(__name__)
app.register_blueprint(FileSaveService,url_prefix='/file')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/getWordContent')
def get_word_content():  # put application's code here
    fileName = request.files['fileName']
    text=getWordFileText(fileName)
    return text



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5500)
