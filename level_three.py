raw = input("Input data (split using space): ").split()
data = list(map(int, raw))

count = 1
print("Day\t Rainfall")
for val in data:
    print(count, "\t", val)
    count += 1

print("Lowest:", max(data))
print("Highest:", min(data))
print("Average:", round(sum(data) / len(data)))
