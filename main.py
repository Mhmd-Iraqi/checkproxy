from flask import *
import requests,json,os
from urllib.parse import *
def dec(data):
	return requests.get(f"https://kurrofkkua.000webhostapp.com/dec.php?ata={quote(data)}&submit=submit").text.split(""" <title>Gmaer</title>""")[1].split("body>")[1].split("center>")[1]


def enc(data):
	return requests.get(f"https://kurrofkkua.000webhostapp.com/enc.php?ata={quote(data)}&submit=submit").text.split(""" <title>Gmaer</title>""")[1].split("<body>")[1].split("center>")[1]
	
fira = Flask(__name__)
@fira.route("/api/darkstorm/mhmd/check")
def star():
	idtar = request.args.get("target")
	data = '{"requested_with":"mehran.firazarin.android","version_code":"115","market_name":"cafebazaar","language_code":"ar","device_info":"320dpi; 720x1449; Redmi; M2006C3LG; dandelion_global; dandelion","sdk_info":"29\/10","android_id":"042b66ad34d63dae","app_signature":"61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81","user_pk":"'+str(idtar)+'","user_picture":"https:\/\/instagram.febl9-1.fna.fbcdn.net\/v\/t51.2885-19\/292087357_3143992945818603_61804610724414833_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.febl9-1.fna.fbcdn.net&_nc_cat=103&_nc_ohc=i8ervsw7MAsAX8AsZNk&edm=AJlpnE4BAAAA&ccb=7-5&oh=00_AT8FRBJ8ZFPeifjL2la0aSk4RXTPRCzlAPzaQAS8iwmvnA&oe=62FF9FF5&_nc_sid=312772","sec_1":"+9647800430720","sec_2":"","username":"mhmdtool","full_name":"mohammed","login":""}'
	data =enc(data)

	headers ={"Host": "firafollower.xyz",
"user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LG MIUI/V12.0.20.0.QCDMIXM)",
"accept": "*/*",
"accept-encoding": "gzip, deflate",
"content-type": "text/xml",
"x-access": "FiraFollower",
"x-version": "2",
"content-length": "693"}
	stat =dec(requests.post("https://firafollower.xyz/api/v4/account.php",headers =headers,data =data).text)
	token = json.loads(stat)
	if 'checkpoint_required.' in stat or 'account blocked.' in stat:
		return {"status": "Id Blocked" , "by": "@J_W_2"}
		
	else:
		user_token =token["data"]['user_token']
		
		data ='{"requested_with":"mehran.firazarin.android","version_code":"115","market_name":"cafebazaar","language_code":"ar","device_info":"320dpi; 720x1449; Redmi; M2006C3LG; dandelion_global; dandelion","sdk_info":"29\/10","android_id":"042b66ad34d63dae","app_signature":"61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81","user_token":"b6f06628ab3493b5d5b3fc7a2eefa2fa","user_pk":"'+str(idtar)+'","user_picture":"https:\/\/instagram.fisu4-2.fna.fbcdn.net\/v\/t51.2885-19\/292087357_3143992945818603_61804610724414833_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fisu4-2.fna.fbcdn.net&_nc_cat=103&_nc_ohc=i8ervsw7MAsAX8uvaQW&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AT_8iJ5vd-XPEjjo6SbKXD0TFKpIqGut8DiqndOjDQWNag&oe=62FF9FF5&_nc_sid=a9513d","username":"mhmdtool","full_name":"mohammed","user_token": "'+str(user_token)+'"}'
		data = enc(data)
		m = requests.post("https://firafollower.xyz/api/v4/account.php",headers =headers,data =data).text
		po =json.loads(dec(m))
		follow_coin = po["data"]["follow_coin"]
		general_coin =po["data"]["like_comment_coin"]
		return {"status": "Success" , "data": {"Follow_Coin": str(follow_coin) , "General_Coin": str(general_coin) , "By": "@J_W_2"}}
