from from flask import Flask, render_template_string

app = Flask(__name__)

LESSONS = {
 1: {"title":"1. Menene Phishing?",
     "maana":"Phishing wata dabara ce da yan damfara ke amfani da ita. Suna turo maka sako kamar daga banki ko Facebook suna cewa 'Danna wannan link'.",
     "yadda":"Suna turo link na karya. Idan ka danna, zai kai ka shafin da yayi kama da na gaskiya, sai su sace password dinka.",
     "cutarwa":"Za su sace kudin banki, su sace account dinka, su ci mutuncinka, su yi damfara da sunanka.",
     "amfani":"Idan ka san phishing, zaka gane sako na karya. Karka taba danna link daga mutumin da baka sani ba. Koyaushe duba link din da kyau."},
 2: {"title":"2. Menene Strong Password?",
     "maana":"Password mai karfi shine wanda yake da wahalar karyawa. Ba 12345 ba.",
     "yadda":"Ka hada Harafi babba, karami, lamba, da alama. Misali: Zaria@2026#Secure!",
     "cutarwa":"Idan password dinka rauni ne (kamar sunanka), hacker zai shiga account dinka cikin dakika 2.",
     "amfani":"Password mai karfi yana kare kudin ka, hotunanka, da sirrinka. Kada ka yi amfani da password daya a ko'ina."},
 3: {"title":"3. Menene Malware & Virus?",
     "maana":"Malware wata software ce marar kyau da ake sakawa a wayarka ko computer domin cutar da ita ko sace bayanai.",
     "yadda":"Yana shigowa ta hanyar downloading na karya, ko USB, ko link. Idan ya shiga zai boye a system.",
     "cutarwa":"Zai rage gudu na waya, ya sace hotuna, ya lalata files, ya sa waya tayi zafi.",
     "amfani":"Ka shigar da Antivirus, karka sauke app daga wajen Play Store, ka yi update a koda yaushe."},
 4: {"title":"4. Social Engineering",
     "maana":"Yaudara ce ta hankali. Ba wai sun karya computer ba, sun karya zuciyarka ne.",
     "yadda":"Mutum zai kira ka yace 'Ni daga banki ne, bani PIN dinka'. Ko yace 'Ka ci kyauta'.",
     "cutarwa":"Mutane suna rasa miliyoyi saboda wannan. Saboda sun yarda da magana mai dadi.",
     "amfani":"Banki BAYA tambayar PIN ko OTP a waya. Duk wanda ya tambaye ka, damfara ne. Ka kashe wayar."},
 5: {"title":"5. Public WiFi Hadari",
     "maana":"WiFi na kyauta a cafe, makaranta, hotel - yana da hadari sosai.",
     "yadda":"Hacker na iya zauna a kan WiFi daya da kai ya ga duk abinda kake yi - password, chat.",
     "cutarwa":"Za su iya sace Facebook, WhatsApp, da banki idan ka yi amfani da free WiFi ba tare da kariya ba.",
     "amfani":"Karka shiga banki da free WiFi. Yi amfani da Data dinka ko VPN. Kashe auto-connect na WiFi."}
}

HOME_HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CyberLearn-NG</title>
<style>
body{background:#050a14;color:white;font-family:Arial;margin:0;padding:0}
.header{background:#001122;padding:20px;text-align:center;border-bottom:2px solid #00ff88}
.header h1{color:#00ff88;margin:0}
.card{background:#101a2e;margin:15px;padding:20px;border-radius:12px;border-left:4px solid #00ff88}
.btn{background:#00ff88;color:black;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:10px}
.tag{background:#00ff8840;color:#00ff88;padding:4px 10px;border-radius:20px;font-size:12px}
</style>
</head>
<body>
<div class="header"><h1>CYBERLEARN-NG</h1><p>Platform na Koyon Cyber Security a Hausa</p></div>
<div style="padding:15px">
<h2>📚 Darussanmu ({{lessons|length}})</h2>
{% for id, l in lessons.items() %}
<div class="card">
<span class="tag">Darasi {{id}}</span>
<h3>{{l.title}}</h3>
<a class="btn" href="/lesson/{{id}}">Karanta Darasi →</a>
</div>
{% endfor %}
</div>
</body>
</html>
"""

LESSON_HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{l.title}}</title>
<style>
body{background:#050a14;color:white;font-family:Arial;margin:0;padding:15px;line-height:1.6}
.box{background:#101a2e;padding:20px;border-radius:12px;margin-bottom:15px;border:1px solid #222}
h1{color:#00ff88}
h3{color:#00ff88;margin-top:0}
a{color:#00ff88;text-decoration:none}
.back{background:#222;padding:10px 20px;border-radius:8px}
</style>
</head>
<body>
<a class="back" href="/">← Komawa</a>
<h1>{{l.title}}</h1>

<div class="box"><h3>📖 Ma'anarsa:</h3><p>{{l.maana}}</p></div>
<div class="box"><h3>⚙️ Yadda Ake Amfani Dashi / Yadda Yake Aiki:</h3><p>{{l.yadda}}</p></div>
<div class="box" style="border-left:4px solid red"><h3>☠️ Cutarwarsa / Hadarinsa:</h3><p>{{l.cutarwa}}</p></div>
<div class="box" style="border-left:4px solid #00ff88"><h3>✅ Amfaninsa / Yadda Zaka Kare Kanka:</h3><p>{{l.amfani}}</p></div>

<div style="text-align:center;margin:30px">
<a href="/lesson/{{next_id}}" style="background:#00ff88;color:black;padding:15px 30px;border-radius:10px;font-weight:bold">Darasi na gaba →</a>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML, lessons=LESSONS)

@app.route("/lesson/<int:id>")
def lesson(id):
    l = LESSONS.get(id)
    if not l: return redirect("/")
    next_id = id+1 if id < len(LESSONS) else 1
    return render_template_string(LESSON_HTML, l=l, next_id=next_id)

if __name__=="__main__":
    app.run()