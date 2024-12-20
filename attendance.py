from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ============= variables=============
        self.var_atten_id = StringVar()
        self.var_name = StringVar()
        self.var_rollno = StringVar()
        self.var_date = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_atten = StringVar()

        img1 = Image.open(r"college_images\sa.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=800, height=200)

        img2 = Image.open(r"college_images\clg.jpg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=800, y=0, width=800, height=200)

        img3 = Image.open(r"college_images\bgimg.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="Grey", fg="Black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1500, height=600)

        Left_frame = LabelFrame(main_frame, bd=2, bg="Silver", relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="Silver")
        left_inside_frame.place(x=3, y=135, width=720, height=370)

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"),
                                   bg="Silver")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        rollLabel = Label(left_inside_frame, text="Roll:", bg="Silver", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_rollno, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # ```python
        # Name
        nameLabel = Label(left_inside_frame, text="Name:", bg="Silver", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_name, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", bg="Silver", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel = Label(left_inside_frame, text="Time:", bg="Silver", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_time, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", bg="Silver", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_date, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", bg="Silver", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ["Status", "Present", "Absent"]
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="Silver")
        btn_frame.place(x=0, y=300, width=715, height=50)  # Increased height

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="Grey", fg="Black")
        save_btn.grid(row=0, column=0, padx=5, pady=5)

        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="Grey", fg="Black")
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        delete_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="Grey", fg="Black")
        delete_btn.grid(row=0, column=2, padx=5, pady=5)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="Grey", fg="Black")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)

        # Right side frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="Silver", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=740, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="Silver")
        table_frame.place(x=5, y=5, width=725, height=455)

        # ==================scrollbar table=====================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=150)
        self.AttendanceReportTable.column("roll", width=150)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=150)
        self.AttendanceReportTable.column("time", width=150)
        self.AttendanceReportTable.column("date", width=150)
        self.AttendanceReportTable.column("attendance", width=150)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data to Export!", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_rollno.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_atten.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten.set("")

    def update_data(self):
        cursor_row = self.AttendanceReportTable.focus()
        if not cursor_row:
            messagebox.showerror("Error", "Select a record to update!", parent=self.root)
            return

        content = self.AttendanceReportTable.item(cursor_row)
        selected_row = content['values']

        if messagebox.askyesno("Confirm Update", "Are you sure you want to update this record?", parent=self.root):
            selected_row[1] = self.var_rollno.get()
            selected_row[2] = self.var_name.get()
            selected_row[3] = self.var_dep.get()
            selected_row[4] = self.var_time.get()
            selected_row[5] = self.var_date.get()
            selected_row[6] = self.var_atten.get()

            self.AttendanceReportTable.item(cursor_row, values=selected_row)
            messagebox.showinfo("Data Updated", "The record has been updated successfully!", parent=self.root)
        else:
            messagebox.showinfo("Update Cancelled", "The update has been cancelled!", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()