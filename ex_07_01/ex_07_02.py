add_value = None
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    value = line[20:]
    # print(float(value))
    if add_value is None:
        add_value = float(value)
    else:
        add_value = add_value + float(value)
    count = count + 1

print("Average spam confidence:", str(add_value/count))
# print(line)
print("--- Done ---")
