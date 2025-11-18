# Ask user for height between 1 and 8
while True:
    try:
        h = int(input("Height: "))
        if 1 <= h <= 8:
            break
    except ValueError:
        continue

# Print double (full) pyramid
for i in range(1, h + 1):
    left = " " * (h - i) + "#" * i
    right = "#" * i
    print(left + "  " + right)
