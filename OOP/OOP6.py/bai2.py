from abc import ABC, abstractmethod
import pickle
class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi  # Gọi đến setter để validate
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    @property
    def tuoi(self):
        return self._tuoi
    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(f"Lỗi: Tuổi '{value}' của cán bộ '{self.ho_ten}' không hợp lệ (phải từ 18 đến 65).")
        self._tuoi = value
    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return f"Họ tên: {self.ho_ten: <15} | Tuổi: {self._tuoi: <2} | Giới tính: {self.gioi_tinh: <4} | Địa chỉ: {self.dia_chi: <10}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ho_ten}', {self._tuoi}, '{self.gioi_tinh}', '{self.dia_chi}')"

    def __eq__(self, other):
        if isinstance(other, CanBo):
            return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi
        return False
    def __lt__(self, other):
        if isinstance(other, CanBo):
            ten_self = self.ho_ten.split()[-1]
            ten_other = other.ho_ten.split()[-1]
            if ten_self == ten_other:
                return self.ho_ten < other.ho_ten
        return ten_self < ten_other
        return NotImplemented
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    @property
    def bac(self):
        return self._bac
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(f"Lỗi: Bậc '{value}' của công nhân '{self.ho_ten}' không hợp lệ (phải từ 1 đến 10).")
        self._bac = value
    def mo_ta(self):
        return f"[Công Nhân] {self.__str__()} | Bậc: {self._bac}/10"
class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return f"[Kỹ Sư] {self.__str__()} | Ngành ĐT: {self.nganh_dao_tao}"
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"[Nhân Viên] {self.__str__()} | Công việc: {self.cong_viec}"
class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, can_bo):
        self.danh_sach.append(can_bo)
        print(f"Đã thêm: {can_bo.ho_ten}")

    def tim_kiem_theo_ten(self, ten_can_tim):
        ket_qua = [cb for cb in self.danh_sach if ten_can_tim.lower() in cb.ho_ten.lower()]
        if not ket_qua:
            print(f"Không tìm thấy cán bộ nào có tên: {ten_can_tim}")
        else:
            print(f"--- KẾT QUẢ TÌM KIẾM '{ten_can_tim}' ---")
            for cb in ket_qua:
                print(cb.mo_ta())

    def hien_thi_danh_sach(self):
        print("--- DANH SÁCH CÁN BỘ ---")
        for cb in self.danh_sach:
            print(cb.mo_ta())

    def luu_file(self, ten_file):
        with open(ten_file, 'wb') as f:
            pickle.dump(self.danh_sach, f)
        print(f"-> Đã lưu dữ liệu vào file '{ten_file}'.")

    def doc_file(self, ten_file):
        try:
            with open(ten_file, 'rb') as f:
                self.danh_sach = pickle.load(f)
            print(f"-> Đã đọc dữ liệu từ file '{ten_file}'.")
        except FileNotFoundError:
            print(f"-> Lỗi: File '{ten_file}' chưa tồn tại.")
if __name__ == "__main__":
    qlcb = QLCB()

    print("--- TEST EXCEPTION & THÊM MỚI ---")
    try:
        cn1 = CongNhan("Nguyen Van An", 30, "Nam", "Ha Noi", 5)
        ks1 = KySu("Tran Thi Binh", 28, "Nu", "Hai Phong", "IT")
        nv1 = NhanVien("Le Van Cuong", 45, "Nam", "Da Nang", "Ke Toan")
        ks2 = KySu("Hoang Dung", 25, "Nam", "Can Tho", "Dien")
        
        qlcb.them_moi(cn1)
        qlcb.them_moi(ks1)
        qlcb.them_moi(nv1)
        qlcb.them_moi(ks2)
    except TuoiKhongHopLe as e:
        print(e)
    except BacKhongHopLe as e:
        print(e)

    print("\n--- TEST ĐA HÌNH & HIỂN THỊ ---")
    qlcb.hien_thi_danh_sach()

    print("\n--- TEST TÌM KIẾM ---")
    qlcb.tim_kiem_theo_ten("Binh")

    print("\n--- TEST __eq__ (SO SÁNH BẰNG NHAU) ---")
    cb_test1 = KySu("Tran Thi Binh", 28, "Nu", "Hai Phong", "IT")
    print(f"ks1 có bằng cb_test1 không? -> {ks1 == cb_test1}")

    print("\n--- TEST __lt__ (SẮP XẾP THEO TÊN ABC) ---")
    ds_sap_xep = sorted(qlcb.danh_sach)
    print("Danh sách sau khi sắp xếp theo TÊN (từ A-Z):")
    for cb in ds_sap_xep:
        print(f"{cb.ho_ten: <15} - {cb.__class__.__name__}")

    print("\n--- TEST FILE I/O (LƯU & ĐỌC) ---")
    FILE_NAME = "danh_sach_can_bo.pkl"
    qlcb.luu_file(FILE_NAME)
    qlcb_moi = QLCB()
    qlcb_moi.doc_file(FILE_NAME)
    print("Dữ liệu sau khi đọc từ file:")
    qlcb_moi.hien_thi_danh_sach()
    