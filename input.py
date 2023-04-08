#Tính tổng hai số nguyên bất kỳ (Có xử lý ngoại lệ đầu vào).
so1 = input("Nhap so thu 1: ") 
so2 = input("Nhap so thu 2: ") 
try:       
    so1 = int(so1)
    so2 = int(so2)

    tong = so1 + so2 
    print("Tong hai so la: ", tong)
except:
    print("So nhap vao khong hop le")