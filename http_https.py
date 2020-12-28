import requests

r = requests.get('https://***')
print(r.url)




file1 = open('modif.txt','r')
file2 = open('http.txt','a')
file3 = open('https.txt','a')
Lines = file1.readlines()

https_domain = "https://"

#http check
for line in Lines:
    http_domain = "http://"
    http_domain = http_domain + line + '/'
    http = requests.get(http_domain)
    file2.write(http.url)

#https check
for line in Lines:
    https_domain = "https://"
    https_domain = https_domain + line + '/'
    https = requests.get(https_domain)
    file3.write(https.url)

file1.close()
file2.close()
file3.close()


