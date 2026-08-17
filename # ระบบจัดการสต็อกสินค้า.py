# ระบบจัดการสต็อกสินค้า
# สำหรับผู้เริ่มต้น Python

products = []


def show_products():
    print("\n===== รายการสินค้า =====")

    if len(products) == 0:
        print("ยังไม่มีสินค้า")
    else:
        for product in products:
            print(
                "รหัส:", product["code"],
                "| ชื่อ:", product["name"],
                "| ราคา:", product["price"],
                "บาท | จำนวน:", product["stock"]
            )


def add_product():
    print("\n===== เพิ่มสินค้า =====")

    code = input("รหัสสินค้า: ")
    name = input("ชื่อสินค้า: ")
    price = float(input("ราคาสินค้า: "))
    stock = int(input("จำนวนสินค้า: "))

    product = {
        "code": code,
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)

    print("เพิ่มสินค้าเรียบร้อยแล้ว")


def sell_product():
    print("\n===== ขายสินค้า =====")

    code = input("รหัสสินค้าที่ต้องการขาย: ")
    amount = int(input("จำนวนที่ขาย: "))

    for product in products:

        if product["code"] == code:

            if product["stock"] >= amount:
                product["stock"] -= amount

                total = product["price"] * amount

                print("ขายสินค้าเรียบร้อย")
                print("สินค้าที่ขาย:", product["name"])
                print("จำนวน:", amount)
                print("ราคาทั้งหมด:", total, "บาท")

            else:
                print("สินค้าในสต็อกไม่เพียงพอ")

            return

    print("ไม่พบรหัสสินค้านี้")


def add_stock():
    print("\n===== เพิ่มสินค้าเข้าสต็อก =====")

    code = input("รหัสสินค้าที่ต้องการเพิ่ม: ")
    amount = int(input("จำนวนที่เพิ่ม: "))

    for product in products:

        if product["code"] == code:
            product["stock"] += amount

            print("เพิ่มสินค้าเข้าสต็อกเรียบร้อย")
            print("จำนวนปัจจุบัน:", product["stock"])

            return

    print("ไม่พบรหัสสินค้านี้")


# =========================
# โปรแกรมหลัก
# =========================

while True:

    print("\n==========================")
    print("   ระบบจัดการสต็อกสินค้า")
    print("==========================")

    print("1. แสดงสินค้า")
    print("2. เพิ่มสินค้า")
    print("3. ขายสินค้า")
    print("4. เพิ่มสินค้าเข้าสต็อก")
    print("5. ออกจากโปรแกรม")

    choice = input("เลือกเมนู: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_product()

    elif choice == "3":
        sell_product()

    elif choice == "4":
        add_stock()

    elif choice == "5":
        print("จบการทำงาน")
        break

    else:
        print("กรุณาเลือกเมนู 1-5")
