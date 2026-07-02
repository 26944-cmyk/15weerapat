import random

n = int(input("ใส่ตัวเลขที่เดา :"))
x = random.randint(1, 100)
i = 0

while n < x:
    print("ยังน้อยไป\n")
    n = int(input("ใส่ตัวเลขที่เดา :"))
    i += 1
    while n > x:
        print("ยังมากไป\n")
        n = int(input("ใส่ตัวเลขที่เดา :"))
        i += 1
    while n == x:
        print ("ถูกต้องแล้วจร้า\n")
        print("ทายไปทั้งหมด " + str(i) + (" ครั้ง"))

        break
  