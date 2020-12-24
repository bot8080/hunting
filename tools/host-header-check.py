import requests
import tldextract
import time


url = 'https://jniwebshop.com/category/89/store'

head_list = ['','Host', 'X-Host','X-HTTP-Host-Override','X-Original-Url','X-Forwarded-Server','X-Host','X-Forwarded-**Host**','X-Forwarded-Host', 'X-Rewrite-Url','Forwarded','Referer']
host = ""

hostobj = tldextract.extract(url)
if hostobj.subdomain == "":
    host = hostobj.domain+"."+hostobj.suffix
else:
    host = hostobj.subdomain+"."+hostobj.domain+"."+hostobj.suffix

def print_roundtrip(response, *args, **kwargs):
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    print('\n')
    print(head)
    print(response)
    # print("---------------Request---------------")
    # print(response.request.method,response.request.url)
    # print('{}'.format(format_headers(response.request.headers)))

    # print("---------------Response---------------")
    # print('{}'.format(format_headers(response.headers)))

    if 'evil' in res.text:
        log = open("host-headers.txt", "a")
        print('{}\n\n'.format(format_headers(response.request.headers)), file = log)


for head in head_list:

    if head == '':
        hdr = {
            'Host': 'evil.com',
            'X-Forwarded-Host' : host,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5'
        }
    else:
        hdr = {
            'Host': host,
             head : 'evil.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    try:
        res = requests.get(url, headers=hdr)
        time.sleep(1)

        print_roundtrip(res, head)


    except Exception as ee:
        print("################################## ", ee)
