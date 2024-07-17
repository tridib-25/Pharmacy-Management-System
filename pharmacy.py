from tkinter import*
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
import datetime
from time import strftime
import mysql.connector

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ===============================varibles Declaration==========================================================
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

        # ========== Title label======================================================================================
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bg="#e6e600",fg="red",bd=15,relief=RIDGE,font=("arial",35,"bold"),padx=2,pady=1)
        lbltitle.pack(side=TOP,fill=X)


        img3 = Image.open("logos.jpg")
        img3 = img3.resize((60,60), Image.Resampling.LANCZOS)
        self.photoImg3 =  ImageTk.PhotoImage(img3)
        b3 =Button(self.root,image=self.photoImg3,text="Pharmacy",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b3.place(x=70,y=10)


        # ======leftrightDataframe======================================================================================
        DataFrame=Frame(self.root,bd=10,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=75,width=1550,height=390)
        
        DataFrameLeft=LabelFrame(DataFrame,bg='#00b300',bd=10,padx=20,relief=RIDGE,fg="blue",
                                                font=("arial",15,"bold"),text="Medicine Information")
        DataFrameLeft.place(x=-20,y=0,width=760,height=370)

        lblReg=Label(DataFrameLeft,width=27,font=("arial",15,"bold"),text="Pharmacy Management System",fg="red",padx=2,bg="white")
        lblReg.place(x=385,y=155)

        # =======images=======================================================

        '''img1 = Image.open("lab.jpg")
        img1 = img1.resize((150,135), Image.Resampling.LANCZOS)
        self.photoImg1 =  ImageTk.PhotoImage(img1)
        b4 =Button(self.root,image=self.photoImg1,text="Pharmacy",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b4.place(x=770,y=330)'''

        img2 = Image.open("pharma.jpg")
        img2 = img2.resize((150,135), Image.Resampling.LANCZOS)
        self.photoImg2 =  ImageTk.PhotoImage(img2)
        b4 =Button(self.root,image=self.photoImg2,text="Pharmacy",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b4.place(x=560,y=295)

        img4 = Image.open("medicines.jpg")
        img4 = img4.resize((150,135), Image.Resampling.LANCZOS)
        self.photoImg4 =  ImageTk.PhotoImage(img4)
        b5 =Button(self.root,image=self.photoImg4,text="Pharmacy",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b5.place(x=390,y=295)
        # ===========Buttonframe=================================================================================
        ButtonFrame=Frame(self.root,bg='#8600b3',bd=10,padx=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=465,width=1550,height=85)

        # ========MainButtons=======
        btnAddData=ttk.Button(ButtonFrame,command=self.add_data,text="ADD MEDICINE",width=10)
        btnAddData.grid(row=0,column=0,padx=14,pady=18)

        btnUpdateMed=ttk.Button(ButtonFrame,command=self.update_data,text="UPDATE",width=10)
        btnUpdateMed.grid(row=0,column=1,padx=14,pady=18)

        btnDeleteMed=ttk.Button(ButtonFrame,command=self.mDelete,text="DELETE",width=10)
        btnDeleteMed.grid(row=0,column=2,padx=14,pady=18)

        btnRestMed=ttk.Button(ButtonFrame,command=self.Reset,text="RESET",width=10)
        btnRestMed.grid(row=0,column=3,padx=14,pady=18)

        btnExitMed=ttk.Button(ButtonFrame,command=self.iExit,text="EXIT",width=10)
        btnExitMed.grid(row=0,column=4,padx=14,pady=18)

        # ==========Search By========
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2)
        lblSearch.grid(row=0,column=5,sticky=W,padx=14,pady=18)

        # variable
        self.serch_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.serch_var,width=10,font=("arial",15),state="readonly")
        search_combo['values']=("Select Option","Ref","medname","lot")
        search_combo.grid(row=0,column=6,sticky=W,padx=14,pady=18)
        search_combo.current(0)

        self.serchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.serchTxt_var,bd=3,relief=RIDGE,width=10,font=("arial",15))
        txtSearch.grid(row=0,column=7)


        btnExit=ttk.Button(ButtonFrame,command=self.search_data,text="SEARCH",width=10)
        btnExit.grid(row=0,column=8,padx=14,pady=18)

        btnExit=ttk.Button(ButtonFrame,command=self.fatch_data,text="SHOW ALL",width=10)
        btnExit.grid(row=0,column=9,padx=14,pady=18)

        # ===================Details Frame===================================================================================
        # ===================Main Labels And enty=========================================================================
        FrameDetails=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        FrameDetails.place(x=0,y=550,width=1550,height=248)

        conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from medicine")
        r=my_cursor.fetchall()

        lblrefno=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Reference No",padx=2,pady=10)
        lblrefno.grid(row=0,column=0,sticky=W)

        comrefno=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,state="readonly",
                                                        font=("arial",10,"bold"),width=22)
        comrefno['value']=r
        comrefno.current(0)
        comrefno.grid(row=0,column=1)

        lblCmpName=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Company Name:",padx=2,pady=10)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=19)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Type Of Medicine",padx=2,pady=10)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",
                                                        font=("arial",11,"bold"),width=19)
        comTypeofMedicine['value']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)

        # ==========AddMedicine============
        conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedicineName from medicine")
        ide=my_cursor.fetchall()
        # self.fetch_Medicine_data()
        
        lblMedicineName=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Medicine Name",padx=2,pady=10)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly",
                                                        font=("arial",11,"bold"),width=19)
        comMedicineName['value']=ide
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)


        lblLotNo=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Lot No:",padx=2,pady=10)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Issue Date:",padx=2,pady=10)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Exp Date:",padx=2,pady=10)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Uses:",padx=2,pady=10)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Side Effect:",padx=2,pady=10)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Prec&Warning:",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,bg='#00b300',font=("arial",10,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",fg="black",bd=2,relief=RIDGE,width=22)
        txtProductQt.grid(row=3,column=3,sticky=W)


# ===============================Right Department Management labelframe =============================================================

        DataFrameRight=LabelFrame(DataFrame,bg="#2eb8b8",bd=12,padx=20,relief=RIDGE,fg="blue",
                                            font=("arial",15,"bold"),text="New Medicine Add Department")
        DataFrameRight.place(x=740,y=0,width=770,height=370)

        # =====Inside label and entry ================================================
        # ============variables medicine=============

        '''img5 = Image.open("tablet.jpg")
        img5 = img5.resize((180,75), Image.Resampling.LANCZOS)
        self.photoImg5 =  ImageTk.PhotoImage(img5)
        b6 =Button(self.root,image=self.photoImg5,text="Pharmacy",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b6.place(x=960,y=160)'''

        img6 = Image.open("instru.jpg")
        img6 = img6.resize((180,100), Image.Resampling.LANCZOS)
        self.photoImg6 =  ImageTk.PhotoImage(img6)
        b6 =Button(self.root,image=self.photoImg6,text="Pharmay",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b6.place(x=1285,y=120)

        
        '''img7 = Image.open("tab.jpg")
        img7 = img7.resize((200,145), Image.Resampling.LANCZOS)
        self.photoImg7 =  ImageTk.PhotoImage(img7)
        b6 =Button(self.root,image=self.photoImg7,text="pharmacy",borderwidth=0,font=("arial",22,"bold"),fg="white",cursor="hand2")
        b6.place(x=1270,y=160)'''

        l_ref=Label(DataFrameRight,text="Reference No:",fg="white",bg="#2eb8b8",font=("arial",15,"bold"))
        l_ref.place(x=0,y=40)
        
        self.ref_add_var=StringVar()
        entry_ref=ttk.Entry(DataFrameRight,textvariable=self.ref_add_var,width=20,font=("arial",15))
        entry_ref.place(x=135,y=40)
        
        l_Medicine=Label(DataFrameRight,text="Medicine Name:",fg="white",bg="#2eb8b8",font=("arial",15,"bold"))
        l_Medicine.place(x=0,y=80)
        
        self.medicine_add_var=StringVar()
        entry_Medicine=ttk.Entry(DataFrameRight,textvariable=self.medicine_add_var,width=20,font=("arial",15))
        entry_Medicine.place(x=135,y=80)

        # ================================ right side frame table ==============================================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=140,width=450,height=170)

        # ================================ right side frame ==============================================

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","tbname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref No")
        self.medicine_table.heading("tbname",text="Tablet Name")
        self.medicine_table["show"]="headings"
        self.medicine_table.column("ref",width=10)
        self.medicine_table.column("tbname",width=50)
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.fetch_Medicine_data()
        self.medicine_table.bind("<ButtonRelease>",self.get_cursor_med)
       
        # ================================== Medicine Add button=============================================================

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="#00b300")
        down_frame.place(x=500,y=140,width=150,height=170)

        add_btn=ttk.Button(down_frame,text="ADD",command=self.add_medicine,width=10) 
        add_btn.grid(row=0,column=0,pady=6,padx=5)

        update_btn=ttk.Button(down_frame,command=self.med_update,text="UPDATE",width=10)
        update_btn.grid(row=1,column=0,pady=6,padx=5)

        delete_btn=ttk.Button(down_frame,command=self.medDelete,text="DELETE",width=10)
        delete_btn.grid(row=2,column=0,pady=6,padx=5)

        clear_btn=ttk.Button(down_frame,command=self.clear_med,text="CLEAR",width=10)
        clear_btn.grid(row=3,column=0,pady=6,padx=5)
     
   
        # =======Scrollbar and Main Table=====================================================================================
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=-18,y=1,width=1518,height=215)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate",
                                            "expdate","uses","sideeffect","warning","dosage","price","productqt")
                                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
   
        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=97)
        self.pharmacy_table.column("companyname",width=97)
        self.pharmacy_table.column("type",width=97)
        self.pharmacy_table.column("tabletname",width=97)
        self.pharmacy_table.column("lotno",width=97)
        self.pharmacy_table.column("issuedate",width=97)
        self.pharmacy_table.column("expdate",width=97)
        self.pharmacy_table.column("uses",width=97)
        self.pharmacy_table.column("sideeffect",width=97)
        self.pharmacy_table.column("warning",width=97)
        self.pharmacy_table.column("dosage",width=97)
        self.pharmacy_table.column("price",width=97)
        self.pharmacy_table.column("productqt",width=97)

        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


    # ===================== MedicineAdd=================================================================      
    def add_medicine(self):
        conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into medicine(ref,MedicineName) values(%s,%s)",(                                                        
                                                                            self.ref_add_var.get(),
                                                                            self.medicine_add_var.get(),
                                                                         
                                                                        ))
        conn.commit()
        self.fetch_Medicine_data()
        self.catchdata()
        self.clear_med()
        
        conn.close()
        messagebox.showinfo("Success","Medicine Added Successfully!")


    
    # ===================fetch data ============================================================

    def fetch_Medicine_data(self):
        conn=mysql.connector.connect(host='localhost',user='dbms',password='test123',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from medicine")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

     # ====================== clear =============================================================

    def clear_med(self):
        self.ref_add_var.set("")
        self.medicine_add_var.set("")
    # ======================getCursorMedicine======================================================
    def get_cursor_med(self,event=" "):
        cursor_rows=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_rows)
        row=content["values"]
        self.ref_add_var.set(row[0])
        self.medicine_add_var.set(row[1])

    # ====================medicien delete===========================================================
    def medDelete(self):
        mDelete=messagebox.askyesno("Pharmacy Management System","Do you want to delete this medicine?")
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
            my_cursor=conn.cursor()
            sql="delete from medicine where ref=%s"
            val=(self.ref_add_var.get(),)
            my_cursor.execute(sql,val)
        else:
            if not mDelete:
                return 
         
        conn.commit()
        self.fetch_Medicine_data()
        self.clear_med()
        conn.close()
    # ============================updateall===================================================================
    def med_update(self):
            if self.ref_add_var.get()=="" or self.medicine_add_var.get()=="":
                messagebox.showwarning("Warning","All fields are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update medicine set MedicineName=%s where ref=%s",(
                                                                                            self.medicine_add_var.get(),
                                                                                            self.ref_add_var.get()                                                                                                                                
                                                                                                                            
                                                                                         ))
                                                                                                                            
                    conn.commit()
                    self.fetch_Medicine_data()
                    conn.close()
                    messagebox.showinfo("Success","Data Successfully Updated!") 
                    
        
                                                                                                                                                            
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    # ==========================Add Main Data====================================================
    def add_data(self):
        if self.ref_var.get()=="" or self.typeMed_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
                my_cursor=conn.cursor()
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
                messagebox.showinfo("Success","Medicine has been successfully added!")
             
            except Exception as es:
                messagebox.showerror("Error",f" Must be enter Integer number:{str(es)}",parent=self.root)
     # ========================Update=============================================================
    def update_data(self):
        if self.ref_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            conn=mysql.connector.connect(host='localhost',user='dbms',password='test123',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set CompanyName=%s,TypeOfMedicine=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where Ref=%s",(
                                                                                
                                                                                                                                                                                                                
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
            self.Reset()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been updated successfully")

                                                      

    # ====================fetchdata=================================================
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="dbms",password="test123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =======================get cursor================================================
    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])
    # =====================Delete================================================================
    def mDelete(self): 
        if self.lot_var.get()=="":
            messagebox.showinfo("ERROR","First Select the Details!!")
        else:
            conn=mysql.connector.connect(host='localhost',user='dbms',password='test123',database='management')
            my_cursor=conn.cursor()
            query="delete from pharmacy where Ref=%s"
            value=(self.ref_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            conn.close()
            self.fatch_data()
            self.Reset()
            messagebox.showinfo("DELETE","Medicine Information has been deleted successfully!")         

    # =====================Exit================================================================
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Pharmacy Management System","Are you sure you want to exit?")
        if iExit>0:
            root.destroy()
            return

    # ==============================reset========================================================
    def Reset(self):    
        # self.ref_var.set(""),
        self.cmpName_var.set(""),
        # self.typeMed_var.set(""),
        # self.medName_var.set(""),
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
        conn=mysql.connector.connect(host='localhost',user='dbms',password='test123',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
      


if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
