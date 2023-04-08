
tenBan1,chieuCaoBan1 = input('Nhập tên và chiều cao của ban thứ 1: ').split()
tenBan2,chieuCaoBan2 = input('Nhập tên và chiều cao của ban thứ 2: ').split()

chieuCaoBan1 = int(chieuCaoBan1)
chieuCaoBan2 = int(chieuCaoBan2)
import math
soSanhChieuCao = math.fabs(chieuCaoBan1 - chieuCaoBan2)

if chieuCaoBan1 > chieuCaoBan2:
    print('Bạn %s cao hơn bạn %s là %d mm' % (tenBan1,tenBan2,soSanhChieuCao)) 
elif chieuCaoBan1 < chieuCaoBan2:
    print('Bạn %s thấp bạn %s là %d mm' % (tenBan1,tenBan2,soSanhChieuCao)) 
else:
    print('Bạn %s bằng bạn %s' % (tenBan1,tenBan2)) 
