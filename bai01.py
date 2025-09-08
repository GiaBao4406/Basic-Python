# Một người cần rút một số tiền T từ ngân hàng và muốn tổng số tờ ít nhất. 
# Cho biết có các loại tiền mệnh giá 100, 20, 5 và 1. 
# Nhập từ bàn phím số tiền T và in ra số tờ mỗi loại mệnh giá và tổng số tờ nhận được.


soTienCanRut = int(input("Nhập số tiền muốn rút: "))

    # số tờ tiền 100
soToMotTram = int (soTienCanRut / 100)
soTienCanRut = soTienCanRut - soToMotTram * 100
    # số tờ tiền 20
soToHaiMuoi = int (soTienCanRut / 20)
soTienCanRut = soTienCanRut - soToHaiMuoi * 20
    # số tờ tiền 5
soToNam = int (soTienCanRut / 5)
soTienCanRut = soTienCanRut - soToNam * 5
# số tờ tiền 1
soToMot = int (soTienCanRut / 1)
soTienCanRut = soTienCanRut - soToMot

tongSoTo = soToMotTram + soToHaiMuoi + soToNam + soToMot
print(f"Tong co {tongSoTo} to tien")
print(f"Có {soToMotTram} số tờ 100, Có {soToHaiMuoi} số tờ 20, Có {soToNam} số tờ 5, Có {soToMot} số tờ 1")