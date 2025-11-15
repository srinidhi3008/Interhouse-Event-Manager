import mysql.connector as mc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkcalendar import *

def SIGNUP():
    winSIGNUP = tk.Tk()
    winSIGNUP.title("Sign up")
    winSIGNUP.geometry("300x350")
    winSIGNUP.configure(background="burlywood2")
    tk.Label(winSIGNUP, text="Enter username (admission no.)", background="burlywood2").place(x=80, y=105)
    username_var = tk.IntVar()
    e1 = tk.Entry(winSIGNUP, textvariable=username_var)
    e1.place(x=90, y=125)
    tk.Label(winSIGNUP, text="Enter password", background="burlywood2").place(x=100, y=145)
    password_var = tk.StringVar()
    e2 = tk.Entry(winSIGNUP, textvariable=password_var, show='*')
    e2.place(x=90, y=165)

    def Confirm():
        username = e1.get()
        password = e2.get()
        try:
            obj = mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur = obj.cursor()
            query = "INSERT INTO cred (username, password) VALUES (%s, %s)"
            cur.execute(query, (username, password))
            obj.commit()
        except mc.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            if obj.is_connected():
                cur.close()
                obj.close()
        info(username)

    def info(username):
        wininfo = tk.Tk()
        wininfo.title("Enter Additional Info")
        wininfo.geometry("300x450")
        wininfo.configure(background="burlywood2")
        tk.Label(wininfo, text="Enter first name", background="burlywood2").place(x=100, y=105)
        fname_var = tk.StringVar()
        e3 = tk.Entry(wininfo, textvariable=fname_var)
        e3.place(x=90, y=125)
        tk.Label(wininfo, text="Enter last name", background="burlywood2").place(x=100, y=145)
        lname_var = tk.StringVar()
        e4 = tk.Entry(wininfo, textvariable=lname_var)
        e4.place(x=90, y=165)
        tk.Label(wininfo, text="Enter class", background="burlywood2").place(x=100, y=185)
        grade_var = tk.IntVar()
        e5 = tk.Entry(wininfo, textvariable=grade_var)
        e5.place(x=90, y=205)
        tk.Label(wininfo, text="Enter section", background="burlywood2").place(x=100, y=225)
        sec_var = tk.StringVar()
        e6 = tk.Entry(wininfo, textvariable=sec_var)
        e6.place(x=90, y=245)
        tk.Label(wininfo, text="Enter house", background="burlywood2").place(x=100,y=265)
        house_var=tk.StringVar()
        e7=tk.Entry(wininfo, textvariable= house_var)
        e7.place(x=90, y=285)
        def enter_info(capt):
            fn = e3.get()
            ln = e4.get()
            gr = e5.get()
            sc = e6.get()
            hs = e7.get()
            obj = mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur = obj.cursor()
            if capt=="Yes":
                q="select * from captains where Admission_No=%s and First_Name=%s and Last_Name=%s and House=%s"
                cur.execute(q, (username,fn,ln,hs))
                data=cur.fetchall()
                if data:
                    cur.close()
                    cur=obj.cursor()
                    q1 = "INSERT INTO info (Admission_no, First_Name, Last_Name, Grade, Section, Captain_vicecaptain, House) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cur.execute(q1, (username, fn, ln, gr, sc, capt, hs))
                    obj.commit()
                    messagebox.showinfo("Success", "Signed up successfully")
                    cur.close()
                    obj.close()
                    wininfo.destroy()
                    winSIGNUP.destroy()
                else:
                    messagebox.showerror("Failed","Please enter valid details")
                    q2="delete from cred where Username=%s"
                    cur.execute(q2,(username,))
                    obj.commit()
                    wininfo.destroy()
            else:
                q1 = "INSERT INTO info (Admission_no, First_Name, Last_Name, Grade, Section, Captain_vicecaptain, House) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur.execute(q1, (username, fn, ln, gr, sc, capt, hs))
                obj.commit()
                messagebox.showinfo("Success", "Signed up successfully")
                cur.close()
                obj.close()
                wininfo.destroy()
                winSIGNUP.destroy()
                
        tk.Label(wininfo, text="Captain/Vice Captain?", background="burlywood2").place(x=100, y=305)
        tk.Button(wininfo, text="Yes", command=lambda: enter_info("Yes"), bg="azure3").place(x=90, y=310)
        tk.Button(wininfo, text="No", command=lambda: enter_info("No"), bg="azure3").place(x=110, y=310)

    tk.Button(winSIGNUP, text="Confirm", command=Confirm).place(x=125, y=195)
    
