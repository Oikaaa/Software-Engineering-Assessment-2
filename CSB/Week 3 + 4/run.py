from bank import TaiKhoan
from bank import TaiKhoanTietKiem

stk = input("So tai khoan: ")
ten = input("Ho va ten: ")
so_du = float(int(input("So du trong tai khoan: ")))

taiKhoan = TaiKhoan(stk, ten, so_du)

withdrawal = float(input("So tien rut: "))
taiKhoan.rut_tien(withdrawal)
print(f"So du con lai: {taiKhoan.lay_so_du()}")

deposit = float(input("So tien nap: "))
taiKhoan.nap_tien(deposit)
print(f"So du con lai: {taiKhoan.lay_so_du()}")

taiKhoanTietKiem = TaiKhoanTietKiem(taiKhoan.stk, taiKhoan.ten, taiKhoan.so_du)

print(f"Lai suat: {taiKhoanTietKiem.lai_suat()}")
print(f"So du theo lai suat hien tai: {taiKhoanTietKiem.lai_suat + taiKhoanTietKiem.so_du}")