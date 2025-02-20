# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_2167972.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all Span tag and get the numbers from it and sum them
span_tags = soup('span')
sum = None
for span in span_tags:
    # print(span)
    print(int(span.contents[0]))
    if sum is None:
        sum = int(span.contents[0])
        continue
    sum = sum + int(span.contents[0])

print(str(sum))