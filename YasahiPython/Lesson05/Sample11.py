data = [1,2,3,4,5]
print("now data is", data, ".")

print("use for sentence data[::-1]")
for d in data[::-1]:
    print(d)
print("data[::-1] is",data[::-1], ".")
print("now data is", data)

print("use for sentence reversed(data)")
for d in reversed(data):
    print(d)
print("reversed(data) is", reversed(data), ".")
print("now data is", data)

print("processing data.reverse()")
data.reverse()
print("now data is", data)