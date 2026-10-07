from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1 style='text-align:center;margin-top:50px;background:#0a0e1a;color:#00ff88;padding:50px'>CYBERLEARN-NG<br><br>🚀 LIVE!<br><br>Alhamdulillah!</h1>"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
