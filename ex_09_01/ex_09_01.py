fname = input("Enter file name: ")
fh = open(fname)
email_dict = dict()
multiple_email_sender = None
email_count = None
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        email_dict[words[1]] = email_dict.get(words[1],0) + 1

for k,v in email_dict.items():
    # print(k,v)
    if email_count is None or v > email_count:
        email_count = v
        multiple_email_sender = k

print(multiple_email_sender,email_count)