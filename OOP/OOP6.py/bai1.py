from abc import ABC, abstractmethod
import pickle
class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia
    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang
    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Lỗi: Giá của sản phẩm '{self._ten_hang}' không được nhỏ hơn 0!")
        self._gia = value
    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass
    def __str__(self):
        return f"Mã: {self._ma_hang: <5} | Tên: {self._ten_hang: <15} | Giá: {self._gia: <10}"

    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False

    def __lt__(self, other):
        if isinstance(other, HangHoa):
            return self.gia < other.gia
        return NotImplemented

    def __hash__(self):
        return hash(self.ma_hang)
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, thoi_gian_bh):
        super().__init__(ma_hang, ten_hang, gia)
        self.thoi_gian_bh = thoi_gian_bh

    def loai_hang(self):
        return "Điện Máy"

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.__str__()} | Bảo hành: {self.thoi_gian_bh} tháng"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, nha_san_xuat):
        super().__init__(ma_hang, ten_hang, gia)
        self.nha_san_xuat = nha_san_xuat

    def loai_hang(self):
        return "Sành Sứ"

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.__str__()} | NSX: {self.nha_san_xuat}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_het_han):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_het_han = ngay_het_han

    def loai_hang(self):
        return "Thực Phẩm"

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.__str__()} | HSD: {self.ngay_het_han}"
class QuanLyHangHoa:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, hang):
        if hang in self.danh_sach:
            raise MaHangTrungLap(f"Lỗi: Mã hàng '{hang.ma_hang}' đã tồn tại trong danh sách!")
        self.danh_sach.append(hang)

    def luu_file(self, ten_file):
        with open(ten_file, 'wb') as f:
            pickle.dump(self.danh_sach, f)
        print(f"-> Đã lưu {len(self.danh_sach)} sản phẩm vào file '{ten_file}'.")

    def doc_file(self, ten_file):
        try:
            with open(ten_file, 'rb') as f:
                self.danh_sach = pickle.load(f)
            print(f"-> Đã đọc {len(self.danh_sach)} sản phẩm từ file '{ten_file}'.")
        except FileNotFoundError:
            print(f"-> File '{ten_file}' chưa tồn tại.")
if __name__ == "__main__":
    ql = QuanLyHangHoa()

    print("--- 1. Thêm hàng hóa & Xử lý Exception ---")
    try:
        sp1 = HangDienMay("DM01", "Tivi Sony", 15000000, 24)
        sp2 = HangSanhSu("SS01", "Chén Bát Tràng", 50000, "Bát Tràng")
        sp3 = HangThucPham("TP01", "Sữa Tươi", 30000, "20/12/2024")
        
        ql.them_hang(sp1)
        ql.them_hang(sp2)
        ql.them_hang(sp3)
        
        print("Thêm thành công 3 sản phẩm!")

    except GiaKhongHopLe as e:
        print(e)
    except MaHangTrungLap as e:
        print(e)

    print("\n--- 2. Đa hình (Polymorphism) & inTTin() ---")
    for sp in ql.danh_sach:
        print(sp.inTTin())

    print("\n--- 3. Magic Method: __lt__ dùng cho sorted() ---")
    ds_sap_xep = sorted(ql.danh_sach)
    for sp in ds_sap_xep:
        print(f"{sp.ma_hang} - Giá: {sp.gia}")

    print("\n--- 4. Magic Method: __hash__ dùng cho set() ---")
    tap_hop = set(ql.danh_sach)
    print(f"Số lượng phần tử trong set: {len(tap_hop)}")

    print("\n--- 5. Context Manager (with open) ---")
    FILE_NAME = "data_hanghoa.pkl"
    ql.luu_file(FILE_NAME)
    ql_moi = QuanLyHangHoa()
    ql_moi.doc_file(FILE_NAME)
    print("Dữ liệu sau khi đọc từ file:")
    for sp in ql_moi.danh_sach:
         print(sp.inTTin())