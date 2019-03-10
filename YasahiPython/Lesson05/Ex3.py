data = [74, 85, 69, 77, 81]
print("test score is", data)

print("more than 80 socre is", [n for n in data if n>80])
print("more than 80 socore num is", len([n for n in data if n>80]))