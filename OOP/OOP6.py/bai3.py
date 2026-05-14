import math

class MauSoBangKhong(Exception):
    pass
class PhanSo:
    def __init__(self, tu, mau):
        self.tu_so = tu
        self.mau_so = mau

    @property
    def tu_so(self):
        return self._tu_so

    @tu_so.setter
    def tu_so(self, value):
        self._tu_so = value

    @property
    def mau_so(self):
        return self._mau_so

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong("Lỗi: Mẫu số không được bằng 0!")
        self._mau_so = value

    def is_toi_gian(self):
        return math.gcd(self._tu_so, self._mau_so) == 1

    def toi_gian(self):
        ucln = math.gcd(self._tu_so, self._mau_so)
        tu_moi = self._tu_so // ucln
        mau_moi = self._mau_so // ucln
        
        if mau_moi < 0:
            tu_moi = -tu_moi
            mau_moi = -mau_moi
        return PhanSo(tu_moi, mau_moi)

    def __add__(self, other):
        if isinstance(other, PhanSo):
            tu_moi = (self._tu_so * other._mau_so) + (other._tu_so * self._mau_so)
            mau_moi = self._mau_so * other._mau_so
            return PhanSo(tu_moi, mau_moi).toi_gian()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, PhanSo):
            tu_moi = (self._tu_so * other._mau_so) - (other._tu_so * self._mau_so)
            mau_moi = self._mau_so * other._mau_so
            return PhanSo(tu_moi, mau_moi).toi_gian()
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, PhanSo):
            return PhanSo(self._tu_so * other._tu_so, self._mau_so * other._mau_so).toi_gian()
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, PhanSo):
            if other._tu_so == 0:
                raise MauSoBangKhong("Lỗi: Không thể chia cho phân số có tử bằng 0 (dẫn đến mẫu số mới bằng 0).")
            return PhanSo(self._tu_so * other._mau_so, self._mau_so * other._tu_so).toi_gian()
        return NotImplemented

    def lay_gia_tri_thuc(self):
        """Hàm phụ trợ để lấy giá trị float phục vụ so sánh"""
        return self._tu_so / self._mau_so

    def __eq__(self, other):
        if isinstance(other, PhanSo):
            ps1 = self.toi_gian()
            ps2 = other.toi_gian()
            return (ps1._tu_so == ps2._tu_so) and (ps1._mau_so == ps2._mau_so)
        return False

    def __lt__(self, other):
        if isinstance(other, PhanSo):
            return self.lay_gia_tri_thuc() < other.lay_gia_tri_thuc()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, PhanSo):
            return self.lay_gia_tri_thuc() > other.lay_gia_tri_thuc()
        return NotImplemented

    def __str__(self):
        if self._tu_so == 0:
            return "0"
        if self._mau_so == 1:
            return str(self._tu_so)
        if self._mau_so == -1:
            return str(-self._tu_so)
        return f"{self._tu_so}/{self._mau_so}"

    def __repr__(self):
        return f"PhanSo({self._tu_so}, {self._mau_so})"

    def __hash__(self):
        ps_tg = self.toi_gian()
        return hash((ps_tg._tu_so, ps_tg._mau_so))

if __name__ == "__main__":
    print("--- KIỂM TRA TẠO PHÂN SỐ VÀ EXCEPTION ---")
    try:
        ps1 = PhanSo(1, 2)
        ps2 = PhanSo(3, 4)
        ps3 = PhanSo(2, 4)
    except MauSoBangKhong as e:
        print(e)

    print("\n--- KIỂM TRA PHÉP TOÁN (+, -, *, /) ---")
    print(f"Cộng: {ps1} + {ps2} = {ps1 + ps2}")
    print(f"Trừ : {ps1} - {ps2} = {ps1 - ps2}")
    print(f"Nhân: {ps1} * {ps2} = {ps1 * ps2}")
    print(f"Chia: {ps1} / {ps2} = {ps1 / ps2}")

    print("\n--- KIỂM TRA RÚT GỌN VÀ __hash__ (SET) ---")
    print(f"Phân số {ps3} có tối giản không? -> {ps3.is_toi_gian()}")
    print(f"Dạng tối giản của {ps3} là: {ps3.toi_gian()}")
    
    tap_hop_ps = {PhanSo(1, 2), PhanSo(2, 4), PhanSo(3, 6), PhanSo(3, 4)}
    print(f"Set các phân số (tự loại trùng): {tap_hop_ps}")

    print("\n--- ỨNG DỤNG: NHẬP VÀ XỬ LÝ DÃY PHÂN SỐ ---")
    danh_sach_ps = [PhanSo(10, 4), PhanSo(3, 4), PhanSo(1, 3), PhanSo(-5, 2), PhanSo(2, 6)]
    
    print("1. Dãy phân số ban đầu:")
    print([str(ps) for ps in danh_sach_ps])
    
    print("2. In ra dạng tối giản của các phân số đó:")
    print([str(ps.toi_gian()) for ps in danh_sach_ps])
    
    ds_sap_xep = sorted(danh_sach_ps)
    print("3. Sắp xếp dãy phân số theo giá trị tăng dần:")
    print([str(ps) for ps in ds_sap_xep])