import urllib.request
import xml.etree.ElementTree as ET

# url = input('Enter location: ')
# if len(url) < 1 : 
#     url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

url = 'http://py4e-data.dr-chuck.net/comments_2167974.xml'

fname = input("Enter file name: ")
if len(fname) > 1:
    fh = open(fname)
    
print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read()
data = fh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    # print(result.text)
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

