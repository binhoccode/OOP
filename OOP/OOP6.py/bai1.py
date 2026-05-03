import pickle
from abc import ABC, abstractmethod

# ==========================================
# 1. CUSTOM EXCEPTION (Ngoại lệ tự định nghĩa)
# ==========================================
class GiaKhongHopLe(Exception):
    """Lỗi sinh ra khi giá sản phẩm nhỏ hơn 0"""
    pass

class MaHangTrungLap(Exception):
    """Lỗi sinh ra khi thêm sản phẩm có mã đã tồn tại"""
    pass


# ==========================================
# 2. ABSTRACT BASE CLASS (Lớp trừu tượng)
# ==========================================
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        # Sử dụng thuộc tính private (biến có gạch dưới)
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia  # Gọi đến @gia.setter để validate ngay khi khởi tạo

    # --- @property: Getter read-only cho ma_hang và ten_hang ---
    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    # --- @property: Getter và Setter cho gia (kèm validation) ---
    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            # Raise Custom Exception
            raise GiaKhongHopLe(f"Lỗi: Giá của '{self._ten_hang}' không hợp lệ ({value}). Giá phải >= 0.")
        self._gia = value

    # --- @abstractmethod ---
    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    # --- Dunder Methods (Magic Methods) ---
    def __str__(self):
        """Hiển thị đẹp khi dùng print(sp)"""
        return f"[{self.ma_hang}] {self.ten_hang} - Giá: {self.gia:,.0f} VND"

    def __eq__(self, other):
        """So sánh bằng nhau dựa trên mã hàng"""
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False

    def __lt__(self, other):
        """So sánh nhỏ hơn dựa trên giá (dùng cho sorted)"""
        return self.gia < other.gia

    def __hash__(self):
        """Băm object để có thể dùng trong set()"""
        return hash(self.ma_hang)


# ==========================================
# 3. CONCRETE CLASSES (Lớp kế thừa)
# ==========================================
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, thoi_gian_bao_hanh):
        super().__init__(ma_hang, ten_hang, gia)
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh

    def loai_hang(self):
        return "Hàng Điện Máy"

    # Method Overriding: Cùng tên hàm inTTin()
    def inTTin(self):
        return f"{self.__str__()} | Bảo hành: {self.thoi_gian_bao_hanh} tháng | Loại: {self.loai_hang()}"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, nha_san_xuat):
        super().__init__(ma_hang, ten_hang, gia)
        self.nha_san_xuat = nha_san_xuat

    def loai_hang(self):
        return "Hàng Sành Sứ"

    # Method Overriding
    def inTTin(self):
        return f"{self.__str__()} | NSX: {self.nha_san_xuat} | Loại: {self.loai_hang()}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, han_su_dung):
        super().__init__(ma_hang, ten_hang, gia)
        self.han_su_dung = han_su_dung

    def loai_hang(self):
        return "Hàng Thực Phẩm"

    # Method Overriding
    def inTTin(self):
        return f"{self.__str__()} | HSD: {self.han_su_dung} | Loại: {self.loai_hang()}"


# ==========================================
# 4. QUẢN LÝ VÀ CHƯƠNG TRÌNH CHÍNH
# ==========================================
class QuanLyHangHoa:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, sp):
        # Kiểm tra trùng lặp mã hàng để raise Exception
        if sp in self.danh_sach: # Hoạt động dựa vào hàm __eq__ đã định nghĩa
            raise MaHangTrungLap(f"Lỗi: Mã hàng '{sp.ma_hang}' đã tồn tại trong hệ thống!")
        self.danh_sach.append(sp)

    def luu_file(self, filename="data_hanghoa.pkl"):
        """Context Manager (with) để lưu file"""
        with open(filename, 'wb') as f:
            pickle.dump(self.danh_sach, f)
        print(f"Đã lưu danh sách vào file {filename}")

    def doc_file(self, filename="data_hanghoa.pkl"):
        """Context Manager (with) để đọc file"""
        try:
            with open(filename, 'rb') as f:
                self.danh_sach = pickle.load(f)
            print(f"Đã đọc dữ liệu từ file {filename}")
        except FileNotFoundError:
            print("Chưa có file dữ liệu, bắt đầu với danh sách trống.")

# --- Demo các yêu cầu ---
if __name__ == "__main__":
    ql = QuanLyHangHoa()

    print("--- 1. KIỂM TRA EXCEPTION VÀ THÊM DỮ LIỆU ---")
    try:
        # Khởi tạo các đối tượng
        sp1 = HangDienMay("DM01", "Tivi Sony", 15000000, 24)
        sp2 = HangSanhSu("SS01", "Bộ ấm trà Minh Long", 850000, "Minh Long")
        sp3 = HangThucPham("TP01", "Sữa Vinamilk", 350000, "12/2024")
        sp4 = HangDienMay("DM02", "Tủ lạnh Samsung", 12000000, 12)
        
        ql.them_hang(sp1)
        ql.them_hang(sp2)
        ql.them_hang(sp3)
        ql.them_hang(sp4)

        # Test Exception 1: Mã trùng lặp
        print("-> Thử thêm mã DM01 lần nữa:")
        sp_trung = HangDienMay("DM01", "Máy giặt", 8000000, 12)
        ql.them_hang(sp_trung) 

    except MaHangTrungLap as e:
        print(e)
    
    try:
        # Test Exception 2: Giá âm
        print("\n-> Thử tạo sản phẩm giá âm:")
        sp_loi_gia = HangThucPham("TP02", "Bánh mì", -5000, "Hôm nay")
    except GiaKhongHopLe as e:
        print(e)

    print("\n--- 2. DEMO ĐA HÌNH VÀ METHOD OVERRIDING ---")
    # Gọi vòng lặp in thông tin (Đa hình: cùng gọi inTTin() nhưng kết quả khác nhau tùy lớp)
    for sp in ql.danh_sach:
        print(sp.inTTin())

    print("\n--- 3. DEMO DUNDER METHODS (__lt__, __str__) ---")
    print("Sắp xếp danh sách theo Giá tăng dần (sử dụng sorted và hàm __lt__):")
    ds_sap_xep = sorted(ql.danh_sach)
    for sp in ds_sap_xep:
        print(sp) # Tự động gọi hàm __str__

    print("\n--- 4. DEMO DUNDER METHOD (__hash__, __eq__) VỚI SET ---")
    # Đưa vào Set, nếu __hash__ và __eq__ hoạt động, các phần tử trùng mã sẽ bị loại trừ
    demo_set = {sp1, sp2, sp1} 
    print(f"Số lượng phần tử trong Set (dù thêm sp1 hai lần): {len(demo_set)}")

    print("\n--- 5. DEMO CONTEXT MANAGER (WITH OPEN) ---")
    ql.luu_file()
    
    # Tạo một quản lý mới và đọc lại từ file
    ql_moi = QuanLyHangHoa()
    ql_moi.doc_file()
    print("Dữ liệu sau khi đọc từ file lên:")
    print(ql_moi.danh_sach[0].inTTin())