@fira.route("/api/darkstorm/mhmd/get")
def getk():
	g =0
	s =0
	idtar = request.args.get("target")
	myid = request.args.get("id")
	data = '{"requested_with":"mehran.firazarin.android","version_code":"115","market_name":"cafebazaar","language_code":"ar","device_info":"320dpi; 720x1449; Redmi; M2006C3LG; dandelion_global; dandelion","sdk_info":"29\/10","android_id":"042b66ad34d63dae","app_signature":"61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81","user_pk":"'+str(idtar)+'","user_picture":"https:\/\/instagram.febl9-1.fna.fbcdn.net\/v\/t51.2885-19\/292087357_3143992945818603_61804610724414833_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.febl9-1.fna.fbcdn.net&_nc_cat=103&_nc_ohc=i8ervsw7MAsAX8AsZNk&edm=AJlpnE4BAAAA&ccb=7-5&oh=00_AT8FRBJ8ZFPeifjL2la0aSk4RXTPRCzlAPzaQAS8iwmvnA&oe=62FF9FF5&_nc_sid=312772","sec_1":"+9647800430720","sec_2":"","username":"mhmdtool","full_name":"mohammed","login":""}'
	data =enc(data)

	headers ={"Host": "firafollower.xyz",
"user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LG MIUI/V12.0.20.0.QCDMIXM)",
"accept": "*/*",
"accept-encoding": "gzip, deflate",
"content-type": "text/xml",
"x-access": "FiraFollower",
"x-version": "2",
"content-length": "693"}
	stat =dec(requests.post("https://firafollower.xyz/api/v4/account.php",headers =headers,data =data).text)
	token = json.loads(stat)
	if 'checkpoint_required.' in stat or "account blocked." in stat:
		return {"status": "Id Blocked"}
	else:
		user_token =token["data"]['user_token']
		
		data ='{"requested_with":"mehran.firazarin.android","version_code":"115","market_name":"cafebazaar","language_code":"ar","device_info":"320dpi; 720x1449; Redmi; M2006C3LG; dandelion_global; dandelion","sdk_info":"29\/10","android_id":"042b66ad34d63dae","app_signature":"61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81","user_token":"b6f06628ab3493b5d5b3fc7a2eefa2fa","user_pk":"'+str(idtar)+'","user_picture":"https:\/\/instagram.fisu4-2.fna.fbcdn.net\/v\/t51.2885-19\/292087357_3143992945818603_61804610724414833_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fisu4-2.fna.fbcdn.net&_nc_cat=103&_nc_ohc=i8ervsw7MAsAX8uvaQW&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AT_8iJ5vd-XPEjjo6SbKXD0TFKpIqGut8DiqndOjDQWNag&oe=62FF9FF5&_nc_sid=a9513d","username":"mhmdtool","full_name":"mohammed","user_token": "'+str(user_token)+'"}'
		data = enc(data)
		m = requests.post("https://firafollower.xyz/api/v4/account.php",headers =headers,data =data).text
		po =json.loads(dec(m))
		follow_coin = po["data"]["follow_coin"]
		general_coin =po["data"]["like_comment_coin"]
		if follow_coin >=100:
			data = '{"requested_with":"mehran.firazarin.android","version_code":"115","market_name":"cafebazaar","language_code":"ar","device_info":"320dpi; 720x1449; Redmi; M2006C3LG; dandelion_global; dandelion","sdk_info":"29\/10","android_id":"042b66ad34d63dae","app_signature":"61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81","user_token":"'+str(user_token)+'","user_pk":"'+str(idtar)+'","to_user":"'+str(myid)+'","coin":"'+str(follow_coin)+'","action":"follow","has_post":"false"}'
			data = enc(data)
			mk = data
			s+=1
		if general_coin >=100:
			data = '{"requested_with":"mehran.firazarin.android","version_code":"115","market_name":"cafebazaar","language_code":"ar","device_info":"320dpi; 720x1449; Redmi; M2006C3LG; dandelion_global; dandelion","sdk_info":"29\/10","android_id":"042b66ad34d63dae","app_signature":"61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81","user_token":"'+str(user_token)+'","user_pk":"'+str(idtar)+'","to_user":"'+str(myid)+'","coin":"'+str(general_coin)+'","action":"like_comment","has_post":"false"}'
			data = enc(data)
			g +=1
			mj = data
		return {"Follow_Coin": follow_coin , "General_Coin": general_coin , "by": "@J_W_2"}
fira.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
		
