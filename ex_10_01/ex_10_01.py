name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict_hrs = dict()
for line in handle :
    line = line.rstrip()
    if line.startswith("From ") :
        time = line.split()[5]
        hour = time.split(":")[0]
        # print(lst)
        dict_hrs[hour] = dict_hrs.get(hour,0) + 1

# print(dict_hrs)

# lst = list()
# for k,v in dict_hrs.items() :
#     lst.append((k, v))

# # print(lst)

# lst = sorted(lst)

# # print(lst)

# for item in lst :
#     print(item[0], item[1])

for hour, count in sorted(dict_hrs.items()) :
    print(hour, count)