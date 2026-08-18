import tkinter as tk
from tkinter import messagebox

# =========================
# ข้อมูลสินค้า
# =========================

products = []


# =========================
# แสดงสินค้า
# =========================

def show_products():

    # ล้างข้อมูลในตารางก่อน
    for item in product_list.get_children():
        product_list.delete(item)

    if len(products) == 0:
        messagebox.showinfo("รายการสินค้า", "ยังไม่มีสินค้า")

    else:
        for product in products:
            product_list.insert(
                "",
                "end",
                values=(
                    product["code"],
                    product["name"],
                    product["price"],
                    product["stock"]
                )
            )


# =========================
# เพิ่มสินค้า
# =========================

def add_product():

    code = code_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()

    if code == "" or name == "" or price == "" or stock == "":
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณากรอกข้อมูลให้ครบ"
        )
        return

    try:
        price = float(price)
        stock = int(stock)

    except:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณากรอกราคาและจำนวนเป็นตัวเลข"
        )
        return

    product = {
        "code": code,
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)

    messagebox.showinfo(
        "สำเร็จ",
        "เพิ่มสินค้าเรียบร้อยแล้ว"
    )

    clear_input()
    show_products()


# =========================
# ขายสินค้า
# =========================

def sell_product():

    code = code_entry.get()
    amount = amount_entry.get()

    if code == "" or amount == "":
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณากรอกรหัสสินค้าและจำนวน"
        )
        return

    try:
        amount = int(amount)

    except:
        messagebox.showwarning(
            "แจ้งเตือน",
            "จำนวนต้องเป็นตัวเลข"
        )
        return

    for product in products:

        if product["code"] == code:

            if product["stock"] >= amount:

                product["stock"] -= amount

                total = product["price"] * amount

                messagebox.showinfo(
                    "ขายสินค้า",
                    "สินค้าที่ขาย: " + product["name"] +
                    "\nจำนวน: " + str(amount) +
                    "\nราคาทั้งหมด: " + str(total) + " บาท"
                )

                clear_input()
                show_products()

            else:
                messagebox.showwarning(
                    "แจ้งเตือน",
                    "สินค้าในสต็อกไม่เพียงพอ"
                )

            return

    messagebox.showwarning(
        "แจ้งเตือน",
        "ไม่พบรหัสสินค้านี้"
    )


# =========================
# เพิ่มสินค้าเข้าสต็อก
# =========================

def add_stock():

    code = code_entry.get()
    amount = amount_entry.get()

    if code == "" or amount == "":
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณากรอกรหัสสินค้าและจำนวน"
        )
        return

    try:
        amount = int(amount)

    except:
        messagebox.showwarning(
            "แจ้งเตือน",
            "จำนวนต้องเป็นตัวเลข"
        )
        return

    for product in products:

        if product["code"] == code:

            product["stock"] += amount

            messagebox.showinfo(
                "สำเร็จ",
                "เพิ่มสินค้าเข้าสต็อกเรียบร้อยแล้ว"
            )

            clear_input()
            show_products()

            return

    messagebox.showwarning(
        "แจ้งเตือน",
        "ไม่พบรหัสสินค้านี้"
    )


# =========================
# ล้างช่องกรอก
# =========================

def clear_input():

    code_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


# =========================
# สร้างหน้าต่าง
# =========================

root = tk.Tk()

root.title("ระบบจัดการสต็อกสินค้า")

root.geometry("850x600")

root.configure(
    bg="#FAF9FC"
)


# =========================
# สี
# =========================

WHITE = "#FFFFFF"

PURPLE = "#DCC8EA"

LIGHT_PURPLE = "#F1EAF6"

DARK_PURPLE = "#73538C"

PINK = "#F5DFE9"

TEXT = "#4A4050"


# =========================
# หัวโปรแกรม
# =========================

title = tk.Label(
    root,
    text="ระบบจัดการสต็อกสินค้า",
    font=("Tahoma", 22, "bold"),
    bg=WHITE,
    fg=DARK_PURPLE,
    pady=15
)

title.pack(
    fill="x"
)


# =========================
# ช่องกรอกข้อมูล
# =========================

input_frame = tk.Frame(
    root,
    bg=LIGHT_PURPLE,
    padx=20,
    pady=15
)

