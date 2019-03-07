sale = int(op("text3").text)
num = int(op("text4").text)

if sale >= 100 and num >= 30 :
    print("sales is so good")
elif sale >= 100:
    print("sales is good")
elif sale >= 50:
    print("sales is so-so")
else:
    print("sales is not good")

print("processing is terminated.")