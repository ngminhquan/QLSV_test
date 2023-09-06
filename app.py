from flask import Flask, render_template, redirect, url_for, request
import students as st

'''
print("CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
action = 1
 
while action != 0:
    print("------------------------")
    print("|- Nhập 1: Danh sách ---")
    print("|- Nhập 2: Thêm      ---")
    print("|- Nhập 3: Xóa       ---")
    print("|- Nhập 4: Sửa       ---")
    print("|- Nhập 0: Thoát     ---")
    print("------------------------")
 
    action = int(input())
    s = st.Students()
 
    if action == 1:
        print('DANH SÁCH SINH VIÊN')
        s.show()
    elif action == 2:
        print('THÊM SINH VIÊN')
        print("Nhập Tên sinh viên: ", end='')
        name = input()
        s.insert(name)
    elif action == 3:
        print('XÓA SINH VIÊN')
        print("Nhập ID sinh viên cần xóa: ", end='')
        id = input()
        s.delete(id)
    elif action == 4:
        print('CẬP NHẬT SINH VIÊN')
        print("Nhập ID sinh viên cần cập nhật: ", end='')
        id = input()
        print("Nhập tên sinh viên mới: ", end="")
        name = input()
        s.update(id, name)
    else:
        break


'''

s = st.Students()
 
app = Flask(__name__)


#tổng quan về app qlsv
@app.route('/')
def index():
   return '<html><body><a href = "http://localhost:5000/student">access</a></body></html>'



#Hiển thị danh sách sv trong hệ thống
@app.route('/student', methods=['POST', 'GET'])
def show_db():
    rows = s.show()
        
    return render_template('home.html', students=rows)
    
    return render_template('home.html')


#Thêm sinh viên mới vào hệ thống
@app.route('/student/add', methods=['GET', 'POST'] )
def add_sv():
    #render_template('add.html')
    if request.method == 'POST':
        ad = request.form['username']
        af = s.insert(ad)
        return redirect(url_for('show_db'))
        return redirect(url_for('show_db'))
    
    return '<form action = "" method = "post">\
      <p><input type = "text" name = "username"/></p>\
      <p><input type = "submit" value = "Login"/></p>\
   </form>'

#Sửa thông tin 1 sinh viên với id và tên
@app.route('/student/edit', methods=['GET', 'POST'])
def edit_sv():
    #render_template('edit.html')
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['username']
        editsv = s.update(id, name)
        return redirect(url_for('show_db'))
    return '<form action = "" method = "POST">\
      <p><input type = "text" name = "id"/></p>\
      <p><input type = "text" name = "username"/></p>\
      <p><input type = "submit" value = "Login"/></p>\
   </form>'

#xóa 1 sinh viên với id
@app.route('/student/delete', methods=['GET', 'POST'])
def del_sv():
    if request.method == 'POST':
        name = request.form['id']
        s.delete(name)
        return redirect(url_for('show_db'))
    return '<form action = "" method = "post">\
      <p><input type = "text" name = "id"/></p>\
      <p><input type = "submit" value = "del"/></p>\
   </form>'


if __name__ == "__main__":
    app.run(debug=True)


