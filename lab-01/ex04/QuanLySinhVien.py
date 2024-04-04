from SinhVien import SinhVien

class QuanLySinhVien:

    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.SoLuongSinhVien() > 0):  # Use self. instead of this.
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
        maxId = maxId + 1
        return maxId

    def SoLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên:")
        sex = input("Nhập giới tính sinh vien:")
        major = input("Nhập chuyên ngành của sinh viên:")
        diemTB = float( input("Nhập điểm của sinh viên:"))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhập tên sinh viên:")
            sex = input("Nhập giới tính sinh vien:")
            major =  input("Nhập chuyên ngành của sinh viên:")
            diemTB = input("Nhập điểm của sinh viên:")
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} Không Tồn Tại.")
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False )
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False )
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False )
    
    def findByID(self, ID):
        searchResult = None
        if (self.SoLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    def findByName(self, keywords):
        listSV = []
        if (self.SoLuongSinhVien() >0):
            for sv in self.listSinhVien:
                if (keywords.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(float(sv._diemTB) >= 8):
            sv._hocLuc = "Giỏi"
        elif (float(sv._diemTB) >= 6.5):
            sv._hocLuc = "Khá"
        elif (float(sv._diemTB) >= 5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID","Name","Sex","Major","Diem TB","Hoc Luc",))
        if (listSV.__len__() >0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                    .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
                print("\n")
    
    def getListSinhVien(self):
        return self.listSinhVien