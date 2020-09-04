import tkinter as tk  # importing tkinter only as tk
from PIL import ImageTk  # package for image used
from tkinter import ttk, messagebox  # for combobox and messagebox
# imported from another python packages
from back_end.database_connection import *
from model.model_student import *
from model.model_user_login import *


# main window class
class student_manage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1450x730+30+20')
        self.config(bg='grey')
        self.title('Student Management System')
        self._frame = None
        self.switch_frame(user_login)

    # function for switching frame
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# class for login window to enter into student management system
class user_login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.dbconn = DbConnection()
        master.resizable(False, False)

        # ============all images used from image package in front_end===============================================
        self.bg_img = ImageTk.PhotoImage(file="image/bg_img.jpg")
        self.user_icon = ImageTk.PhotoImage(file="image/user.png")
        self.pass_icon = ImageTk.PhotoImage(file="image/pass.png")
        self.logo_icon = ImageTk.PhotoImage(file="image/logo.png")

        # for background image of user login
        self.bg_fm = tk.Frame(master, width=1450, height=730)
        self.bg_fm.place(x=0, y=0)
        lbl_bg = tk.Label(self.bg_fm, image=self.bg_img)
        lbl_bg.pack()

        # main frame for user login
        self.lg_fm1 = tk.Frame(master, width=350, height=300, bd=3, bg='#f3efee')
        self.lg_fm1.place(x=550, y=250)

        # ============================inside lg_fm1=================================================================
        lbl_logo = tk.Label(self.lg_fm1, image=self.logo_icon, bg='#f3efee')
        lbl_logo.place(x=150, y=0)

        lbl_admin = tk.Label(self.lg_fm1, text='Admin Login', font=('times', 20, 'bold'), bg='#f3efee', fg='#657076')
        lbl_admin.place(x=90, y=40)

        lbl_dev = tk.Label(self.lg_fm1, text='Developed By:', font=('times', 10), bg='#f3efee', fg='#a4623a')
        lbl_dev.place(x=80, y=75)

        lbl_dev1 = tk.Label(self.lg_fm1, text='Samir Thapaliya', font=('times', 10, 'italic'), bg='#f3efee',
                            fg='#a4623a')
        lbl_dev1.place(x=165, y=75)

        #  label for placing user icon
        lbl_user = tk.Label(self.lg_fm1, image=self.user_icon, font=('times', 15))
        lbl_user.place(x=35, y=120)

        # entry field for username
        self.ent_username = tk.Entry(self.lg_fm1, width=35)
        self.ent_username.place(x=80, y=128)

        # for text message bellow username
        lbl_user1 = tk.Label(self.lg_fm1, text='enter the username provided', font=('times', 9, 'italic'), bg='#f3efee',
                             fg='#d72c0e')
        lbl_user1.place(x=80, y=150)

        # label for password label
        lbl_pass = tk.Label(self.lg_fm1, image=self.pass_icon, font=('times', 15))
        lbl_pass.place(x=35, y=190)

        # entry field for password
        self.ent_password = tk.Entry(self.lg_fm1, show='*', width='35')
        self.ent_password.place(x=80, y=198)

        # for text message below password
        lbl_pass1 = tk.Label(self.lg_fm1, text='enter the password provided', font=('times', 9, 'italic'), bg='#f3efee',
                             fg='#d72c0e')
        lbl_pass1.place(x=80, y=220)

        # for login button
        self.fm_btn = tk.Frame(master, width=150)
        self.fm_btn.place(x=660, y=530)
        lg_btn = tk.Button(self.fm_btn, text='login', width=10, font=('times', 15, 'bold'), bg='#494e78', fg='white',
                           command=self.login_verification)
        lg_btn.pack()

    # function for login verification
    def login_verification(self):
        while True:
            verification = login(self.ent_username.get(), self.ent_password.get())
            query = 'select * from login where user=%s and password= %s'
            values = (verification.get_user(), verification.get_password())
            rows = self.dbconn.user_login(query, values)
            if rows:
                messagebox.showinfo('Welcome', 'Login Successful')
                self.master.switch_frame(student)

            elif verification.get_user() == '' or verification.get_password() == '':
                messagebox.showerror('Error', 'please fill all entries!')
            else:
                messagebox.showerror('error', 'Invalid Username and Password')
            break

    # for destroying all frames created in user login for going into next frame
    def destroy(self):
        self.lg_fm1.destroy()
        self.bg_fm.destroy()
        self.fm_btn.destroy()


