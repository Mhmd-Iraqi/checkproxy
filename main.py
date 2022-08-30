import requests,random
import re,json
from pywebio import *
from urllib.parse import quote
from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
from pywebio.pin import *
from pywebio.session import *
import requests
@config(theme="dark")
def MyApp():
	popup(
	'اهلا بك عزيزي المستخدم في موقع استخراج سيشن',
	put_text("فقط حط اليوزر و الباس"))
	data = input_group(
	'ادخل اليوزر + الباسورد',
	[
	input("Username",name="username",type="text"),
	input("Password",name="password",type="password"),
	]
	)
	username = data["username"]
	password = data["password"]
	popup('Please Wait',put_image("https://images.app.goo.gl/gZdtCVGkKXriHoV5A"))
	header = {"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}
	with requests.Session() as max:
			url_scrap = "https://www.instagram.com/"
			data = max.get(url_scrap, headers=header).content
			token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]

	headers = {
	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	    "Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
		"Host": "www.instagram.com",
		"X-CSRFToken": token,
		"X-Requested-With": "XMLHttpRequest",
		"Referer": "https://www.instagram.com/accounts/login/",
		"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",}
	data = {
		"username": str(username),
		"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), str(password)),
		"optIntoOneTap": False,
		"queryParams": {},
		"stopDeletionNonce": "",
		"trustedDeviceRecords": {}}
		
		
	with requests.Session() as r:
		url = "https://www.instagram.com/accounts/login/ajax/"
		response = r.post(url, data=data, headers=headers)
		login = json.loads(response.content)
		#print (login)
		
		if ("userId") in str(login):
			
			id = str(login['userId'])
			sessionid = str(r.cookies['sessionid'])
			popup("تم تسجيل الدخول بنجاح",
			put_text(f"""
Username : {username}
Password : {password}
Sessionid : {sessionid}
UserId : {id}"""))
			
		elif ("checkpoint_url") in str(login):
			popup(
			"حسابك مضروب سكيور",
			put_text(f"""
Username : {username}
Password : {password}"""))
		elif ("Please wait") in str(login):
			popup(
			"الايبي الخاص بيك محضور ارجع بعد 30 دقيقه",
			put_text(f"""
Username : {username}
Password : {password}"""))
		else:
			popup(
			"اليوزر او الباسورد خطأ",
			put_text(f"""
Username : {username}
Password : {password}"""))
start_server(MyApp,port=81)
