class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        if he_so_luong <= 0:
            raise ValueError("Hệ số lương phải lớn hơn 0")
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong
        self.luong_toi_da = luong_toi_da
    def tinh_thu_nhap(self, luong_co_ban=1000000):
        luong = self.he_so_luong * luong_co_ban
        return min(luong, self.luong_toi_da)
    def hien_thi_thong_tin(self):
        print(f"Mã NV: {self.ma_nv} | Họ tên: {self.ho_ten} | Năm sinh: {self.nam_sinh} | Giới tính: {self.gioi_tinh}")
        print(f"Địa chỉ: {self.dia_chi} | Hệ số lương: {self.he_so_luong} | Lương tối đa: {self.luong_toi_da:,.0f}")
class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        hop_dong_hop_le = ["3 tháng", "6 tháng", "1 năm"]
        if thoi_han_hd not in hop_dong_hop_le:
            raise ValueError("Thời hạn hợp đồng chỉ được là: '3 tháng', '6 tháng', '1 năm'")
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_ld = phu_cap_ld
    def tinh_thu_nhap(self, luong_co_ban=1000000):
        luong_co_ban_tinh_duoc = super().tinh_thu_nhap(luong_co_ban)
        thu_nhap_tong = luong_co_ban_tinh_duoc + self.phu_cap_ld
        return min(thu_nhap_tong, self.luong_toi_da)

    def hien_thi_thong_tin(self):
        print("\n--- Thông tin Cộng tác viên ---")
        super().hien_thi_thong_tin()
        print(f"Thời hạn HĐ: {self.thoi_han_hd} | Phụ cấp LĐ: {self.phu_cap_ld:,.0f}")
        print(f"Tổng thu nhập: {self.tinh_thu_nhap():,.0f}")

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri_cv):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri_cv = vi_tri_cv

    def hien_thi_thong_tin(self):
        print("\n--- Thông tin Nhân viên chính thức ---")
        super().hien_thi_thong_tin()
        print(f"Vị trí công việc: {self.vi_tri_cv}")
        print(f"Tổng thu nhập: {self.tinh_thu_nhap():,.0f}")


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bd_quan_ly, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bd_quan_ly = ngay_bd_quan_ly
        self.phu_cap_ql = phu_cap_ql

    def tinh_thu_nhap(self, luong_co_ban=1000000):
        luong_co_ban_tinh_duoc = super().tinh_thu_nhap(luong_co_ban)
        thu_nhap_tong = luong_co_ban_tinh_duoc + self.phu_cap_ql
        return min(thu_nhap_tong, self.luong_toi_da)

    def hien_thi_thong_tin(self):
        print("\n--- Thông tin Trưởng phòng ---")
        super().hien_thi_thong_tin()
        print(f"Ngày BĐ quản lý: {self.ngay_bd_quan_ly} | Phụ cấp QL: {self.phu_cap_ql:,.0f}")
        print(f"Tổng thu nhập: {self.tinh_thu_nhap():,.0f}")
if __name__ == "__main__":
    try:
        ctv = CongTacVien("CTV01", "Ngô Bá Khá", 2000, "Nam", "Hà Nội", 1.5, 5000000, "6 tháng", 500000)
        ctv.hien_thi_thong_tin()

        nvc = NhanVienChinhThuc("NV01", "Trần Hà Linh", 1995, "Nữ", "Đà Nẵng", 2.5, 10000000, "Kế toán")
        nvc.hien_thi_thong_tin()

        tp = TruongPhong("TP01", "Lê Bon Giêm", 1985, "Nam", "TP.HCM", 4.0, 20000000, "01/01/2023", 3000000)
        tp.hien_thi_thong_tin()

    except ValueError as e:
        print(f"Lỗi dữ liệu đầu vào: {e}")