# class for student management
class student(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.dbconn = DbConnection()  # database connection

        # ========================image used in background==================================================
        self.bg_fm_img = ImageTk.PhotoImage(file="image/1.jpg")

        # background frame for placing image
        self.bg_frame = tk.Frame(master, width=1450, height=730)
        self.bg_frame.place(x=0, y=0)
        lbl_bg = tk.Label(self.bg_frame, image=self.bg_fm_img).pack()

        # heading at top
        self.admission = tk.Frame(master, bd=0, bg='grey')
        self.admission.place(x=0, y=0, height=55, width=1450)
        user_lb1 = tk.Label(self.admission, text='Student Management System',
                            font=("Comic Sans MS", 28, 'bold'), bd=5, relief=tk.FLAT,
                            bg='#322840', fg='White', height=10)
        user_lb1.pack(side=tk.TOP, fill=tk.X)

        # new frame for adding student
        self.manage_frame = tk.Frame(master, bd=4, relief=tk.RIDGE, bg='#400F46')
        self.manage_frame.place(x=10, y=110, width=670, height=530)

        # heading for manage frame
        title = tk.Label(self.manage_frame, text='Manage Student', font=('Comic Sans MS', 24, 'bold'), bg='#400F46',
                         fg='white')
        title.place(x=200, y=0)

        # ============================all widgets inside manage_frame==============================================
        stu_id = tk.Label(self.manage_frame, text='Student Id', font=('Georgia', 16), bg='#400F46', fg='#D2D2D2')
        stu_id.place(x=10, y=90)
        self.stu_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.stu_ent.place(x=160, y=90)

        f_name = tk.Label(self.manage_frame, text='First Name', font=('times new roman', 16), bg='#400F46',
                          fg='#D2D2D2')
        f_name.place(x=10, y=140)
        self.f_name_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.f_name_ent.place(x=160, y=140)

        l_name = tk.Label(self.manage_frame, text='Last Name', font=('times new roman', 16), bg='#400F46', fg='#D2D2D2')
        l_name.place(x=345, y=140)
        self.l_name_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.l_name_ent.place(x=470, y=140)

        gender = tk.Label(self.manage_frame, text='Gender', font=('times new roman', 16), bg='#400F46', fg='#D2D2D2')
        gender.place(x=10, y=190)
        self.gender_combo = tk.ttk.Combobox(self.manage_frame, width=12, font=('times new roman', 14), state='readonly')
        self.gender_combo['values'] = ('Male', 'Female', 'Other')
        self.gender_combo.place(x=160, y=190)

        dob = tk.Label(self.manage_frame, text='D.O.B', font=('times new roman', 16), bg='#400F46', fg='#D2D2D2')
        dob.place(x=10, y=240)
        self.dob_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.dob_ent.place(x=160, y=240)
        dob_txt = tk.Label(self.manage_frame, text='*DD-MM-YYYY', font=('times new roman', 9), bg='#400F46',
                           fg='#D2D2D2')
        dob_txt.place(x=300, y=245)

        contact = tk.Label(self.manage_frame, text='Contact', font=('times new roman', 16), bg='#400F46', fg='#D2D2D2')
        contact.place(x=10, y=290)
        self.contact_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.contact_ent.place(x=160, y=290)

        email = tk.Label(self.manage_frame, text='Email', font=('times new roman', 16), bg='#400F46', fg='#D2D2D2')
        email.place(x=10, y=340)
        self.email_ent = tk.Entry(self.manage_frame, width=20, font=('times new roman', 16))
        self.email_ent.place(x=160, y=340)

        par_nm = tk.Label(self.manage_frame, text='Parent Name', font=('times new roman', 16), bg='#400F46',
                          fg='#D2D2D2')
        par_nm.place(x=10, y=390)
        self.par_nm_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.par_nm_ent.place(x=160, y=390)

        par_con = tk.Label(self.manage_frame, text='Parent Contact', font=('times new roman', 16), bg='#400F46',
                           fg='#D2D2D2')
        par_con.place(x=345, y=390)
        self.par_con_ent = tk.Entry(self.manage_frame, width=12, font=('times new roman', 16))
        self.par_con_ent.place(x=480, y=390)

        address = tk.Label(self.manage_frame, text='Address', font=('times new roman', 16), bg='#400F46', fg='#D2D2D2')
        address.place(x=10, y=440)
        self.address_ent = tk.Text(self.manage_frame, font=('times new roman', 16), width=22, height=3)
        self.address_ent.place(x=160, y=440)

        # =================button frame and it's widgets==========================================================
        self.button_frame = tk.Frame(master, bd=1, bg='#00151E')
        self.button_frame.place(x=90, y=640, width=520, height=50)

        add = tk.Button(self.button_frame, text='Add', width=8, command=self.add, font=('times', 14, 'bold'),
                        bg='#D5DCF8')
        add.pack(side=tk.LEFT, padx=4)
        Clear = tk.Button(self.button_frame, text='Clear', width=8, command=self.clear_data, font=('times', 14, 'bold'),
                          bg='#D5DCF8')
        Clear.pack(side=tk.LEFT, padx=4)
        Update = tk.Button(self.button_frame, text='Update', width=8, command=self.update_data,
                           font=('times', 14, 'bold'), bg='#D5DCF8')
        Update.pack(side=tk.LEFT, padx=4)
        delete = tk.Button(self.button_frame, text='Delete', width=8, command=self.delete_data,
                           font=('times', 14, 'bold'), bg='#D5DCF8')
        delete.pack(side=tk.LEFT, padx=4)

        ext = tk.Button(self.button_frame, text='Exit', width=8, font=('times', 14, 'bold'), bg='crimson',
                        command=lambda: master.switch_frame(user_login))
        ext.pack(side=tk.LEFT, padx=4)

        # ===============================frame for showing student information=====================================
        self.info_frame = tk.Frame(master, bd=4, bg='#322840', relief=tk.RIDGE)
        self.info_frame.place(x=690, y=55, width=765, height=730)

        # label for search
        search_by = tk.Label(self.info_frame, text='Search By', font=('times', 20, 'bold'), bg='#322840',
                             fg='white')
        search_by.place(x=0, y=0)

        # combobox for search option
        self.search_combo = tk.ttk.Combobox(self.info_frame, width=10, font=('times', 12), state='readonly')
        self.search_combo['values'] = ('Student_Id', 'First_name', 'Last_name', 'Contact')
        self.search_combo.place(x=150, y=10)

        # entry for searching value
        self.search_ent = tk.Entry(self.info_frame, font=('times', 16), width=8)
        self.search_ent.place(x=260, y=10)

        # label for sorting
        sort_by = tk.Label(self.info_frame, text='Sort By', font=('times', 20, 'bold'), bg='#322840',
                           fg='white')
        sort_by.place(x=0, y=45)

        # combobox for sort
        self.sort_combo = tk.ttk.Combobox(self.info_frame, width=10, font=('times', 12), state='readonly')
        self.sort_combo['values'] = ('Asc', 'Desc')
        self.sort_combo.place(x=150, y=50)

        # button for search
        search_btn = tk.Button(self.info_frame, text='Search', width=8, height=1, font=('times', 10, 'bold'),
                               command=self.search_value)
        search_btn.place(x=360, y=10)

        # button for showing all values
        show_btn = tk.Button(self.info_frame, text='Show All', width=8, font=('times', 10, 'bold'), command=self.fetch)
        show_btn.place(x=430, y=10)

        # button for sorting
        sort_btn = tk.Button(self.info_frame, text='Sort', width=8, font=('times', 10, 'bold'), command=self.sort)
        sort_btn.place(x=260, y=50)

        # =======================tree view==========================================================================
        self.table1_Frame = tk.Frame(self.info_frame, bd=4, relief=tk.RIDGE)
        self.table1_Frame.place(x=10, y=90, width=730, height=570)

        scroll_x = tk.Scrollbar(self.table1_Frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(self.table1_Frame, orient=tk.VERTICAL)
        self.Student_table = tk.ttk.Treeview(self.table1_Frame,
                                             columns=(
                                                 'Student_Id', 'First_name', 'Last_name', 'Gender', 'DOB', 'Contact',
                                                 'Email', 'Parent_name', 'Parent_contact', 'Address'),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading('Student_Id', text='Student Id')
        self.Student_table.heading('First_name', text='First name')
        self.Student_table.heading('Last_name', text='Last name')
        self.Student_table.heading('Gender', text='Gender')
        self.Student_table.heading('DOB', text='D.O.B')
        self.Student_table.heading('Contact', text='Contact')
        self.Student_table.heading('Email', text='Email')
        self.Student_table.heading('Parent_name', text='Parent Name')
        self.Student_table.heading('Parent_contact', text='Parent Contact')
        self.Student_table.heading('Address', text='Address')
        self.Student_table['show'] = 'headings'

        self.Student_table.column('Student_Id', width=100)
        self.Student_table.column('First_name', width=100)
        self.Student_table.column('Last_name', width=100)
        self.Student_table.column('Gender', width=100)
        self.Student_table.column('DOB', width=100)
        self.Student_table.column('Contact', width=100)
        self.Student_table.column('Email', width=150)
        self.Student_table.column('Parent_name', width=100)
        self.Student_table.column('Parent_contact', width=100)
        self.Student_table.column('Address', width=200)
        self.Student_table.pack(fill=tk.BOTH, expand=1)
        self.Student_table.bind('<ButtonRelease-1>', self.show_data)

        self.fetch()

    # function for add student information
    def add(self):
        try:
            stu = student_detail(self.stu_ent.get(), self.f_name_ent.get(), self.l_name_ent.get(),
                                 self.gender_combo.get(),
                                 self.dob_ent.get(), self.contact_ent.get(), self.email_ent.get(),
                                 self.par_nm_ent.get(),
                                 self.par_con_ent.get(), self.address_ent.get('1.0', tk.END))
            if stu.get_Student_Id() == '' or stu.get_First_name() == '' or stu.get_Last_name() == '' or \
                    stu.get_Gender() == '' or stu.get_Dob() == '' or stu.get_Contact() == '' or \
                    stu.get_Email() == '' or stu.get_Parent_name() == '' or stu.get_Parent_contact() == '' or \
                    stu.get_Address() == '':
                messagebox.showerror('error', 'Please Fill all entries')

            else:
                query = 'insert into student_manage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                values = (
                    stu.get_Student_Id(), stu.get_First_name(), stu.get_Last_name(), stu.get_Gender(), stu.get_Dob(),
                    stu.get_Contact(), stu.get_Email(), stu.get_Parent_name(), stu.get_Parent_contact(),
                    stu.get_Address())

                self.dbconn.insert(query, values)
                self.fetch()
                self.clear_data()

                messagebox.showinfo('Info', 'Data Inserted Successfully!')

        except:
            messagebox.showerror("Error", 'Please insert unique Student Id, Contact, email and Parent Contact!')

    # function for fetching student data from table to entry field
    def fetch(self):
        stu = student_detail(self.stu_ent.get(), self.f_name_ent.get(), self.l_name_ent.get(), self.gender_combo.get(),
                             self.dob_ent.get(), self.contact_ent.get(), self.email_ent.get(), self.par_nm_ent.get(),
                             self.par_con_ent.get(), self.address_ent.get('1.0', tk.END))
        query = 'select * from student_manage'
        rows = self.dbconn.select(query)
        if len(rows) != 0:
            self.Student_table.delete(
                *self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', tk.END, values=row)

    # function for clearing all inserted data in entry field
    def clear_data(self):
        stu = student_detail(self.stu_ent.get(), self.f_name_ent.get(), self.l_name_ent.get(), self.gender_combo.get(),
                             self.dob_ent.get(), self.contact_ent.get(), self.email_ent.get(), self.par_nm_ent.get(),
                             self.par_con_ent.get(), self.address_ent.get('1.0', tk.END))
        self.stu_ent.delete('0', tk.END)
        self.f_name_ent.delete('0', tk.END)
        self.l_name_ent.delete('0', tk.END)
        self.gender_combo.set('')
        self.dob_ent.delete('0', tk.END)
        self.contact_ent.delete('0', tk.END)
        self.email_ent.delete('0', tk.END)
        self.par_nm_ent.delete('0', tk.END)
        self.par_con_ent.delete('0', tk.END)
        self.address_ent.delete('1.0', tk.END)

    # function for updating student data from added one
    def update_data(self):
        stu = student_detail(self.stu_ent.get(), self.f_name_ent.get(), self.l_name_ent.get(), self.gender_combo.get(),
                             self.dob_ent.get(), self.contact_ent.get(), self.email_ent.get(), self.par_nm_ent.get(),
                             self.par_con_ent.get(), self.address_ent.get('1.0', tk.END))
        if stu.get_Student_Id() == '' or stu.get_First_name() == '' or stu.get_Last_name() == '' or \
                stu.get_Gender() == '' or stu.get_Dob() == '' or stu.get_Contact() == '' or stu.get_Email() == '' or \
                stu.get_Parent_name() == '' or stu.get_Parent_contact() == '' or stu.get_Address() == '':
            messagebox.showerror('error', 'Please Fill all entries')
        else:
            query = 'update student_manage set First_name=%s,Last_name=%s, Gender=%s,Dob=%s,Contact=%s,' \
                    'Email=%s,Parent_name=%s,Parent_contact=%s, Address=%s where Student_Id=%s '
            values = (stu.get_First_name(), stu.get_Last_name(), stu.get_Gender(), stu.get_Dob(), stu.get_Contact(),
                      stu.get_Email(), stu.get_Parent_name(), stu.get_Parent_contact(), stu.get_Address(),
                      stu.get_Student_Id())
            self.dbconn.update(query, values)
            self.clear_data()
            self.fetch()
            messagebox.showinfo('Info', 'Data Update Successfully!')

    # function for deleting student data
    def delete_data(self):
        stu = student_detail(self.stu_ent.get(), self.f_name_ent.get(), self.l_name_ent.get(), self.gender_combo.get(),
                             self.dob_ent.get(), self.contact_ent.get(), self.email_ent.get(), self.par_nm_ent.get(),
                             self.par_con_ent.get(), self.address_ent.get('1.0', tk.END))
        if stu.get_Student_Id() == '' or stu.get_First_name() == '' or stu.get_Last_name() == '' or \
                stu.get_Gender() == '' or stu.get_Dob() == '' or stu.get_Contact() == '' or stu.get_Email() == '' or \
                stu.get_Parent_name() == '' or stu.get_Parent_contact() == '' or stu.get_Address() == '':
            messagebox.showerror('error', 'Please select column to delete from table')
        else:
            query = 'delete from student_manage where Student_Id=%s'
            values = (stu.get_Student_Id(),)
            self.dbconn.delete(query, values)
            self.clear_data()
            self.fetch()
            messagebox.showinfo('Info', 'Data Deleted Successfully!')

    # function for show data button
    def show_data(self, ev):
        data_row = self.Student_table.focus()
        content = self.Student_table.item(data_row)
        row = content['values']

        stu = student_detail(self.stu_ent.delete('0', tk.END), self.f_name_ent.delete('0', tk.END),
                             self.l_name_ent.delete('0', tk.END), self.gender_combo.delete('0', tk.END),
                             self.dob_ent.delete('0', tk.END), self.contact_ent.delete('0', tk.END),
                             self.email_ent.delete('0', tk.END), self.par_nm_ent.delete('0', tk.END),
                             self.par_con_ent.delete('0', tk.END), self.address_ent.delete('1.0', tk.END))
        try:
            self.stu_ent.insert(tk.END, row[0])
            self.f_name_ent.insert(tk.END, row[1])
            self.l_name_ent.insert(tk.END, row[2])
            self.gender_combo.set(row[3])
            self.dob_ent.insert(tk.END, row[4])
            self.contact_ent.insert(tk.END, row[5])
            self.email_ent.insert(tk.END, row[6])
            self.par_nm_ent.insert(tk.END, row[7])
            self.par_con_ent.insert(tk.END, row[8])
            self.address_ent.insert(tk.END, row[9])
        except IndexError:
            messagebox.showerror('Warning', 'Please do not click on blank field')

    # ===============================Linear search Algorithm=============================
    # Pseudocode:
    # Step0: Start
    # Step1: Function for merge search is made which is called by class method with argument records, values and index.
    # Step2: Empty list is created for storing search value
    # Step3: For loop is created in the record list
    # Step4: Inside for loop if iterated value in a given index is not string, run another conditional flow
    # Step5: Inside if iterated value in a given index is equal to value then append iterated value to the list
    # Step6: If the condition does not meet iterated value in a given index is converted in capital letter which is
    # then compared to the value
    # Step7: Now append iterated value in empty list
    # Step8: Finally, return rows
    # Step9: Stop

    @classmethod
    def search(cls, records, value, index):
        rows = []
        for item in records:
            if type(item[index]) != str:
                if item[index] == value:
                    rows.append(item)
            else:
                if item[index].upper() == value.upper():
                    rows.append(item)
        return rows

    # search value in linear search
    def search_value(self):
        search_by = self.search_combo.get()
        search_value = self.search_ent.get()
        try:
            search_value = int(search_value)
        except ValueError:
            pass
        if search_by == '' or search_value == '':
            messagebox.showinfo('Sorry', 'Please select all required fields')
        elif search_by == 'Student_Id' and type(search_value) != int:
            messagebox.showinfo('Error', 'values should be integer')
        else:
            query = 'select * from student_manage;'
            records = self.dbconn.select(query)

            if search_by == 'Student_Id':
                rows = student.search(records, search_value, 0)
            elif search_by == 'First_name':
                rows = student.search(records, search_value, 1)
            elif search_by == 'Last_name':
                rows = student.search(records, search_value, 2)
            elif search_by == 'Contact':
                rows = student.search(records, search_value, 5)
            else:
                rows = []
            if len(rows) != 0:
                self.Student_table.delete(
                    *self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', tk.END, values=row)

    # ==========================================Algorithm for merge sorting===============================
    # Pseudocode:
    # Step0: start
    # Step1: Function named merge_sort will be created with two argument records and ascending and set as
    #   boolean value True
    # Step2: Empty list called as item will be created to store final result
    # Step3: check whether the length of listing is equal to one
    # Step4: if condition meets, return listing
    # Step5: if condition does not meet, the length of listing will be divided into two half and store the
    #   value in middle variable
    # Step6: call merge_sort with argument records[:middle] and store in variable first_half
    # Step7: call merge_sort with argument records[middle:] and store in variable second_half
    # Step8: create a two variable x and y having 0 value
    # Step9: while loop will be used to check the whether x and y is greater than length of first_half and
    #   second_half respectively
    # Step10: if value of first_half is greater than second_half, append the second half value to empty list and
    #     increase the value of y with 1
    # Step11: if condition is does not meet, append the value of first_half to empty list and increase the value
    #   of x with 1
    # Step12: Now, set result equal to the sum of result and first_half[x:]
    # Step13: now, set result equal to the sum of result and second_half[y:]
    # Step14: Now, check whether ascending is equal to True or false
    # Step15: if condition meets, return result
    # Step16: if ascending is equal to False, reverse the result and return result
    # Step17: stop
    @classmethod
    def merge_sort(self, listing, ascending=True):
        item = []
        if len(listing) == 1:
            return listing
        middle = len(listing) // 2
        first_half = self.merge_sort(listing[:middle])
        second_half = self.merge_sort(listing[middle:])
        x = 0
        y = 0
        while x < len(first_half) and y < len(second_half):
            # for descending order
            if first_half[x] > second_half[y]:
                item.append(second_half[y])
                y = y + 1
            else:
                item.append(first_half[x])
                x = x + 1
        result = item + first_half[x:]
        result = result + second_half[y:]
        if ascending:
            return result
        else:
            result.reverse()
            return result

    # sorting value in merge sort
    def sort(self):
        sort_by = self.sort_combo.get()
        query = 'select * from student_manage'
        fetch_value = self.dbconn.select(query)
        if sort_by == 'Asc':
            rows = self.merge_sort(fetch_value, True)

        elif sort_by == 'Desc':
            rows = self.merge_sort(fetch_value, False)
        else:
            rows = []
            messagebox.showinfo('Sorry', 'Please select all required fields')
        if len(rows) != 0:  # if length of row is not equal to zero than there will be some data
            self.Student_table.delete(
                *self.Student_table.get_children())  # deleting children element from Student_table
            for row in rows:  # iteration for loop, with this loop we will store the datas from fetch data
                self.Student_table.insert('', tk.END, values=row)

    # function for destroying student class
    def destroy(self):
        self.admission.destroy()
        self.manage_frame.destroy()
        self.button_frame.destroy()
        self.table1_Frame.destroy()
        self.info_frame.destroy()


# calling main class
app = student_manage()
app.mainloop()
