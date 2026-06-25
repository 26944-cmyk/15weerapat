print("คำนวณความเร็วรถ ด้วยกฎจราจรทางบก \n")
vehice_speed = int(input("ความเร็วของรถคือเท่าใด :"))

if vehice_speed >= 0 and vehice_speed <= 80:
    print("สถานะความปลอดภัยของท่านอยุ่ในระดับ")
    print ("ปลอดภัยค่ะ")
elif vehice_speed < 0 :
    print ("ขออภัย ความเร็วของยานพาหนะท่านไม่สามารถติดลบได้ค่ะ")
elif vehice_speed >= 81 and vehice_speed <= 100 :
    print("สถานะความปลอดภัยของท่านอยุ่ในระดับ")
    print ("อยู่ในช่วงสุ่มเสี่ยงและเตือนค่ะ")
elif vehice_speed  >= 101 and vehice_speed < 120 :
    print("สถานะความปลอดภัยของท่านอยุ่ในระดับ")
    print("เสี่ยงถูกปรับค่ะ")
else:
    print("สถานะความปลอดภัยของท่านอยุ่ในระดับ")
    print("ผิดกฎหมายค่ะ")