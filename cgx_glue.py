import socket
from flask import Flask

app = Flask(__name__)

HOST = '127.0.0.1'
PORT = 50000
RELAY_PORT = 51000

@app.route('/<trigger_value>')
def trigger(trigger_value):
        trigger_value = trigger_value
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, RELAY_PORT))
        s.send(bytes(trigger_value, encoding='utf8'))
        data = s.recv(1024)
        s.close()

if __name__ == '__main__':
	app.run(host=HOST, port=PORT)
