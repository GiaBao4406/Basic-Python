# nhập 2 số từ bàn phím
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# tính toán
tong = a + b
hieu = a - b
tich = a * b


# in kết quả
print(f"Tổng: {tong:.2f}")
print(f"Hiệu: {hieu:.2f}")
print(f"Tích: {tich:.2f}")
if b != 0:
    print("Thương: {0:.2f}".format(a/b))
else:
    thuong = "Không xác định (chia cho 0)"
