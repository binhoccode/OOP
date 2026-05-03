class NhanVien:
   LUONG_MAX = 50000000.0
   def __init__(self, ten_nhan_vien, luong_co_ban=int, he_so_luong=int):
    self.ten_nhan_vien = ten_nhan_vien
    self.luong_co_ban = luong_co_ban
    self.he_so_luong = he_so_luong
   def get_ten_nhan_vien(self):
        return self._ten_nhan_vien
   def set_ten_nhan_vien(self, ten_nhan_vien):
        self._ten_nhan_vien = ten_nhan_vien
   def get_luong_co_ban(self):
        return self._luong_co_ban
   def set_luong_co_ban(self, luong_co_ban):
        self._luong_co_ban = luong_co_ban
   def get_he_so_luong(self):
        return self._he_so_luong
   def set_he_so_luong(self, he_so_luong):
        self._he_so_luong = he_so_luong
   def tinh_luong(self):
        return self.luong_co_ban * self.he_so_luong
   def in_ttin_nhan_vien(self):
        print("Thông tin nhân viên:")
        print(f"Tên: {self.ten_nhan_vien}")
        print(f"Lương cơ bản: {self.luong_co_ban}")
        print(f"Hệ số lương: {self.he_so_luong}")
        print(f"Lương thực nhận: {self.luong_co_ban*self.he_so_luong}")
        print("-----------------------------")
   def tang_luong(self, delta):
    luong_moi = self.luong_co_ban * (self.he_so_luong + delta)
    if luong_moi > self.LUONG_MAX:
        print("Lương mới vượt quá mức tối đa. Không thể tăng lương.")
    else:
        self.he_so_luong += delta
        print(f"Lương đã được tăng. Hệ số lương mới: {self.he_so_luong}")
    return True
if __name__ == "__main__":
    nv1 = NhanVien("Triệu Vân",5000000,2.5)
    nv1.in_ttin_nhan_vien()
    print("\n[Hành động] Thực hiện tăng hệ số lương thêm 1.0...")
    if nv1.tang_luong(1.0):
        print("-> Tăng lương thành công! Dưới đây là thông tin mới:")
        nv1.in_ttin_nhan_vien()