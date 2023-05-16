from flask import Flask, render_template, request, redirect
import csv
from pymongo import MongoClient


app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']

if db.internees.count_documents({}) == 0:
    # data = [{'STT':1, 'name':'Nguyễn Đức Vinh', 'year' : 2002, 'gender' : 'Name', 'school' : 'PTIT', 'major' : 'IT'}]
    data = [{'STT': 1, 'name': 'Bùi Minh Sơn', 'year': 2002, 'gender': 'Nam', 'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Công nghệ thông tin'}, {'STT': 2, 'name': 'Đào Đại Hiệp', 'year': 2001, 'gender': 'Nam', 'school': 'Đại học Bách khoa Hà Nội', 'major': 'Điện tử viễn thông'}, {'STT': 3, 'name': 'Đỗ Anh Tú', 'year': 2002, 'gender': 'Nam', 'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Mạng máy tính và truyền thông dữ liệu'}, {'STT': 4, 'name': 'Đỗ Bảo Hoàng', 'year': 1997, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'}, {'STT': 5, 'name': 'Hoàng Quốc Doanh', 'year': 2001, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': None}, {'STT': 6, 'name': 'Le Minh Duc', 'year': 2002, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'Công nghệ thông tin ứng dụng phần mềm'}, {'STT': 7, 'name': 'Lê Phúc Lai', 'year': 2002, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'Kỹ thuật điện tử viễn thông'}, {'STT': 8, 'name': 'Lê Quang Anh', 'year': 1997, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'}, {'STT': 9, 'name': 'Lê Trọng Minh', 'year': 2000, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Kỹ thuật điều khiển và tự động hóa'}, {'STT': 10, 'name': 'Lê Tùng Lâm', 'year': 1999, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'}, {'STT': 11, 'name': 'Lê Văn Chiến', 'year': 2002, 'gender': 'Nam', 'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Kỹ thuật hàng không vũ trụ'}, {'STT': 12, 'name': 'Linh Thi Nguyen', 'year': 2002, 'gender': 'Nữ', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'ICT'}, {'STT': 13, 'name': 'Nguyễn Đại An', 'year': 2023, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'}, {'STT': 14, 'name': 'Nguyễn Đình Hoàng', 'year': 2002, 'gender': 'Nam', 'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Công nghệ thông tin ứng dụng phần mềm'}, {'STT': 15, 'name': 'Nguyen Duc Vinh Data', 'year': 2002, 'gender': 'Nam', 'school': 'Học viện Công nghệ Bưu chính Viễn thông', 'major': None}, {'STT': 16, 'name': 'Nguyễn Dương Long', 'year': 2002, 'gender': 'Nam', 'school': 'ĐH Thuỷ lợi', 'major': 'Công nghệ thông tin ứng dụng phần mềm'}, {'STT': 17, 'name': 'Nguyen Huu Thang', 'year': 2000, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'}, {'STT': 18, 'name': 'Nguyễn Mạnh Cường', 'year': 1997, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Điện tử'}, {'STT': 19, 'name': 'Nguyễn Mạnh Đức', 'year': 2002, 'gender': 'Nam', 'school': 'Học viện Kỹ thuật mật mã', 'major': 'An toàn thông tin'}, {'STT': 20, 'name': 'Nguyễn Ngọc Chung', 'year': 2002, 'gender': 'Nam', 'school': 'Học viên Công nghệ Bưu chính Viễn Thông HCM', 'major': None}, {'STT': 21, 'name': 'Nguyễn Tuấn Anh', 'year': 1997, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'}, {'STT': 22, 'name': 'Nguyễn Văn Quang', 'year': 1997, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'}, {'STT': 23, 'name': 'Ninh Chí Hướng', 'year': 2002, 'gender': 'Nam', 'school': 'Học viện Công nghệ Bưu chính viễn thông', 'major': 'An toàn thông tin'}, {'STT': 24, 'name': 'Ninh Văn Nghĩa', 'year': 2001, 'gender': 'Nam', 'school': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'}, {'STT': 25, 'name': 'Phạm Anh Đức', 'year': 2001, 'gender': 'Nam', 'school': 'Đại học Bách Khoa Hà Nội', 'major': 'Toán ứng dụng và tin học'}, {'STT': 26, 'name': 'Phạm Duy Cương', 'year': 1997, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Công nghệ điện tử'}, {'STT': 27, 'name': 'Phạm Hồng Thanh', 'year': 1998, 'gender': 'Nam', 'school': 'Swinburne University', 'major': 'Phát triển phần mềm'}, {'STT': 28, 'name': 'Phạm Thị Khánh Linh', 'year': 2002, 'gender': 'Nữ', 'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Mạng máy tính và truyền thông dữ liệu'}, {'STT': 29, 'name': 'Phạm Văn Tới', 'year': 2002, 'gender': 'Nam', 'school': 'Học viện Công nghệ Bưu chính viễn thông', 'major': 'Công nghệ thông tin ứng dụng phần mềm'}, {'STT': 30, 'name': 'Trần Đức Mạnh', 'year': 1998, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Bảo mật thông tin'}, {'STT': 31, 'name': 'Trần Mạnh Dũng', 'year': 2001, 'gender': 'Nam', 'school': 'Học viện Công nghệ Bưu chính Viễn thông', 'major': 'Điện tử viễn thông'}, {'STT': 32, 'name': 'Trần Minh Dương', 'year': 2002, 'gender': 'Nam', 'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Mạng máy tính và truyền thông dữ liệu'}, {'STT': 33, 'name': 'Trần Xuân Phú', 'year': 2001, 'gender': 'Nam', 'school': 'school Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh', 'major': 'Khoa học máy tính'}, {'STT': 34, 'name': 'Vũ Hoàng Long', 'year': 2001, 'gender': 'Nam', 'school': 'Đại học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'}, {'STT': 35, 'name': 'Vũ Minh Hiếu', 'year': 2000, 'gender': 'Nam', 'school': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Kỹ thuật phần mềm'}]
    db.internees.insert_many(data)


@app.route("/")
def index():
    return render_template("index.html", attendees=db.internees.find())

@app.route("/addStudent", methods = ['GET','POST'])
def addStudent():
    if request.method == 'GET':
        return render_template("addStudent.html")
    if request.method == 'POST':
        id = int(request.form["STT"])
        name = request.form["name"]
        year = int(request.form["year"])
        gender = request.form["gender"]
        school = request.form["school"]
        major = request.form["major"]
        db.internees.insert_one({'STT':id, 'name':name, 'year' : year, 'gender' : gender, 'school' : school, 'major' : major})
        return redirect('/')


@app.route('/deleteStudent/<int:id>', methods=['DELETE'])
def deleteStudent(id):
    db.internees.delete_one({"STT": id})
    return redirect('/')



@app.route('/view/<int:id>')
def viewStudent(id):
    students = []
    students.append(db.internees.find_one({"STT": id}))
    return render_template("detail.html", students=students)

@app.route('/updateStudent/<int:id>',methods = ['GET','POST'])
def updateStudent(id):
    students = []
    if request.method == 'GET':
        students.append(db.internees.find_one({"STT":id}))
        return render_template("updateStudent.html", students = students)
    if request.method == 'POST':
        name = request.form["name"]
        year = int(request.form["year"])
        gender = request.form["gender"]
        school = request.form["school"]
        major = request.form["major"]
        db.internees.update_one({'STT':id}, {"$set" : {'name':name, 'year' : year, 'gender' : gender, 'school' : school, 'major' : major}})
        return redirect('/')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)