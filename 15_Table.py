# พิมพ์หัวตาราง
print(" ", end="\t")
for col in range(1, 13):
    print(col, end="\t")
print()

# วนแถว
for row in range(1, 13):
    print(row, end="\t")

    # วนคอลัมน์
    for col in range(1, 13):
        print(row * col, end="\t")

    print()