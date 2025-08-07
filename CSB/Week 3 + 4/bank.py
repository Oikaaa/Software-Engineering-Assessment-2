class TaiKhoan:
    def __init__(self, stk, ten, so_du):
        self.stk = stk
        self.ten = ten
        self.so_du = so_du

    def rut_tien(self, so_tien):
        if self.so_du > so_tien:
            self.so_du = self.so_du - so_tien
        else:
            print("Ban khong du tien de thuc hien rut")

    def nap_tien(self, so_tien):
        self.so_du = self.so_du + so_tien

    def lay_so_du(self):
        return self.so_du

class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, stk, ten, so_du):
        super().__init__(stk, ten, so_du)

    def lai_suat(self):
        self.lai_suat = (self.so_du*8)/100
        return self.lai_suat
