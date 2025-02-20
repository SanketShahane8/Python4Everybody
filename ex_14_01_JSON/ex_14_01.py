import urllib.request, urllib.parse
import json, ssl

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2167975.json'

print('Retrieving: ', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')


try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))

comments = js['comments']
# print(json.dumps(comments, indent=4))

comment_count = 0
comment_count_sum = 0
for comment in comments:
    # print('Name:', comment['name'])
    # print('Count:', comment['count'])
    comment_count = comment_count + 1
    comment_count_sum = comment_count_sum + comment['count']

print('Count:', comment_count)
print('Sum:', comment_count_sum)