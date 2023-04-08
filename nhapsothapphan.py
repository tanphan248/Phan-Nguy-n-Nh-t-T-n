#Làm tròn số thập phân A đến B chữ số sau dấu phẩy (Có xử lý ngoại lệ đầu vào).
giaTriA = input("Nhap so thap phan: ") 
giaTriB = input("Nhap so ki tu rut gon: ") 
isParseDone = False
try: 
    soA = float(giaTriA) 
    soB = int(giaTriB) 
    isParseDone = True
except: 
    print("Dinh dang dau vao khong hop le!") 

if isParseDone:
    print('{0:.{1}f}'.format(soA, soB))