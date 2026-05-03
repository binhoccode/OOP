import copy
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            S = args[0]
            self.__d1 = copy.deepcopy(S.get_d1())
            self.__d2 = copy.deepcopy(S.get_d2())
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
            
        else:
            raise ValueError("Tham số khởi tạo không hợp lệ!")
    def get_d1(self):
        return self.__d1

    def get_d2(self):
        return self.__d2
    def in_thong_tin(self, ten_doan_thang="Đoạn thẳng"):
        print(f"{ten_doan_thang}: Nối từ điểm d1{self.__d1} đến điểm d2{self.__d2}")
if __name__ == "__main__":
    print("1. Khởi tạo mặc định:")
    line1 = LineSegment()
    line1.in_thong_tin("Line 1")
    print("\n2. Khởi tạo với 2 đối tượng Point:")
    p_A = Point(10, 20)
    p_B = Point(30, 40)
    line2 = LineSegment(p_A, p_B)
    line2.in_thong_tin("Line 2")
    print("\n3. Khởi tạo với 4 số nguyên (x1, y1, x2, y2):")
    line3 = LineSegment(5, 5, 15, 15)
    line3.in_thong_tin("Line 3")
    print("\n4. Khởi tạo sao chép sâu (Line 4 copy từ Line 3):")
    line4 = LineSegment(line3)
    line4.in_thong_tin("Line 4")
    line3.get_d1().x = 999 
    print("\n--- Sau khi đổi d1.x của Line 3 thành 999 ---")
    line3.in_thong_tin("Line 3 (Đã sửa)")
    line4.in_thong_tin("Line 4 (Bản sao)")