def admin():
    def register():
        def show(e):
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            q="select First_Name,Last_Name,Grade,House from info where Admission_No=%s"
            cur.execute(q,(username,))
            data=cur.fetchone()
            fname=data[0]
            lname=data[1]
            grade=data[2]
            house=data[3]
            cur.close()
            cur=obj.cursor()
            q2="select * from registrations where Admission_No=%s and Event_Name=%s"
            cur.execute(q2,(username,e))
            data=cur.fetchall()
            if data:
                messagebox.showinfo("","You have already registered")
                winreg.destroy()
            else:
                q1="insert into registrations (First_Name, Last_Name, Grade, Event_Name, Admission_No, House) VALUES (%s, %s, %s, %s, %s, %s)"
                cur.execute(q1, (fname,lname,grade,e,username,house))
                obj.commit()
                messagebox.showinfo("Success", "Registered successfully")
                cur.close()
                obj.close()
                winreg.destroy()
        winreg=tk.Tk()  
        winreg.title("Register Now!")
        winreg.geometry("300x350")
        winreg.configure(background="burlywood2")
        tk.Label(winreg, text="Enter event name", background="burlywood2").place(x=90, y=125)
        ename=tk.StringVar()
        e6=tk.Entry(winreg, textvariable=ename)
        e6.place(x=90, y=145)
        tk.Button(winreg, text="OK",command=lambda: [show(e6.get())],bg="azure3").place(x=100, y=225)  
    def main_search():
        def search():
            ename=entry.get()
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            q="select * from events where Event_Name like %s"
            cur.execute(q, ('%'+ ename +'%',))
            data=cur.fetchall()
            if not data:
                messagebox.showinfo("","Event not found")
                winsearch.destroy()
            if data:
                tree=ttk.Treeview(winsearch)
                tree['show']='headings'
                s=ttk.Style(winsearch)
                s.theme_use("clam")
                s.configure(".",font=('Helvetica', 11))
                s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
                tree["columns"]=("Event_Name","Grades","Prelims_Date","Finals_Date")
                tree.column("Event_Name", width=100, minwidth=100, anchor=tk.CENTER)
                tree.column("Grades", width=100, minwidth=100, anchor=tk.CENTER)    
                tree.column("Prelims_Date", width=100, minwidth=100, anchor=tk.CENTER)
                tree.column("Finals_Date", width=100, minwidth=100, anchor=tk.CENTER)
                tree.heading("Event_Name", text="Event Name")
                tree.heading("Grades", text="Grades")
                tree.heading("Prelims_Date", text="Prelims Date")
                tree.heading("Finals_Date", text="Finals Date")
                for i in data:
                    tree.insert('', 'end', values=(i[0], i[1], i[2], i[3]))
                cur.close()
                obj.close()
                tree.pack()
                hsb=ttk.Scrollbar(winAdmin, orient="horizontal") 
                hsb.configure(command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X, side=BOTTOM)
        winsearch=tk.Tk()
        winsearch.title("Search Events")
        winsearch.geometry("400x300")
        winsearch.configure(background="burlywood2")
        tk.Label(winsearch, text="Enter event name to search", background="burlywood2").place(x=100, y=50)
        entry=tk.Entry(winsearch)
        entry.place(x=100, y=80)
        tk.Button(winsearch, text="Search", command=search, bg="azure3").place(x=160, y=120)

    def main_update():

        def select_pd():
            def get_pd():
                global pdate
                pdate=pcal.get_date()
                wincal.destroy()
            wincal=tk.Tk()
            wincal.title("Select Prelims Date")
            wincal.geometry("300x350")
            pcal=Calendar(wincal, selectmode="day", year=2024, month=11)
            pcal.pack(pady=20)
            tk.Button(wincal, text="Select", command=get_pd, bg="azure3").place(x=130, y=280)

        def select_fd():
            def get_fd():
                global fdate
                fdate=fcal.get_date()
                wincal.destroy()
            wincal=tk.Tk()
            wincal.title("Select Finals Date")
            wincal.geometry("300x350")
            fcal=Calendar(wincal, selectmode="day", year=2024, month=11)
            fcal.pack(pady=20)
            tk.Button(wincal, text="Select", command=get_fd, bg="azure3").place(x=130, y=280)
        
        def update():
            ename=en_entry.get()            
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            q="update events set Prelims_Date=%s, Finals_Date=%s where Event_Name=%s"
            cur.execute(q, (pdate, fdate, ename))
            obj.commit()
            messagebox.showinfo("Success", "Event updated successfully")
            cur.close()
            obj.close()
            winup.destroy()
            winAdmin.destroy()
            admin()
        winup=tk.Tk()
        winup.title("Update Event")
        winup.geometry("400x400")
        winup.configure(background="burlywood2")
        tk.Label(winup, text="Enter event name to update", background="burlywood2").place(x=100, y=50)
        en_entry=tk.Entry(winup)
        en_entry.place(x=100, y=80)
        tk.Button(winup, text="Select Prelims Date", command=select_pd, bg="azure3").place(x=100, y=110)
        tk.Button(winup, text="Select Finals Date", command=select_fd, bg="azure3").place(x=100, y=140)
        tk.Button(winup, text="OK", command=update, bg="azure3").place(x=100, y=170)
    
    def view_house_registrations():
        def see():
            reg=tk.Tk()
            tree=ttk.Treeview(reg)
            tree['show']='headings'
            s=ttk.Style(reg)
            s.theme_use("clam")
            s.configure(".",font=('Helvetica', 11))
            s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
            tree["columns"]=("First_Name","Last_Name","Grade","Event_Name","Admission_No","House")
            tree.column("First_Name", width=200, minwidth=200, anchor=tk.CENTER)
            tree.column("Last_Name", width=200, minwidth=200, anchor=tk.CENTER)    
            tree.column("Grade", width=200, minwidth=200, anchor=tk.CENTER)
            tree.column("Event_Name", width=200, minwidth=200, anchor=tk.CENTER)
            tree.column("Admission_No", width=200,minwidth=200,anchor=tk.CENTER)
            tree.column("House", width=200, minwidth=200, anchor=tk.CENTER)
            tree.heading("First_Name", text="First Name")
            tree.heading("Last_Name", text="Last Name")
            tree.heading("Grade", text="Grade")
            tree.heading("Event_Name", text="Event Name")
            tree.heading("Admission_No", text="Admission No")
            tree.heading("House", text="House")
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            q="select House from captains where Admission_No=%s"
            cur.execute(q,(username,))
            data=cur.fetchone()
            if data:
                house=data[0]
                cur.close()
                obj.close()
                obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
                cur=obj.cursor()
                q2="select * from registrations where house=%s"
                cur.execute(q2,(house,))
                data=cur.fetchall()
                for i in data:
                    tree.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5]))
                tree.pack()
                hsb=ttk.Scrollbar(reg, orient="horizontal") 
                hsb.configure(command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X, side=BOTTOM)
            else:
                messagebox.showerror("Failed","Enter your own admission number")
        see()
    
    def view():
        def delete():
            select=tree.selection()
            if not select:
                messagebox.showwarning("Selection Error", "Please select an event to withdraw from.")
                return
            ename=tree.item(select)['values'][0] 
            confirm=messagebox.askyesno("Withdraw", f"Are you sure you want to withdraw from {ename}?")
            if confirm:
                try:
                    obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
                    cur=obj.cursor()
                    q="delete from registrations where Event_Name = %s and Admission_No=%s"
                    cur.execute(q, (ename,username))
                    obj.commit()
                    messagebox.showinfo("Success", "Withdrawn successfully.")
                    tree.delete(select) 
                except mc.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")
                finally:
                    if obj.is_connected():
                        cur.close()
                        obj.close()
                        see.destroy()
                        view()
        see = tk.Tk()
        see.title("Registered Events")
        see.geometry("500x500")
        see.configure(background="burlywood2")
        tree=ttk.Treeview(see)
        tree['show']='headings'
        s=ttk.Style(see)
        s.theme_use("clam")
        s.configure(".",font=('Helvetica', 11))
        s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
        tree["columns"]=("Event_Name")
        tree.column("Event_Name", width=200, minwidth=200, anchor=tk.CENTER)
        tree.heading("Event_Name", text="Event Name")
        obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
        cur=obj.cursor()
        q="select * from registrations where Admission_No= %s"
        cur.execute(q, (username,))
        data=cur.fetchall()
        for i in data:
            tree.insert('', 'end', values=(i[3],))
        cur.close()
        obj.close()
        tree.pack()
        
        hsb=ttk.Scrollbar(see, orient="horizontal") 
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X, side=BOTTOM)
        tk.Button(see, text="Withdraw", command=delete, bg="azure3").place(x=210, y=350) 

    def add():
        
        def show(n,g,p,f):
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            try:
                q1="insert into events (Event_Name, Grades, Prelims_Date, Finals_Date) values (%s, %s, %s, %s)"
                cur.execute(q1, (n,g,p,f))
                obj.commit()
                messagebox.showinfo("Success", "Added successfully")
                winadd.destroy()
                winAdmin.destroy()
                admin()
            except mc.Error as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                cur.close()
                obj.close()
                winAdmin.destroy()
                admin()
                
        def pdate():
            def getp():
                global p_date
                p_date=cal.get_date()
                wincal.destroy()
            wincal=tk.Tk()
            wincal.geometry("300x350")
            wincal.title("Calendar")
            cal=Calendar(wincal,selectmode="day", year=2024, month=11)
            cal.pack(pady=20)
            tk.Button(wincal, text="OK",command=getp, bg="azure3").place(x=150,y=300)

        def fdate():
            def getf():
                global f_date
                f_date=cal.get_date()
                wincal.destroy()
            wincal=tk.Tk()
            wincal.geometry("300x350")
            wincal.title("Calendar")
            cal=Calendar(wincal,selectmode="day", year=2024, month=11)
            cal.pack(pady=20)
            tk.Button(wincal, text="OK",command=getf, bg="azure3").place(x=150,y=300)
        winadd = tk.Tk()
        winadd.title("Add Event")
        winadd.geometry("300x350")
        winadd.configure(background="burlywood2")
        tk.Label(winadd, text="Enter event name", background="burlywood2").place(x=100, y=105)
        name = tk.StringVar()
        e3 = tk.Entry(winadd, textvariable=name)
        e3.place(x=90, y=125)
        tk.Label(winadd, text="Enter grades", background="burlywood2").place(x=100, y=145)
        grades = tk.StringVar()
        e4 = tk.Entry(winadd, textvariable=grades)
        e4.place(x=90, y=165)
        tk.Button(winadd, text="Select Prelims date",command=pdate, bg="azure3").place(x=100, y=185)
        tk.Button(winadd, text="Select Finals date",command=fdate, bg="azure3").place(x=100, y=225) 
        tk.Button(winadd, text="OK",command=lambda: [show(name.get(), grades.get(), p_date, f_date)],bg="azure3").place(x=100, y=265)
    
    winAdmin = tk.Tk()
    winAdmin.title("Events")
    winAdmin.geometry("1000x1000")
    winAdmin.configure(background="burlywood2")
    
    tree=ttk.Treeview(winAdmin)
    tree['show']='headings'
    s=ttk.Style(winAdmin)
    s.theme_use("clam")
    s.configure(".",font=('Helvetica', 11))
    s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
    tree["columns"]=("Event_Name","Grades","Prelims_Date","Finals_Date")
    tree.column("Event_Name", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("Grades", width=200, minwidth=200, anchor=tk.CENTER)    
    tree.column("Prelims_Date", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("Finals_Date", width=200, minwidth=200, anchor=tk.CENTER)
    tree.heading("Event_Name", text="Event Name")
    tree.heading("Grades", text="Grades")
    tree.heading("Prelims_Date", text="Prelims Date")
    tree.heading("Finals_Date", text="Finals Date")
    
    obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
    cur=obj.cursor()
    q1="select * from events;"
    cur.execute(q1)
    data=cur.fetchall()
    for row in data:
        tree.insert('','end',text="",values=(row[0],row[1],row[2],row[3]))
    tree.pack()
    hsb=ttk.Scrollbar(winAdmin, orient="horizontal") 
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    tk.Button(winAdmin, text="Add Event", command=add, bg="azure3").place(x=500, y=500)
    tk.Button(winAdmin, text="Search Events", command=main_search, bg="azure3").place(x=500, y=550)
    tk.Button(winAdmin, text="Update Event", command=main_update, bg="azure3").place(x=500, y=600)
    tk.Button(winAdmin, text="View House Registrations", command=view_house_registrations, bg="azure3").place(x=500, y=650)
    tk.Button(winAdmin, text="Register", command=register, bg="azure3").place(x=500, y=700)
    tk.Button(winAdmin, text="View Your Registrations", command=view, bg="azure3").place(x=500, y=750)


def student():
    def register():
        def show(e):
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            q="select First_Name,Last_Name,Grade,House from info where Admission_No=%s"
            cur.execute(q,(username,))
            data=cur.fetchone()
            fname=data[0]
            lname=data[1]
            grade=data[2]
            house=data[3]
            cur.close()
            cur=obj.cursor()
            q2="select * from registrations where Admission_No=%s and Event_Name=%s"
            cur.execute(q2,(username,e))
            data=cur.fetchall()
            if data:
                messagebox.showinfo("","You have already registered")
                winreg.destroy()
            else:
                q1="insert into registrations (First_Name, Last_Name, Grade, Event_Name, Admission_No, House) VALUES (%s, %s, %s, %s, %s, %s)"
                cur.execute(q1, (fname,lname,grade,e,username,house))
                obj.commit()
                messagebox.showinfo("Success", "Registered successfully")
                cur.close()
                obj.close()
                winreg.destroy()
        winreg=tk.Tk()  
        winreg.title("Register Now!")
        winreg.geometry("300x350")
        winreg.configure(background="burlywood2")
        tk.Label(winreg, text="Enter event name", background="burlywood2").place(x=90, y=125)
        ename=tk.StringVar()
        e6=tk.Entry(winreg, textvariable=ename)
        e6.place(x=90, y=145)
        tk.Button(winreg, text="OK",command=lambda: [show(e6.get())],bg="azure3").place(x=100, y=225)        

    def view():
        def delete():
            select=tree.selection()
            if not select:
                messagebox.showwarning("Selection Error", "Please select an event to withdraw from.")
                return
            ename=tree.item(select)['values'][0] 
            confirm=messagebox.askyesno("Withdraw", f"Are you sure you want to withdraw from {ename}?") 
            if confirm:
                try:
                    obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
                    cur=obj.cursor()
                    q="delete from registrations where Event_Name = %s and Admission_No=%s"
                    cur.execute(q, (ename,username))
                    obj.commit()
                    messagebox.showinfo("Success", "Withdrawn successfully.")
                    tree.delete(select)
                except mc.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")
                finally:
                    if obj.is_connected():
                        cur.close()
                        obj.close()
                        see.destroy()
                        view()
        see = tk.Tk()
        see.title("Registered Events")
        see.geometry("500x500")
        see.configure(background="burlywood2")
        tree=ttk.Treeview(see)
        tree['show']='headings'
        s=ttk.Style(see)
        s.theme_use("clam")
        s.configure(".",font=('Helvetica', 11))
        s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
        tree["columns"]=("Event_Name")
        tree.column("Event_Name", width=200, minwidth=200, anchor=tk.CENTER)
        tree.heading("Event_Name", text="Event Name")
        obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
        cur=obj.cursor()
        q="select * from registrations where Admission_No= %s"
        cur.execute(q, (username,))
        data=cur.fetchall()
        for i in data:
            tree.insert('', 'end', values=(i[3],))
        cur.close()
        obj.close()
        tree.pack()
        hsb=ttk.Scrollbar(see, orient="horizontal") 
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X, side=BOTTOM)
        tk.Button(see, text="Withdraw", command=delete, bg="azure3").place(x=210, y=350) 
          
    def main_search():
        def search():
            ename=entry.get()
            obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
            cur=obj.cursor()
            q="select * from events where Event_Name like %s"
            cur.execute(q, ('%'+ ename +'%',))
            data=cur.fetchall()
            if not data:
                messagebox.showinfo("","Event not found")
                winsearch.destroy()
            if data:
                tree=ttk.Treeview(winsearch)
                tree['show']='headings'
                s=ttk.Style(winsearch)
                s.theme_use("clam")
                s.configure(".",font=('Helvetica', 11))
                s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
                tree["columns"]=("Event_Name","Grades","Prelims_Date","Finals_Date")
                tree.column("Event_Name", width=100, minwidth=100, anchor=tk.CENTER)
                tree.column("Grades", width=100, minwidth=100, anchor=tk.CENTER)    
                tree.column("Prelims_Date", width=100, minwidth=100, anchor=tk.CENTER)
                tree.column("Finals_Date", width=100, minwidth=100, anchor=tk.CENTER)
                tree.heading("Event_Name", text="Event Name")
                tree.heading("Grades", text="Grades")
                tree.heading("Prelims_Date", text="Prelims Date")
                tree.heading("Finals_Date", text="Finals Date")
                for i in data:
                    tree.insert('', 'end', values=(i[0], i[1], i[2], i[3]))
                cur.close()
                obj.close()
                tree.pack()
                hsb=ttk.Scrollbar(winstud, orient="horizontal") 
                hsb.configure(command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X, side=BOTTOM)
        winsearch=tk.Tk()
        winsearch.title("Search Events")
        winsearch.geometry("400x300")
        winsearch.configure(background="burlywood2")
        tk.Label(winsearch, text="Enter event name to search", background="burlywood2").place(x=100, y=50)
        entry=tk.Entry(winsearch)
        entry.place(x=100, y=80)
        tk.Button(winsearch, text="Search", command=search, bg="azure3").place(x=160, y=120)        
    winstud=tk.Tk()
    winstud.title("Events")
    winstud.geometry("1000x1000")
    winstud.configure(background="burlywood2")
    tree=ttk.Treeview(winstud)
    tree['show']='headings'
    s=ttk.Style(winstud)
    s.theme_use("clam")
    s.configure(".",font=('Helvetica', 11))
    s.configure("Treeview.Heading", foregroud='red',font=('Helvetica', 11, "bold"))
    tree["columns"]=("Event_Name","Grades","Prelims_Date","Finals_Date")
    tree.column("Event_Name", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("Grades", width=200, minwidth=200, anchor=tk.CENTER)    
    tree.column("Prelims_Date", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("Finals_Date", width=200, minwidth=200, anchor=tk.CENTER)
    tree.heading("Event_Name", text="Event Name")
    tree.heading("Grades", text="Grades")
    tree.heading("Prelims_Date", text="Prelims Date")
    tree.heading("Finals_Date", text="Finals Date")
    obj=mc.connect(host="localhost", user="root", password="sql123", database="school")
    cur=obj.cursor()
    q1="select * from events;"
    cur.execute(q1)
    data=cur.fetchall()
    for row in data:
        tree.insert('','end',text="",values=(row[0],row[1],row[2],row[3]))
    tree.pack()
    hsb=ttk.Scrollbar(winstud, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    tk.Button(winstud, text="Register", command=register, bg="azure3").place(x=500, y=600)
    tk.Button(winstud, text="Search Events", command=main_search, bg="azure3").place(x=500, y=650)
    tk.Button(winstud, text="View your registrations", command=view, bg="azure3").place(x=500, y=700)

def checkCred():
    global username
    username=e1.get()
    pwd=e2.get()
    
    try:
        obj=mc.connect(host="localhost",user="root",password="sql123",database="school")
        cur=obj.cursor()
        
        q1="select password from cred where username = %s"
        cur.execute(q1, (username,))
        data=cur.fetchone() 

        if data:
            db_password = data[0]
            if db_password == pwd:
                q2="select Captain_vicecaptain from info where Admission_no=%s"
                cur.execute(q2,(username,))
                role=cur.fetchone()
                
                if role and role[0]=="Yes":
                    admin()
                    win.destroy()
                elif role and role[0]=="No":
                    student()
                    win.destroy()
                else:
                    messagebox.showerror("Login Error", "User data incomplete. Please contact admin.")
            else:
                messagebox.showinfo("Fail","Incorrect password")
        else:
            messagebox.showinfo("Fail","Username doesn't exist")

    except mc.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        if 'obj' in locals() and obj.is_connected():
            cur.close()
            obj.close()

win=tk.Tk()
win.geometry('500x500')
try:
    bg=PhotoImage(file="logo.png")
    label1=Label(win, image=bg) 
    label1.place(x=125, y=135) 
except tk.TclError:
    print("Warning: logo.png not found. Skipping background image.")

L1=tk.Label(win, text="NPS HSR Interhouse Events",fg="blue4",font=("Helvetica",20)).place(x=75, y=75)
win.title("NPS HSR")
username_var=tk.StringVar() 
l1=tk.Label(win,text="Enter username (admission no.)",fg="blue4",bg="white",font=("Helvetica",16)).place(x=140,y=105)
e1=tk.Entry(win, textvariable=username_var) 
e1.place(x=170,y=140,width=150,height=30)

pwd_var=tk.StringVar() 
l2=tk.Label(win,text="Enter password",fg="blue4",bg="white",font=("Helvetica",16)).place(x=160,y=180)
e2=tk.Entry(win,show="*", textvariable=pwd_var) 
e2.place(x=170,y=220,width=150,height=30)

b=tk.Button(win, text="Log In", command=checkCred, bg="azure2").place(x=220,y=260)
b2=tk.Button(win, text="Sign Up", command=SIGNUP, bg="azure2").place(x=220.5,y=300)

win.mainloop()
