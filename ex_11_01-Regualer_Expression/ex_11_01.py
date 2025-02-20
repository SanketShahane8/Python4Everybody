import re
file_name = "regex_sum_2167970.txt"

handle = open(file_name)

sum = 0
for line in handle:
    line = line.rstrip()
    # print(line)
    num_lst = re.findall('[0-9]+', line)
    if len(num_lst) > 0 :
        # print(num_lst)
        for num in num_lst :
            sum = sum + int(num)

print("sample file sum: ", str(sum))
