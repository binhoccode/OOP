class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def xuat_thong_tin(self):
        print(f"Mã hàng: {self.ma_hang}")
        print(f"Tên hàng: {self.ten_hang}")
        print(f"Nhà sản xuất: {self.nha_sx}")
        print(f"Giá: {self.gia:,.0f} VNĐ")
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, thoi_gian_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat
    def xuat_thong_tin(self):
        print("\n[Hàng Điện Máy]")
        super().xuat_thong_tin()
        print(f"Thời gian bảo hành: {self.thoi_gian_bao_hanh} tháng")
        print(f"Điện áp: {self.dien_ap} V")
        print(f"Công suất: {self.cong_suat} W")
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu
    def xuat_thong_tin(self):
        print("\n[Hàng Sành Sứ]")
        super().xuat_thong_tin()
        print(f"Loại nguyên liệu: {self.loai_nguyen_lieu}")
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, ngay_san_xuat, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.ngay_san_xuat = ngay_san_xuat
        self.ngay_het_han = ngay_het_han
    def xuat_thong_tin(self):
        print("\n[Hàng Thực Phẩm]")
        super().xuat_thong_tin()
        print(f"Ngày sản xuất: {self.ngay_san_xuat}")
        print(f"Ngày hết hạn: {self.ngay_het_han}")
if __name__ == "__main__":
    may_giat = HangDienMay(ma_hang="DM001", ten_hang="Máy giặt LG", nha_san_xuat="LG Electronics", gia=12000000, thoi_gian_bao_hanh=24, dien_ap=220, cong_suat=1500)
    binh_su = HangSanhSu(ma_hang="SS001", ten_hang="Bình sứ Bát Tràng", nha_san_xuat="Bát Tràng", gia=500000, loai_nguyen_lieu="Sứ cao cấp")
    sua_tuoi = HangThucPham(ma_hang="TP001", ten_hang="Sữa tươi Vinamilk", nha_san_xuat="Vinamilk", gia=30000, ngay_san_xuat="2026-04-18", ngay_het_han="2027-08-07")
    print("== Danh sách hàng hóa ==")
    may_giat.xuat_thong_tin()
    binh_su.xuat_thong_tin()
    sua_tuoi.xuat_thong_tin()