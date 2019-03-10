city = ["Tokyo", "Nagoya", "Osaka", "Kyoto"]
sale = [80,60,22,50,75]

print("city name is", city, ".")
print("sales data is", sale, ".")

print("data zips.")

for d in zip(city, sale):
    print(d)

print("zip data and index.")

for d in enumerate(city):
    print(d)