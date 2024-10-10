class Database():
  def __init__(self):
    self.conn = sqlite3.connect("student.db")
    self.cur = self.conn.cursor()
  
  def create_table(self):
    self.cur.execute('''CREATE TABLE IF NOT EXISTS student (
      name TEXT,
      age INTEGER,
      gender TEXT
    )''')
    self.conn.commit()
  
  def add_data(self,name,age,gender):
    self.cur.execute("INSERT INTO student VALUES (?,?,?)",(name,age,gender))
    self.conn.commit()
  
  def get_data(self,name):
    self.cur.execute("SELECT * FROM student WHERE name = ?",(name,))
    return self.cur.fetchone()
  
  def get_all_data(self):
    self.cur.execute("SELECT * FROM student")
    return self.cur.fetchall()

  def remove_data(self,name):
    self.cur.execute("DELETE FROM student WHERE name = ?",(name,))
    self.conn.commit()
  
  def update_data(self,name,age):
    self.cur.execute("UPDATE student SET age = ? WHERE NAME = ?",(age,name))
    self.conn.commit()

class Student():
  def __init__(self):
    self.db = Database()
    self.db.create_table()
  
  def add_student(self,name,age,gender):
    self.db.add_data(name,age,gender)
  
  def get_student(self,name):
    return self.db.get_data(name)
  
  def get_all_student(self):
    return self.db.get_all_data()
  
  def remove_student(self,name):
    self.db.remove_data(name)
  
  def update_student(self,name,age):
    self.db.update_data(name,age)


if __name__ == "__main__":
  student = Student()

  while True:
    print("1. Add Student into Data")
    print("2. Get Student info")
    print("3. Get all Information")
    print("4. Remove Student from Database")
    print("5. Update Student information")
    print("6. Exit")


    choice = int(input("Enter your choice:"))

    if choice == 1:
      name = input("Enter name:")
      age = int(input("Enter age"))
      gender = input("Enter gender:")
      student.add_student(name,age,gender)
    elif choice == 2:
      name = input("Enter name:")
      check = student.get_student(name)
      if check:
        print(check)
      else:
        print("No Record Found")
    elif choice ==3:
      students = student.get_all_student()
      for student in students:
        print(student)
    elif choice == 4:
      name = input("Enter name:")
      check = student.get_student(name)
      if check:
        student.remove_student(name)
        print("Record Deleted")
      else:
        print("No Record Found")
    elif choice == 5:
      name = input("Enter name:")
      age = int(input("Enter age"))
      check = student.get_student(name)
      if check:
        student.update_student(name,age)
        print("Record Updated")
      else:
        print("No Record Found")
    elif choice == 6:
      print("Exiting.......")
      break
    else:
      print("Invalid Choice")
      


