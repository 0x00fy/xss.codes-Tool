### xss.codes-Tool
https://xss.codes Http Header XSS Attacker

### What does this do?

Allows you to send XSS payloads to HTTP Header values (with Cloudflare Bypass)

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


### Mass : 

python mass.py -l sitelist.txt -u xss.codes userdomainname
