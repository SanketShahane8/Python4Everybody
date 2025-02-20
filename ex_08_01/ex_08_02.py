fname = input("Enter file name: ")
if len(fname) > 1:
    fh = open(fname)
    lst = list()
    email_lst = list()
    for line in fh:
        line = line.rstrip()
        if not line.startswith("From:"):
            continue
        # print(line)
        lst = line.split()
        # print(lst)
        email = lst[1]
        print(email)
        email_lst.append(email)
    # print(email_lst)
    print("There were", len(email_lst), "lines in the file with From as the first word")