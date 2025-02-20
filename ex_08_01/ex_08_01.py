fname = input("Enter file name: ")
fh = open(fname)
lst = list()
final_lst = list()
for line in fh:
    line = line.rstrip()
    lst = line.split()
    # print(lst)
    for word in lst:
        if word not in final_lst:
            final_lst.append(word)

final_lst.sort()
print(final_lst)
# print(line.rstrip())