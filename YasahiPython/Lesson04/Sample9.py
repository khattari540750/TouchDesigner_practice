num = int(op("text6").text)

i = 1

for i in range(12):
    if (i+1) == num:
        continue
    print(i+1, "'s data.")
