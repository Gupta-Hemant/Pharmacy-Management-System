from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector
import pyttsx3
import cv2
from tkvideo import tkvideo
from pyzbar.pyzbar import decode
from tkinter import filedialog
import os


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.state('zoomed')
        
        self.engine = pyttsx3.init()

        # Variable declaration
        self.addmed_var = StringVar()
        self.refMed_var = StringVar()
        
        # Main variable 
    
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        # Top frame
        lbltitle = Label(self.root, text=" PHARAMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                         bg='white', fg='darkgreen', font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        # Logo
        img1 = Image.open("D:\\MAJOR PROJECT\ṇ\Logo.jpg")
        img1 = img1.resize((75, 65), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0, command=self.say_hello)
        b1.place(x=50, y=25)

        # DataFrame
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1530, height=400)

        # Add Medicine Frame
        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information",
                                   fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        self.root.after(1500, self.speak_text, "Welcome to Pharmacy Management System")

        # Button Frame
        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=500, width=1530, height=65)

        # Main buttons
        btnAddData = Button(ButtonFrame, command=self.add_data ,text="Add Medicine", font=("arial", 12, "bold"), width=10 , bg="darkgreen", fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnUpdateMed=Button(ButtonFrame,text="UPDATE", command=self.update , font=("arial", 13, "bold"), width=10,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0, column=1)
      
        btnDeleteMed=Button(ButtonFrame, text="DELETE", command=self.delete , font=("arial", 13, "bold"), width=10,bg="red", fg="white")
        btnDeleteMed.grid(row=0, column=2)
      
        btnRestMed=Button(ButtonFrame, command=self.reset, text="RESET", font=("arial", 13, "bold"), width=10, bg="darkgreen", fg="white")
        btnRestMed.grid(row=0, column=3)
      
        btnExitMed=Button(ButtonFrame,command=self.exit_application , text="EXIT", font=("arial", 13, "bold"), width=10, bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4)
        
        #========================Search By=========================================================================
      
        lblSearch=Label(ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)
        
        self.search_var=StringVar()
        serch_combo=ttk. Combobox (ButtonFrame, textvariable=self.search_var ,width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo["values"]=("Select Option","refno","Medname", "Lot")
        serch_combo.grid(row=0, column=6)
        serch_combo.current(0)
        
        self.serchTxt_var=StringVar()
        txtSerch=Entry(ButtonFrame, textvariable=self.serchTxt_var, bd=3, relief=RIDGE, width=11, font=("arial", 17, "bold"))
        txtSerch.grid(row=0, column=7)
      
        searchBtn=Button(ButtonFrame, command=self.search_data, text="SEARCH", font=("arial", 13, "bold"), width=9, bg="darkgreen", fg="white")
        searchBtn.grid(row=0, column=8)
        
        btnScanQR = Button(ButtonFrame, text="SCAN SEARCH", command=self.scan_qr_codes, font=("arial", 13, "bold"), width=12, bg="darkgreen", fg="white")
        btnScanQR.grid(row=0, column=9)

        showAll=Button(ButtonFrame, command=self.fatch_data ,text="SHOW ALL", font=("arial", 13, "bold"), width=9, bg="darkgreen", fg="white")
        showAll.grid(row=0, column=10) 
        
        btnGenerateBill = Button(ButtonFrame, text="GENERATE BILL", command=self.generate_bill,
                                 font=("arial", 12, "bold"), width=13, bg="darkgreen", fg="white")
        btnGenerateBill.grid(row=0,column=11)
 
    #===================Label and entry=========================================================================
      
        lblrefno=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox (DataFrameLeft, textvariable=self.ref_var , width=27, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)  

        lblCmpName=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name:", padx=2, pady=6)
        lblCmpName.grid(row=1, column=0, sticky=W)
        
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtCmpName.grid(row=1, column=1)
        
        lblTypeofMedicine=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Type of Medicine", padx=2, pady=6)
        lblTypeofMedicine.grid(row=2, column=0, sticky=W)
        comTypeofMedicine=ttk.Combobox (DataFrameLeft, textvariable=self.typeMed_var ,state="readonly",
                                                            font=("arial", 12, "bold"),width=27)

        comTypeofMedicine ['value']=("Tablet", "Liquid", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2, column=1)

        #===================Add Medicine========================================================================= 

        lblMedicineName=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2, pady=6)
        lblMedicineName.grid(row=3, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()
        
        comMedicineName=ttk.Combobox(DataFrameLeft, textvariable=self.medName_var ,state="readonly",
                                                     font=("arial", 12, "bold"), width=27)
        comMedicineName['value']=med
        comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)

        lblLotNo=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo=Entry (DataFrameLeft, textvariable=self.lot_var , font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtLotNo.grid(row=4, column=1)

        lblIssueDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:",padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate=Entry (DataFrameLeft, textvariable=self.issuedate_var , font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtIssueDate.grid(row=5, column=1)

        lblExDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExDate=Entry (DataFrameLeft, textvariable=self.expdate_var , font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses: ", padx=2, pady=4)
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses=Entry (DataFrameLeft, textvariable=self.uses_var , font=("arial", 13, "bold"),bg="white", bd=2, relief=RIDGE, width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0,sticky=W)
        txtSideEffect=Entry (DataFrameLeft, textvariable=self.sideEffect_var , font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtSideEffect.grid(row=8, column=1)

        lblPrecwarning=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Prec&warning:", padx=15)
        lblPrecwarning.grid(row=0, column=2, sticky=W)
        txtPrecwarning=Entry (DataFrameLeft, textvariable=self.warning_var , font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrecwarning.grid(row=0, column=3)

        lblDosage=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:", padx=15,pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage=Entry (DataFrameLeft, textvariable=self.dosage_var , font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtDosage.grid(row=1, column=3)

        lblPrice=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablets Price:", padx=15,pady=6)
        lblPrice.grid(row=2, column=2, sticky=W)
        txtPrice=Entry (DataFrameLeft, textvariable=self.price_var , font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrice.grid(row=2, column=3)

        lblProductQt=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Product QT:", padx=15, pady=6)
        lblProductQt.grid(row=3, column=2, sticky=W)
        txtProductQt=Entry (DataFrameLeft, textvariable=self.product_var , font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtProductQt.grid(row=3, column=3, sticky=W)    
        
    #===================Images=========================================================================
        
        lblhome=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Stay Home Stay Safe:", padx=2, pady=6,bg="white",fg="red",width=44)
        lblhome.place(x=410,y=140)

        img2=Image.open("D:\\MAJOR PROJECT\\img-3.webp")
        img2=img2.resize((150,135), Image.LANCZOS)
        self.photoimg2=ImageTk. PhotoImage (img2)
        b1=Button(self.root, command=self.speak_message, image=self.photoimg2, borderwidth=0)
        b1.place(x=770,y=330)

        img3=Image.open("D:\\MAJOR PROJECT\\img-4.jpg")
        img3=img3.resize((150,135), Image.LANCZOS)
        self.photoimg3=ImageTk. PhotoImage(img3)
        b1=Button(self.root, command=self.speak_message, image=self.photoimg3, borderwidth=0)
        b1.place(x=620,y=330)

        img4=Image.open("D:\\MAJOR PROJECT\\img-5.jpg")
        img4=img4.resize((150,135), Image.LANCZOS)
        self.photoimg4=ImageTk. PhotoImage (img4)
        b1=Button(self.root, command=self.speak_message, image=self.photoimg4, borderwidth=0)
        b1.place(x=475,y=330)


        # DataFrameRight
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="New Medicine Add Department",
                                    fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)
        
        img5=Image.open("D:\\MAJOR PROJECT\\img-8.jpg")
        img5=img5.resize((200,75), Image.LANCZOS)
        self.photoimg5=ImageTk. PhotoImage(img5)
        b1=Button(self.root, command=self.speak_medicine, image=self.photoimg5, borderwidth=0)
        b1.place(x=960,y=160)

        img6=Image.open("D:\\MAJOR PROJECT\\img-7.jpg")
        img6=img6.resize((200,75), Image.LANCZOS)
        self.photoimg6=ImageTk. PhotoImage (img6)
        b1=Button(self.root, command=self.speak_medicine, image=self.photoimg6, borderwidth=0)
        b1.place(x=1160,y=160)
        
        self.cap = cv2.VideoCapture("videoplayback.mp4")  # Replace this with your video file path

        # Create a frame to contain the video
        self.video_frame = tk.Frame(self.root, width=195, height=110)
        self.video_frame.place(x=1270, y=160)

        # Create a canvas to display the video
        self.canvas = tk.Canvas(self.video_frame, width=195, height=110)
        self.canvas.pack()

        # Update the video on the canvas
        self.update_video()
        
        # Update the video on the canvas
        self.update_video()

        #img7=Image.open("D:\Major Project\img-2.jpg")
        #img7=img7.resize((200, 145), Image. ANTIALIAS)
        #self.photoimg7=ImageTk. PhotoImage(img7)
        #b1=Button(self.root, command=self.speak_medicine, image=self.photoimg7, borderwidth=0)
        #b1.place(x=1270,y=160)

        # Reference No
        lblrefno = Label(DataFrameRight, font=("arial", 12, "bold"), text="Reference No: ")
        lblrefno.place(x=0, y=80)
        txtrefno = Entry(DataFrameRight, textvariable=self.refMed_var, font=("arial", 15, "bold"), bg="white", bd=2,
                         relief=RIDGE, width=14)
        txtrefno.place(x=135, y=80)

        # Medicine Name
        lblmedName = Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name: ")
        lblmedName.place(x=0, y=110)
        txtmedName = Entry(DataFrameRight, textvariable=self.addmed_var, font=("arial", 15, "bold"), bg="white",
                           bd=2, relief=RIDGE, width=14)
        txtmedName.place(x=135, y=110)
        
        #========================side frame=========================================================================
        
        side_frame=Frame (DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0,y=150, width=290, height=160)

        sc_x=ttk.Scrollbar (side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y=ttk.Scrollbar (side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table=ttk.Treeview(side_frame, column=("ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack (fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        # Add Medicine Button
        
        down_frame=Frame(DataFrameRight,bd=7, relief=RIDGE, bg="darkgreen")
        down_frame.place (x=330,y=115, width=153, height=200)
        
        btnScanQR = Button(down_frame, text="SCAN REF QR", command=self.scan_qr_code, font=("arial", 12, "bold"), width=13, bg="blue", fg="white", pady=2)
        btnScanQR.grid(row=0, column=0)
        
        btnAddmed=Button(down_frame,command=self.AddMed, text="ADD", font=("arial", 12, "bold"), width=13, bg="lime", fg="white", pady=4)
        btnAddmed.grid(row=1, column=0)
        
        btnUpdatemed=Button (down_frame, command=self.UpdateMed , text="UPDATE", font=("arial", 12, "bold"), width=13, bg="purple", fg="white", pady=4)
        btnUpdatemed.grid(row=2, column=0)
        
        btnDeletemed=Button (down_frame, command=self.DeleteMed , text="DELETE", font=("arial", 12, "bold"), width=13,bg="red", fg="white", pady=4)
        btnDeletemed.grid(row=3, column=0)
        
        btnClearmed=Button (down_frame, command=self.ClearMed , text="CLEAR", font=("arial", 12, "bold"), width=13,bg="orange", fg="white",pady=2)
        btnClearmed.grid(row=4, column=0)
  
        #========================Frame Details=========================================================================
        
        Framedeatils=Frame(self.root, bd=15, relief=RIDGE)
        Framedeatils.place (x=0,y=580, width=1530,height=210)
        
        #========================Main Table & scrollbar=================================================================
        
        Table_frame=Frame (Framedeatils, bd=15, relief=RIDGE, padx=20)
        Table_frame.place (x=0,y=1, width=1500, height=180)

        scroll_x=ttk.Scrollbar (Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=ttk.Scrollbar (Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table=ttk. Treeview (Table_frame, column=("reg","companyname", "type", "tabletname","lotno","issuedate",
                                                       "expdate", "uses","sideeffect", "warning", "dosage", "price", "productqt")
                                                       ,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot No")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect")
        self.pharmacy_table.heading("warning", text="Prec&Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqt", text="Product Qts")
        self.pharmacy_table.pack (fill=BOTH, expand=1)

        self.pharmacy_table.column("reg", width=100)
        self.pharmacy_table.column("companyname", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tabletname", width=100)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffect", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqt", width=100)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    #========================Add Medicne and Functionality Declaration==============================================
    
    def AddMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                                        self.refMed_var.get(),
                                                                        self.addmed_var.get(),   
                                                                        ))
        conn.commit()
        self.fetch_dataMed()
        #self.Medget_cursor()
        self.ref_var.set(self.refMed_var.get())
        self.medName_var.set(self.addmed_var.get())
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")
        
        
    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END,values=i)
        conn.commit()
        conn.close()
        
    #========================MedGetCursor==============================================
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])
    
    def UpdateMed(self):
        if self.refMed_var.get() =="" or self.addmed_var.get() =="":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                    self.addmed_var.get(),
                                                    self.refMed_var.get(),
                                                ))
            my_cursor.execute("update pharma set Ref=%s where MedName=%s",(
                                                    self.refMed_var.get(),
                                                    self.addmed_var.get(),      
            ))
            conn.commit()
            self.fetch_dataMed()
            self.ref_var.set(self.refMed_var.get())
            self.medName_var.set(self.addmed_var.get())
            conn.close()
            
            messagebox.showinfo("Success","Medicine has been updated")
            
    def DeleteMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        
        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql, val)
        
        conn.commit()
        self.fetch_dataMed()
        #self.ref_var.set(self.refMed_var.get())
        #self.medName_var.set(self.addmed_var.get())
        conn.close()
        
        messagebox.showinfo("Delete","Info deleted successfully")
        
    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
        
    #========================Main Table==============================================
    
    def add_data(self):
        if self.ref_var.get() =="" or self.lot_var.get() =="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.ref_var.get(),
                                                                                            self.cmpName_var.get(),
                                                                                            self.typeMed_var.get(),
                                                                                            self.medName_var.get(),
                                                                                            self.lot_var.get(),
                                                                                            self.issuedate_var.get(),
                                                                                            self.expdate_var.get(),
                                                                                            self.uses_var.get(),
                                                                                            self.sideEffect_var.get(),
                                                                                            self.warning_var.get(),
                                                                                            self.dosage_var.get(),
                                                                                            self.price_var.get(),
                                                                                            self.product_var.get()
                                                                                            
                                                                                            
                                                                                            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","data has been inserted")
            
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for i in row:
            self.pharmacy_table.insert("",END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        
        
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row [1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row [3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row [5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row [8]),
        self.warning_var.set(row [9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row [11]),
        self.product_var.set(row[12])
        
    def update(self):
        if self.ref_var.get() =="" or self.lot_var.get() =="":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s, type=%s, medname=%s, lot=%s, issuedate=%s, expdate=%s, uses=%s, sideeffect=%s, warning=%s, dosge=%s, price=%s, product=%s where refno=%s",(
                                                                                            
                                                                                                                                                                                                            self.cmpName_var.get(),
                                                                                                                                                                                                            self.typeMed_var.get(),
                                                                                                                                                                                                            self.medName_var.get(),
                                                                                                                                                                                                            self.lot_var.get(),
                                                                                                                                                                                                            self.issuedate_var.get(),
                                                                                                                                                                                                            self.expdate_var.get(),
                                                                                                                                                                                                            self.uses_var.get(),
                                                                                                                                                                                                            self.sideEffect_var.get(),
                                                                                                                                                                                                            self.warning_var.get(),
                                                                                                                                                                                                            self.dosage_var.get(),
                                                                                                                                                                                                            self.price_var.get(),
                                                                                                                                                                                                            self.product_var.get(),
                                                                                                                                                                                                            self.ref_var.get()
                                                                                            
                                                                                                                                                                                                          ))
            
            conn.commit()
            self.fatch_data()
            conn.close()
            
            messagebox.showinfo("Updated","Record has been updated successfully")
            
    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        
        sql="delete from pharmacy where refno=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql, val)
        
        conn.commit()
        self.fatch_data()
        conn.close()
        
        messagebox.showinfo("Delete","Info deleted successfully")
        
    def reset(self):
        self.ref_var.set(""),
        self.cmpName_var.set(""),
        self.typeMed_var.set(""),
        self.medName_var.set(""),0
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")    
        
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2405", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.serchTxt_var.get()) + "%'")

    
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for i in rows:
            self.pharmacy_table.insert("", END, values=i)
        conn.commit()
        conn.close()
        
    def exit_application(self):
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
        if MsgBox == 'yes':
            root.destroy()
            
    def say_hello(self):
        self.engine.say("Hello! Welcome to Health Care Pharmacy")
        self.engine.runAndWait()
        
    def speak_message(self):
        self.engine.say("Stay home! stay safe! ")
        self.engine.runAndWait()
        
    def speak_medicine(self):
        self.engine.say("New Medicine add department")
        self.engine.runAndWait()
        
    def speak_text(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        
    def generate_bill(self):
        selected_items = self.pharmacy_table.selection()
        bill_window = Toplevel(root)
        bill_window.title("Bill")

        bill_frame = Frame(bill_window)
        bill_frame.pack()

        if not selected_items:
            messagebox.showwarning("No Item Selected", "Please select an item to generate the bill.")
            return

        bill_text = "=============== Pharmacy Bill ==============\n\n"
        total_amount = 0

        for i, item in enumerate(selected_items, start=1):
            item_values = self.pharmacy_table.item(item, 'values')
            ref_no, med_name, issue_date, product, price = item_values[0], item_values[3], item_values[5], item_values[12], item_values[11]

            bill_text += f"Reference No: {ref_no}\n"
            bill_text += f"Medicine Name: {med_name}\n"
            bill_text += f"Issue Date: {issue_date}\n"
            bill_text += f"Product Quantity: {product}\n\n"
            bill_text += "===========================================\n\n"
            bill_text += f"Total Amount: {price}\n"

            total_amount += float(price)  # Assuming the price is in the 11th column

        bill_text += "===========================================\n"

        lblBillTitle = Label(bill_frame, text="Bill Details", font=("arial", 14, "bold"))
        lblBillTitle.grid(row=0, columnspan=2)

        lblBillText = Label(bill_frame, text=bill_text, font=("arial", 12))
        lblBillText.grid(row=1, columnspan=2, sticky="w")
        
        # Print or display the bill
        #print(bill_text)

    # Adding a button to print the bill
        btnPrintBill = Button(bill_frame, text="Save & Print Bill", command=lambda: self.save_and_print_bill(bill_text))
        btnPrintBill.grid(row=2, columnspan=2)

    def save_and_print_bill(self, bill_text):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(bill_text)
                messagebox.showinfo("Bill Saved", "Bill saved successfully!")

            # Print the saved bill
                self.print_file(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the bill: {e}")

    def print_file(self, file_path):
        if os.path.exists(file_path):
            try:
                os.startfile(file_path, "print")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while printing the file: {e}")
        else:
            messagebox.showerror("Error", "File not found.")
    
    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (400, 225))
            frame = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.root.after(20, self.update_video)
        else:
            self.cap.release()
            self.cap = cv2.VideoCapture("videoplayback.mp4")  # Replace this with your video file path
            self.update_video()


    def scan_qr_code(self):
    # Initialize camera capture
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera

        while True:
        # Read frame from the camera
            ret, image = cap.read()

        # Decode QR code
            decoded_objects = decode(image)

        # Display the frame
            cv2.imshow('QR Code Scanner', image)

        # Check if a QR code is detected
            if decoded_objects:
                for obj in decoded_objects:
                    scanned_data = obj.data.decode("utf-8")
                    print('Data:', scanned_data)

                # Update the reference number field in the pharmacy table
                    self.refMed_var.set(scanned_data)

                # Once you've set the scanned data to the reference number, you may want to exit the loop
                    break

        # Wait for 'q' key to quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    # Release the camera and close OpenCV windows
                cap.release()
                cv2.destroyAllWindows()
                
    def scan_qr_codes(self):
    # Initialize camera capture
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera

        while True:
        # Read frame from the camera
            ret, image = cap.read()

        # Decode QR code
            decoded_objects = decode(image)

        # Display the frame
            cv2.imshow('QR Code Scanner', image)

        # Check if a QR code is detected
            if decoded_objects:
                for obj in decoded_objects:
                    scanned_data = obj.data.decode("utf-8")
                    print('Data:', scanned_data)

                # Update the reference number field in the pharmacy table
                    self.serchTxt_var.set(scanned_data)

                # Once you've set the scanned data to the reference number, you may want to exit the loop
                    break

        # Wait for 'q' key to quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    # Release the camera and close OpenCV windows
                cap.release()
                cv2.destroyAllWindows()



if __name__ == "__main__":
    root = tk.Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
