print("\n สู ต ร คู ณ ห ร ร ษ า พ า เ พ ลิ น (ได้หลายสูตร)😘😘\n")

n1 = int(input("ใส่ตัวเลขตัวแรก :"))
n2 = int(input("ใส่ตัวเลขตัวที่สอง :"))

for i in range(n1, n2 + 1):
    print(f"\n--- สูตรคูณแม่ {i} ---")
    
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}")
        

print("\nBy Weerapat Wisetsup 4/4 No.15😁❤️\n")