from mysql.connector import MySQLConnection, Error
 
class Students:
 
    conn = None
 
    def __init__(self):
        """Hàm khởi tạo constructor"""
        self.connect()
 
    def __del__(self):
        """Hàm hủy destructor"""
        if self.conn != None:
            self.conn.close()
 
    def connect(self):
        """ Kết nối MySQL bằng module MySQLConnection """
        db_config = {
            'host': 'localhost',
            'database': 'qlsv',
            'user': 'root',
            'password': 'minhQuanLOV3'
        }
 
        conn = None
 
        try:
            conn = MySQLConnection(**db_config)
            if conn.is_connected() == False:
                raise Error
 
        except Error as error:
            print(error)
 
        self.conn = conn
 
    def show(self):
        '''
        """Hàm hiển thị danh sách sinh viên"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM students")
            row = cursor.fetchone()
            a = []
            while row is not None:
                print(row)
                row = cursor.fetchone()
 
        except Error as e:
            print(e)
 
        finally:
            cursor.close()
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
        return []
 
    def insert(self, fullname):
        """Hàm thêm sinh viên"""
        query = "INSERT INTO students(fullname) VALUES(%s)"
        args = (fullname,)
 
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
 
            if cursor.lastrowid:
                print('Insert thành công!')
            else:
                print('Insert thất bại!')
 
            self.conn.commit()
            return self.show()
 
        except Error as error:
            print(error)
 
        finally:
            cursor.close()
 
 
    def update(self, id, name):
        """Hàm update sinh viên"""
        query = """ UPDATE students
                    SET fullname = %s
                    WHERE id = %s """
        data = (name, id)
 
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, data)
            self.conn.commit()
            return self.show()
 
        except Error as error:
            return 'error'
 
        finally:
            cursor.close()
 
    def delete(self, id):
        """Hàm xóa sinh viên"""
        query = "DELETE FROM students WHERE id = %s"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (id,))
            self.conn.commit()
            return self.show()
 
        except Error as error:
            return error
 
        finally:
            cursor.close()