class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten} | Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi}")


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc công nhân phải nằm trong khoảng từ 1 đến 10.")
        self.bac = bac

    def hien_thi_thong_tin(self):
        print(">> Loại: Công Nhân")
        super().hien_thi_thong_tin()
        print(f"Bậc: {self.bac}/10")


class Kysu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi_thong_tin(self):
        print(">> Loại: Kỹ Sư")
        super().hien_thi_thong_tin()
        print(f"Ngành đào tạo: {self.nganh_dao_tao}")


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi_thong_tin(self):
        print(">> Loại: Nhân Viên Phục Vụ")
        super().hien_thi_thong_tin()
        print(f"Công việc: {self.cong_viec}")


class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_can_bo(self, can_bo):
        self.danh_sach.append(can_bo)
        print("-> Đã thêm cán bộ thành công!")

    def tim_kiem_theo_ten(self, ten_tim_kiem):
        ket_qua = [cb for cb in self.danh_sach if ten_tim_kiem.lower() in cb.ho_ten.lower()]
        
        if not ket_qua:
            print(f"-> Không tìm thấy cán bộ nào có tên: '{ten_tim_kiem}'")
        else:
            print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{ten_tim_kiem}' ---")
            for cb in ket_qua:
                cb.hien_thi_thong_tin()
                print("-" * 30)

    def hien_thi_danh_sach(self):
        if not self.danh_sach:
            print("-> Danh sách cán bộ hiện đang trống.")
            return
            
        print("\n=== DANH SÁCH TOÀN BỘ CÁN BỘ ===")
        for cb in self.danh_sach:
            cb.hien_thi_thong_tin()
            print("-" * 30)


if __name__ == "__main__":
    quan_ly = QLCB()

    while True:
        print("\n===== QUẢN LÝ CÁN BỘ =====")
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị thông tin danh sách cán bộ")
        print("4. Thoát khỏi chương trình")
        
        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")

        if lua_chon == '1':
            loai_cb = input("Chọn loại cán bộ (1-Công nhân, 2-Kỹ sư, 3-Nhân viên): ")
            ho_ten = input("Nhập họ tên: ")
            tuoi = int(input("Nhập tuổi: "))
            gioi_tinh = input("Nhập giới tính (Nam/Nữ/Khác): ")
            dia_chi = input("Nhập địa chỉ: ")

            if loai_cb == '1':
                bac = int(input("Nhập bậc (1-10): "))
                try:
                    cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
                    quan_ly.them_can_bo(cb)
                except ValueError as e:
                    print(f"Lỗi: {e}")
            elif loai_cb == '2':
                nganh = input("Nhập ngành đào tạo: ")
                cb = Kysu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
                quan_ly.them_can_bo(cb)
            elif loai_cb == '3':
                cong_viec = input("Nhập công việc: ")
                cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
                quan_ly.them_can_bo(cb)
            else:
                print("Lựa chọn loại cán bộ không hợp lệ!")

        elif lua_chon == '2':
            ten_can_tim = input("Nhập họ tên cần tìm kiếm: ")
            quan_ly.tim_kiem_theo_ten(ten_can_tim)

        elif lua_chon == '3':
            quan_ly.hien_thi_danh_sach()

        elif lua_chon == '4':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")