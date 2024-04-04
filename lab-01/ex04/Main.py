from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1):

    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")

    print("*************************MENU****************************")

    print("*********************************************************")
    print("**     1. Thêm sinh viên.                              **")

    print("**     2. Cập nhật thông tin sinh viên bởi ID.         **")

    print("**     3. Xóa sinh viên bởi ID.                        **")

    print("**     4. Tìm kiếm sinh viên theo tên.                 **")

    print("**     5. Sắp xếp sinh viên theo điểm trung bình.      **")

    print("**     6. Sắp xếp sinh viên theo tên chuyên ngành.     **")

    print("**     7. Hiển thị danh sách sinh viên.                **")

    print("**     0. Thoát.                                       **")

    print("*********************************************************")


    key = int(input("Nhập Tùy chọn:"))
    if (key == 1):
        print("\n1. Thêm sinh Viên")
        qlsv.nhapSinhVien()
        print("\n. Thêm sinh Viên Thành Công!")
    elif (key == 2):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên.")
            print("\n Nhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\n Danh sách Sinh Viên Trong!")
    elif (key == 3):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n3 Xóa Sinh Viên.")
            print("\n Nhập ID: ")
            ID = int(input())
            if ( qlsv.deleteById(ID)):
              print("\n Sinh Viên có id = ", ID, "đã bị xóa")  
            else:
                print("\n Sinh Viên có id = ", ID, "Không Tồn Tại")
        else:
            print("\n Danh sách Sinh Viên Trong!")
    elif (key == 4):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n4. Tìm kiếm SInh Viên Theo Tên.")
            print("\n Nhập tên để Tìm Kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\n Danh sách Sinh Viên Trong!")
    elif (key == 5):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n5. Sắp Xếp Sinh viên theo diểm trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh sách Sinh Viên Trong!")
    elif (key == 6):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên Theo Tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh sách Sinh Viên Trong!")
    elif (key == 7):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh sách Sinh Viên Trong!")
    elif (key == 0):      
        print("\n Bạn đã chọn thoát Chương Trình")
        break
    else:
        print("\n Không có chức năng này!")
        print("\n Hãy chọn chức năng trong hộp menu")
        