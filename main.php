from flask import *
import requests,os
app = Flask(__name__)
@app.route("/check/proxy/checkproxy/dark.php")
def k():
	proxy = request.args.get("proxy")
	data = f"data={proxy}"
	return requests.post("https://hidemy.name/api/checker.php?out=js&action=list_new&tasks=http,ssl,socks4,socks5&parser=lines",data=data).json()
if __name__=="__main__":	
	app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
