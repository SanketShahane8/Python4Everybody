text = "X-DSPAM-Confidence:    0.8475"
find_letter =  text.find('0')
print(float(text[find_letter:]))