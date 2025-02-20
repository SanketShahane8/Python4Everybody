import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')

address = address.strip()
parms = dict()
parms['q'] = address

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))

plus_code =  js['features'][0]['properties']['plus_code']
print('Plus code', plus_code)