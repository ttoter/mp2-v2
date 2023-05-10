from flask import Flask, request
import json
import subprocess
import socket
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def num_parm():

    print('===============================================')
    print('===============================================')
    print('===============================================')
    print(request.content_type) #application/json
    print(request.data.decode("utf-8")) #application/json
    print('====')
    
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Running..."
    if request.method == 'GET':
        return socket.gethostname()

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)