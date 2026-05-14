class ConCho:
    def __init__(self, ten, mau_sac, giong, cam_xuc):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc
    def sua(self):
        print(f"[{self.ten}] đang sủa.")

    def vay_duoi(self):
        print(f"[{self.ten}] đang vẫy đuôi.")

    def an(self):
        print(f"[{self.ten}] đang ăn.")

    def chay(self):
        print(f"[{self.ten}] đang chạy.")
class Oto:
    def __init__(self, hang, kich_thuoc, mau_sac, gia):
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau_sac = mau_sac
        self.gia = gia
    def tang_toc(self):
        print(f"Chiếc {self.hang} màu {self.mau} đang tăng tốc!")

    def giam_toc(self):
        print(f"Chiếc {self.hang} đang giảm tốc.")

    def dam(self):
        print(f"Cảnh báo: Chiếc {self.hang} vừa xảy ra va chạm (đâm)!")
class TaiKhoan:
    def __init__(self, ten_taikhoan, so_taikhoan, ngan_hang, so_du):
        self.ten_taikhoan = ten_taikhoan
        self.so_taikhoan = so_taikhoan
        self.ngan_hang = ngan_hang
        self.so_du = so_du
    def gui(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
            print(f"Đã gửi {so_tien} vào tài khoản. Số dư mới: {self.so_du}")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def rut(self, so_tien):
        if 0 < so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien}. Số dư còn lại: {self.so_du}")
        else:
            print("Số dư không đủ hoặc số tiền rút không hợp lệ.")

    def kiem_tra_so_du(self):
        print(f"Tài khoản {self.so_tk} của {self.ten_tk} tại {self.ngan_hang} có số dư: {self.so_du}")