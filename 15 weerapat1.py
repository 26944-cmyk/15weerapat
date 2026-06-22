print("โปรแกรมคำนวณคะแนนค่าเฉลี่ยและคะแนนรวม\n")

score1 = int(input("ใส่คะแนนวิชา1 :"))
score2 = int(input("ใส่คะแนนวิชา2 :"))
score3 = int(input("ใส่คะแนนวิชา3 :"))

Total_score = score1 + score2 + score3
Average_score = Total_score / 3

if Average_score <= 60:
    print("\nคุณอยู่ในระดับ ควรปรับปรุง")
elif Average_score <= 80:
    print("\nขอแสดงความยินดีคุณอยู่ในระดับ ผ่าน")
else:
    print("\nแสดงความยินดีด้วยคุณอยู่ในระดับ ดีเยี่ยม")    
    


print("คะแนนรวมของทั้งสามวิชา คือ " + str(Total_score))
print("คะแนนเฉลี่ยของทั้งสามวิชา คือ " + str(Average_score))