input_frame.pack(
    fill="x",
    padx=20,
    pady=15
)


# รหัสสินค้า

tk.Label(
    input_frame,
    text="รหัสสินค้า",
    bg=LIGHT_PURPLE,
    fg=TEXT,
    font=("Tahoma", 10)
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

code_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Tahoma", 10)
)

code_entry.grid(
    row=0,
    column=1,
    padx=5
)


# ชื่อสินค้า

tk.Label(
    input_frame,
    text="ชื่อสินค้า",
    bg=LIGHT_PURPLE,
    fg=TEXT,
    font=("Tahoma", 10)
).grid(
    row=0,
    column=2,
    padx=5
)

name_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Tahoma", 10)
)

name_entry.grid(
    row=0,
    column=3,
    padx=5
)


# ราคา

tk.Label(
    input_frame,
    text="ราคา",
    bg=LIGHT_PURPLE,
    fg=TEXT,
    font=("Tahoma", 10)
).grid(
    row=1,
    column=0,
    padx=5,
    pady=10
)

price_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Tahoma", 10)
)

price_entry.grid(
    row=1,
    column=1,
    padx=5
)


# จำนวนสินค้า

tk.Label(
    input_frame,
    text="จำนวนสินค้า",
    bg=LIGHT_PURPLE,
    fg=TEXT,
    font=("Tahoma", 10)
).grid(
    row=1,
    column=2,
    padx=5
)

stock_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Tahoma", 10)
)

stock_entry.grid(
    row=1,
    column=3,
    padx=5
)


# จำนวนขาย / เพิ่ม

tk.Label(
    input_frame,
    text="จำนวนขาย / เพิ่ม",
    bg=LIGHT_PURPLE,
    fg=TEXT,
    font=("Tahoma", 10)
).grid(
    row=2,
    column=0,
    padx=5
)

amount_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Tahoma", 10)
)

amount_entry.grid(
    row=2,
    column=1,
    padx=5
)


# =========================
# ปุ่ม
# =========================

button_frame = tk.Frame(
    root,
    bg="#FAF9FC"
)

button_frame.pack(
    pady=5
)


tk.Button(
    button_frame,
    text="เพิ่มสินค้า",
    command=add_product,
    bg=PURPLE,
    fg=TEXT,
    font=("Tahoma", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat"
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    button_frame,
    text="ขายสินค้า",
    command=sell_product,
    bg=PURPLE,
    fg=TEXT,
    font=("Tahoma", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat"
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    button_frame,
    text="เพิ่มเข้าสต็อก",
    command=add_stock,
    bg=PURPLE,
    fg=TEXT,
    font=("Tahoma", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat"
).grid(
    row=0,
    column=2,
    padx=5
)


tk.Button(
    button_frame,
    text="แสดงสินค้า",
    command=show_products,
    bg=PINK,
    fg=TEXT,
    font=("Tahoma", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat"
).grid(
    row=0,
    column=3,
    padx=5
)


tk.Button(
    button_frame,
    text="ล้างข้อมูล",
    command=clear_input,
    bg=WHITE,
    fg=TEXT,
    font=("Tahoma", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat"
).grid(
    row=0,
    column=4,
    padx=5
)


# =========================
# ตารางสินค้า
# =========================

import tkinter.ttk as ttk

table_frame = tk.Frame(
    root,
    bg=WHITE
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)


product_list = ttk.Treeview(
    table_frame,
    columns=(
        "code",
        "name",
        "price",
        "stock"
    ),
    show="headings"
)


product_list.heading(
    "code",
    text="รหัสสินค้า"
)

product_list.heading(
    "name",
    text="ชื่อสินค้า"
)

product_list.heading(
    "price",
    text="ราคา"
)

product_list.heading(
    "stock",
    text="จำนวน"
)


product_list.column(
    "code",
    width=150,
    anchor="center"
)

product_list.column(
    "name",
    width=300,
    anchor="center"
)

product_list.column(
    "price",
    width=150,
    anchor="center"
)

product_list.column(
    "stock",
    width=150,
    anchor="center"
)


product_list.pack(
    fill="both",
    expand=True
)


# =========================
# เริ่มโปรแกรม
# =========================

root.mainloop()