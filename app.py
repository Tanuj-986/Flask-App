from flask import Flask, request

from flask import send_from_directory

from flask import redirect, url_for

from STT_TTS import STT, TTS

from Brain import brain

import time

from flask import make_response, send_file



app = Flask(__name__)


# @app.route('/')
# def index():
#     return "<h1> Hello World <h1>"

# @app.route('/hello')
# def hello():
#     return "<h1> Hello <h1>"

# @app.route('/greet/<name>')
# def greet(name):
#     return f"<h1> Hello {name} <h1>"

# @app.route('/sum/<int:num1>/<int:num2>')
# def sum(num1, num2):
#     return f"<h1> The sum of {num1} and {num2} is {num1 + num2} <h1>"




##################################################################################

@app.route('/upload', methods=['POST', 'GET'])
def upload_audio():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file.save(f"./audio_file/{file.filename}")


    t1 = time.time()

    prompt = STT(f"./audio_file/{file.filename}")
    response = brain(prompt)
    TTS(response, "./audio_file/response.wav")
    t2 = time.time()

    t3 = t2-t1
    print(f"Response time: {t3}")

    response = make_response(send_file('./audio_file/response.wav', as_attachment=True))
    response.headers['X-Time-Taken'] = str(t3)
    return response

    # return send_from_directory('./audio_file', 'response.wav', as_attachment=True)

    # return f'File uploaded successfully', 200




@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    upload_folder = './audio_file/'
    return send_from_directory("audio_file\\response.wav")

##################################################################################




if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)