data = [
    ["Tokyo", 32, 25],
    ["Nagoya", 28, 21],
    ["Osaka", 27, 20],
    ["Kyoto", 26, 19],
    ["Fukuoka", 27, 22]
]

print("now data is", data, ".")

for dat in data:
    print("city data is", dat)
    for d in dat:
        print(d, end="\t")
    print()

print(data[0][0], "'s highest temperature is", data[0][1], "lowest temperature is", data[0][2])