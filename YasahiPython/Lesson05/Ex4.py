city = ["Tokyo", "Nagoya", "Osaka", "Kyoto", "Fukuoka"]
print("city data is",city)

highestTemp = [32, 28, 27, 26, 27]
print("highest tempreture data is", highestTemp)

lowestTemp = [25, 21, 20, 19, 22]
print("lowest tempreture data is", lowestTemp)

for c, h, l in zip(city, highestTemp, lowestTemp):
    print(c, "'s highest tempreture is", h, "'s lowest tempreture is", l)
