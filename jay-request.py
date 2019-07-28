import os
import sys

##########
def printcx(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36,'p':37}
        for i in w:
                x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
        x+='\033[0m'
        x=x.replace('\r0','\033[0m')
        print(x)

def runing():
        os.system('clear')
        os.system('sleep 2')
        os.system('pkg update && pkg upgrade')
        os.system('pip2 install --upgrade pip')
        os.system('pip2 install requests && pip2 install mechanize')
        os.system('pkg install cowsay')
        os.system('pkg install toilet && pkg install figlet')
        os.system('pkg install ruby && gem install lolcat')
        os.system('clear')
        os.system('sleep 2')
        os.system('figlet -f slant "SUCCESS" | lolcat')
        printcx ('\rh   ALL TOOLS INSTALED')
        os.system('sleep 2')
        os.system('clear')
        os.system('sleep 2')
        os.system('figlet -f slant "WELCOME" | lolcat')
        os.system('figlet -f slant "  TO " | lolcat')
        os.system('figlet -f slant "DARK-LINK" | lolcat')
        os.system('figlet -f slant "PROJECT" | lolcat')
        os.system('sleep 2')
        os.system('clear')
	command()

def command():
	os.system('git clone https://github.com/D4rk-L1nk/Dark-Link.fbtools.git')
        os.system('cd Dark-Link.fbtools')
        os.system('ls')
os.system('cd Dark-Link.fbtools')
        os.system('python2 fbtools.py')

def load():
	print (' ')
        printcx ('''\rh    before you run this program,
  first check and install all the supporting tools
              of this program.''')
	try:
        	printcx ('''\rm Press \rp'\rhy\rp'/'\rhY\rp' \rmif you agree
\rm or press \rp'\rhn\rp'/'\rhN\rp'\rm if you disagree''')
		y = raw_input('y/N? ')
                if y == 'y' or y == 'Y':
                	os.system('clear')
			os.system('sleep 2')
                        runing()
                elif y == 'n' or y == 'N':
                        os.system('clear')
                        exit()
		else:
                        printcx ('\rm[!] Input not found')
                        load()
	except KeyboardInterrupt:
                printcx ('[*] CTRL+C detected')
                printcx ('\rm[!] UserInterrupt not supportrd')
                load()
        except (NameError, SyntaxError):
		printcx ('[!] Input not found')

load()
