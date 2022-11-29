from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Registration System")
        self.root.geometry("1350x700+0+0")
        
        title = Label(self.root,text = "Student Registration System",font=("Ubuntu",40,"bold",),bd=10,relief=GROOVE,bg="#5bccf6",fg="red")
        title.pack(side=TOP,fill=X)

        # # # ALL Variables # # #  

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # MANAGE FRAME #
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ef9273")
        Manage_Frame.place(x=20,y=100,width=455,height=590)

        m_title = Label(Manage_Frame,text = "Manage Students ", bg="#ef9273",fg="white",font=("Ubuntu",25,"bold"))
        m_title.grid(row=0,columnspan =2,pady=4)

        lbl_roll = Label(Manage_Frame,text = "Roll No: ", bg = "#ef9273",fg="white",font=("Ubuntu",20,"bold"))
        lbl_roll.grid(row=1,column =0,pady=10,padx = 20,sticky="w")

        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("Ubuntu",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column =1,pady=10,padx = 20,sticky="w")

        lbl_name = Label(Manage_Frame,text = "Name :",bg = "#ef9273",fg="white", font=("Ubuntu",20,"bold"))
        lbl_name.grid(row=2,column =0,pady=10,padx = 20,sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.name_var,font=("Ubuntu",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column =1,pady=10,padx = 20,sticky="w")
        
        lbl_email = Label(Manage_Frame,text = "Email :",bg = "#ef9273",fg="white",font=("Ubuntu",20,"bold"))
        lbl_email.grid(row=3,column =0,pady=10,padx = 20,sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font=("Ubuntu",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column =1,pady=10,padx = 20,sticky="w")

        lbl_gender = Label(Manage_Frame,text = "Gender :",bg = "#ef9273",fg = "white",font=("Ubuntu",20,"bold"))
        lbl_gender.grid(row=4,column =0,pady=10,padx = 20,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("Ubuntu",13,"bold"),state='readonly')
        combo_gender['values'] = ["Male","Female","Other"]
        combo_gender.grid(row = 4,column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_Frame,text = "Contact :",bg = "#ef9273",fg = "white", font=("Ubuntu",20,"bold"))
        lbl_contact.grid(row = 5,column=0,pady =10,padx =20,sticky = "W")

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("Ubuntu",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column =1,pady=10,padx = 20,sticky="w")

        lbl_dob = Label(Manage_Frame,text = "DOB :",bg = "#ef9273",fg = "white", font=("Ubuntu",20,"bold"))
        lbl_dob.grid(row = 6,column=0,pady =10,padx =20,sticky = "W")

        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var,font=("Ubuntu",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address = Label(Manage_Frame,text = "Address :",bg = "#ef9273",fg = "white", font=("Ubuntu",20,"bold"))
        lbl_address.grid(row = 7,column=0,pady =10,padx =20,sticky = "W")

        self.txt_address = Text(Manage_Frame,width=25,height=2.7)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        # # # Button Frame # # #

        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#ef9273")
        btn_Frame.place(x=10,y=500,width=410)

        Addbtn = Button(btn_Frame,text= "Add",width=10,command=self.add_students)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)
        
        updatebtn = Button(btn_Frame,command=self.update_data,text= "Update",width=10)
        updatebtn.grid(row=0,column=1,padx=10,pady=10)
        
        deletebtn = Button(btn_Frame,command=self.delete_data,text= "Delete",width=10)
        deletebtn.grid(row=0,column=2,padx=10,pady=10)
        
        clearbtn = Button(btn_Frame,command=self.clear,text= "Clear ",width=10)
        clearbtn.grid(row=0,column=3,padx=10,pady=10)

        # # # Detail Frame # # #
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ef9273")
        Detail_Frame.place(x=500,y=100,width=830,height=590)

        lbl_search = Label(Detail_Frame,text = "Search By",bg = "#ef9273",fg = "white", font=("Ubuntu",20,"bold"))
        lbl_search.grid(row = 0,column=0,pady =10,padx =20,sticky = "W")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("Ubuntu",13,"bold"),state='readonly')
        combo_search['values'] = ["Name","Roll_No","DOB","Contact"]
        combo_search.grid(row = 0,column=1,padx=20,pady=10)


        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,font=("Ubuntu",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn = Button(Detail_Frame,command=self.search_data,pady=5,text= "Search ",width=10)
        searchbtn.grid(row=0,column=3,padx=10,pady=10)
        
        showallbtn = Button(Detail_Frame,pady=5,command=self.fetch_data,text= "Show All",width=10)
        showallbtn.grid(row=0,column=4,padx=10,pady=10)

        # sortbtn = Button(Detail_Frame,pady=5,command=self.sort_data,text= "Sort",width=5)
        # sortbtn.grid(row=0,column=5,padx=10,pady=10)


        # # # Table Frame # # # 

        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#ef9273")
        Table_Frame.place(x=10,y=70,width=800,height=500) 

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("Roll NO","Name","Email","Gender","Contact","DOB","Address"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll NO",text="Roll NO")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        

        # # # Functionality and Validation # # #


    def add_students(self):
        if(self.Roll_No_var.get()=="" or self.name_var.get()==""):
            messagebox.showerror("Error","All feilds are empty")
        elif("@gmail.com" not in self.email_var.get()):
            messagebox.showerror("Error","Incorrect E-mail Format!")    
        else:
            con=pymysql.connect(host = "localhost",user="root",password="",database="gajanan")
            cur = con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Values Inserted!")

    def fetch_data(self):
        con=pymysql.connect(host = "localhost",user="root",password="",database="gajanan")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host = "localhost",user="root",password="",database="gajanan")
        cur = con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END),
                                                                        self.Roll_No_var.get()
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con=pymysql.connect(host = "localhost",user="root",password="",database="gajanan")
        cur = con.cursor()
        cur.execute("delete from student where roll_no = %s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        if(self.search_txt.get()==""):
            messagebox.showerror("ERROR","Feild is empty!")
        else:    
            con=pymysql.connect(host = "localhost",user="root",password="",database="gajanan")
            cur = con.cursor()
            cur.execute("select * from student where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall() 
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()

    # def sort_data(self):
    #     con=pymysql.connect(host = "localhost",user="root",password="",database="gajanan")
    #     cur = con.cursor()
    #     cur.execute("SELECT * FROM student WHERE DATE(%s) > 2022 order by %s ASC ", self.name_var.get())
    #     rows = cur.fetchall() 
    #     if len(rows) != 0:
    #         self.Student_table.delete(*self.Student_table.get_children())
    #         for row in rows:
    #             self.Student_table.insert('',END,values=row)
    #         con.commit()
    #     con.close() 



root = Tk()
ob = Student(root)

root.mainloop()