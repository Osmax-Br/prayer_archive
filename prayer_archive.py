from tkinter.constants import DISABLED
from guizero import *
from tksheet import Sheet
import tkinter as tk
import ctypes
import sqlite3
db = sqlite3.connect("prayer.db")
week = ["سبت","احد","اثنين","ثلاثاء","اربعاء","خميس","جمعة"]
ctypes.windll.shcore.SetProcessDpiAwareness(1)
app = App(title= "set prayer time",width=1920,height=1080,bg = "#012443")
app.tk.state('zoomed')
app.text_color = "#FF6B6B"
app.text_size = 30
def p():
    pass
command = """ create table if not exists times(year_day int primary key not null,    
                                               week_day int,
                                               day int,
                                               month int,
                                               fajr_hour int,
                                               fajr_minute int,
                                               shrouk_hour int,
                                               shrouk_minute int,
                                               duhr_hour int,
                                               duhr_minute int,
                                               asr_hour int,
                                               asr_minute int,
                                               mughrb_hour int,
                                               mughrb_minute int,
                                               isha_hour int,
                                               isha_minute int,
                                               city text);

"""
db.execute(command)
db.commit()
def save():
    week_day.remove("اختر يوما")
    c = db.cursor()
    c.execute("""select year_day from times where year_day = ? """,(year_day.value,))
    if c.fetchone():
        error("hi","تم ادخال هذا التاريخ مسبقا")
    else:    
        c = db.cursor()
        c.execute("""select year_day from times where day = ? and month = ?""",(day.value,month.value,))
        if c.fetchone():
            error("hi","تم ادخال هذا التاريخ مسبقا")
        else:
            if(year_day.value == "" or day.value == "" or month.value == "" or week_day.value == "اختر يوما" or
            fajr_hour.value == "" or fajr_minute.value == "" or shrouk_hour.value == "" or shrouk_minute.value == ""
            or duhr_hour.value == "" or duhr_minute.value == "" or asr_hour.value == "" or asr_minute.value == ""
            or mughrb_hour.value == "" or mughrb_minute.value == "" or isha_hour.value == "" or isha_minute.value == ""):
                error("hi","يوجد معلومات منقوصة")
            else:
                db.execute("""insert into times values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(year_day.value,week_day.value,day.value,month.value,
                fajr_hour.value,fajr_minute.value,shrouk_hour.value,shrouk_minute.value,duhr_hour.value,
                duhr_minute.value,asr_hour.value,asr_minute.value,mughrb_hour.value,mughrb_minute.value,
                isha_hour.value,isha_minute.value,"homs"))
                db.commit()
                week_day.remove("اختر يوما")
                year_day.value = int(year_day.value) + 1
                if month.value == "12" and day.value == "31":
                    info("hi","finish")
                    month.value = day.value = 1
                elif int(month.value) in [1,3,5,7,8,10,12] and day.value == "31":
                    month.value= int(month.value)+1
                    day.value = 1
                elif int(month.value) not in [1,3,5,7,8,10,12,2] and day.value == "30": 
                     month.value= int(month.value)+1
                     day.value = 1
                elif int(month.value) == 2 and day.value == "28":
                     month.value= int(month.value)+1
                     day.value = 1                      
                else:
                    day.value = int(day.value) + 1 
                i = week.index(week_day.value)
                if i+1 <7 :
                    i+=1
                    week_day.value = week[i]
                else:
                    i = 0
                    week_day.value = week[i]      
def last():
    command = """ select * from times where year_day = {}  """.format(int(year_day.value)-1)
    c  = db.cursor()
    c.execute(command)
    data = c.fetchall() 
    if data != []:
        year_day.value = data[0][0] 
        day.value = data[0][2] 
        month.value = data[0][3] 
        week_day.value = data[0][1]
        fajr_hour.value = data[0][4]  
        fajr_minute.value = data[0][5] 
        shrouk_hour.value = data[0][6] 
        shrouk_minute.value = data[0][7]
        duhr_hour.value = data[0][8]  
        duhr_minute.value = data[0][9]  
        asr_hour.value = data[0][10] 
        asr_minute.value = data[0][11]
        mughrb_hour.value = data[0][12] 
        mughrb_minute.value = data[0][13]
        isha_hour.value = data[0][14] 
        isha_minute.value = data[0][15] 
    else:
        error("hi","لا يوجد تاريخ مماثل في قاعدة البيانات")
        ''''
        #year_day.value = ""
        day.value = ""
        month.value = "" 
        week_day.remove("اختر يوما")
        week_day.append("اختر يوما")
        week_day.value = "اختر يوما"
        fajr_hour.value = ""  
        fajr_minute.value = "" 
        shrouk_hour.value = "" 
        shrouk_minute.value = ""
        duhr_hour.value = ""
        duhr_minute.value = ""  
        asr_hour.value = "" 
        asr_minute.value = ""
        mughrb_hour.value = ""
        mughrb_minute.value = ""
        isha_hour.value = ""
        isha_minute.value = ""     
      '''
def next():
    command = """ select * from times where year_day = {}  """.format(int(year_day.value)+1)
    c  = db.cursor()
    c.execute(command)
    data = c.fetchall() 
    if data != []:
        year_day.value = data[0][0] 
        day.value = data[0][2] 
        month.value = data[0][3] 
        week_day.value = data[0][1]
        fajr_hour.value = data[0][4]  
        fajr_minute.value = data[0][5] 
        shrouk_hour.value = data[0][6] 
        shrouk_minute.value = data[0][7]
        duhr_hour.value = data[0][8]  
        duhr_minute.value = data[0][9]  
        asr_hour.value = data[0][10] 
        asr_minute.value = data[0][11]
        mughrb_hour.value = data[0][12] 
        mughrb_minute.value = data[0][13]
        isha_hour.value = data[0][14] 
        isha_minute.value = data[0][15] 
    else:
       error("hi","no data with this day")
       # year_day.value = ""
       '''
        day.value = ""
        month.value = "" 
        week_day.remove("اختر يوما")
        week_day.append("اختر يوما")
        week_day.value = "اختر يوما"
        fajr_hour.value = ""  
        fajr_minute.value = "" 
        shrouk_hour.value = "" 
        shrouk_minute.value = ""
        duhr_hour.value = ""
        duhr_minute.value = ""  
        asr_hour.value = "" 
        asr_minute.value = ""
        mughrb_hour.value = ""
        mughrb_minute.value = ""
        isha_hour.value = ""
        isha_minute.value = ""    
        '''
def table():
    c = db.cursor()
    c.execute("""select * from times """)
    data = c.fetchall()
    class demo(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.grid_columnconfigure(0, weight = 1)
            self.grid_rowconfigure(0, weight = 1)
            self.frame = tk.Frame(self)
            self.frame.grid_columnconfigure(0, weight = 1)
            self.frame.grid_rowconfigure(0, weight = 1)
            self.sheet = Sheet(self.frame,
                               page_up_down_select_row = True,
                               expand_sheet_if_paste_too_big = True,
                               column_width = 80,
                               startup_select = (0,1,"rows"),
                                data = [[f"Row {r}, Column {c}" for c in range(5)] for r in range(len(data))], #to set sheet data at startup
                                headers = ["اليوم السنوي",    
                                               "يوم الاسبوع",
                                               "اليوم",
                                               "الشهر",
                                               "ساعة الفجر",
                                               "دقيقة الفجر",
                                               "ساعة الشروق",
                                               "دقيقة الشروق",
                                               "ساعة الظهر",
                                               "دقيقة الظهر",
                                               "ساعة العصر",
                                               "دقيقة العصر",
                                               "ساعة المغرب",
                                               "دقيقة المغرب",
                                               "ساعة العشاء",
                                               "دقيقة العشاء",
                                               "المدينة"],
                                theme = "dark blue",
                                height = 1080, #height and width arguments are optional
                                width = 1920 #For full startup arguments see DOCUMENTATION.md
                                )
            self.sheet.enable_bindings(("single_select", #"single_select" or "toggle_select"
                                             "drag_select",   #enables shift click selection as well
                                        "select_all",
                                             "column_drag_and_drop",
                                             "row_drag_and_drop",
                                             "column_select",
                                             "row_select",
                                             "column_width_resize",
                                             "double_click_column_resize",
                                             "row_width_resize",
                                             "column_height_resize",
                                             "arrowkeys",
                                             "row_height_resize",
                                             "double_click_row_resize",
                                             "right_click_popup_menu",
                                             "rc_select",
                                             "copy"
                                             
                                             
                                             
                                        ))
            self.frame.grid(row = 0, column = 0, sticky = "nswe")
            self.sheet.grid(row = 0, column = 0, sticky = "nswe")
            #ur code here
            data_rows = len(data)
            #self.sheet.set_cell_data(1, 2, "NEW VALUE")
            for r in range(len(data)):
                #for i in data[r]
                self.sheet.set_row_data(r, values = (data[r][0],data[r][1],data[r][2],data[r][3],data[r][4],data[r][5],data[r][6],data[r][7],data[r][8],
                                                     data[r][9],data[r][10],data[r][11],data[r][12],data[r][13],data[r][14],data[r][15],data[r][16]))   
    app = demo()
    app.state("zoomed")
    app.mainloop() 
   

def update():
    try:
        db.execute("""update times SET week_day = ? ,day = ? , month = ?  ,
                fajr_hour = ? , fajr_minute = ? , shrouk_hour = ? , shrouk_minute = ?
                , duhr_hour = ? , duhr_minute = ? , asr_hour = ? , asr_minute = ?
                , mughrb_hour = ? , mughrb_minute = ? , isha_hour = ? , isha_minute = ? where year_day = ?""",(week_day.value, day.value , month.value ,
                fajr_hour.value , fajr_minute.value , shrouk_hour.value , shrouk_minute.value,
                duhr_hour.value , duhr_minute.value , asr_hour.value , asr_minute.value,
                mughrb_hour.value , mughrb_minute.value , isha_hour.value , isha_minute.value , year_day.value) ) 
        db.commit()   
        info("hi","تم التعديل بنجاح")  
    except:
        error("hi","يوجد خطا لم يتم التعديل")           


#####
menu = MenuBar(app,toplevel = ["file","about"]
               ,options=[   [["op1",p],["op2",p]],[["op1",p],["op2",p]]  ])
main_title = Text(app,"ادخال بيانات اوقات الصلاة 2022",align= "top")
main_title.text_size = 40
main_title.text_color = "#FFAB4C"               
Box(app,align="top",height= 30)
date_box = Box(app,align= "top",width = "fill")
#
Box(date_box,align="right",width = 60)
Text(date_box,text = "  اليوم السنوي",align="right")
year_day = TextBox(date_box,align="right",width=5)
year_day.tk.config(insertbackground="white") 
year_day.bg = "#3F3351"
year_day.text_color = "#E9A6A6"
#
Box(date_box,align="right",width = 60)
Text(date_box,text = " اليوم",align="right")
week_day = Combo(date_box,align="right",width=10,options=["اختر يوما","سبت","احد","اثنين","ثلاثاء","اربعاء","خميس","جمعة"],selected="اختر يوما")
week_day.bg = "#3F3351"
week_day.text_color = "#E9A6A6"
week_day.text_size = 20
#
Box(date_box,align="right",width = 60)
Text(date_box,text = "  تاريخ اليوم",align="right")
day = TextBox(date_box,align="right",width=5)
day.tk.config(insertbackground="white") 
day.bg = "#3F3351"
day.text_color = "#E9A6A6"
#
Box(date_box,align="right",width = 60)
Text(date_box,text = " الشهر",align="right")
month = TextBox(date_box,align="right",width=5)
month.tk.config(insertbackground="white") 
month.bg = "#3F3351"
month.text_color = "#E9A6A6"
#
Box(date_box,align="right",width = 60)
Text(date_box,text = " المدينة",align="right")
city = Text(date_box,align="right",width=5,text = "حمص")
city.bg = "#3F3351"
city.text_color = "#E9A6A6"
city.text_size = 20
########
Box(app,align="top",height= 100)
first_prayers_box = Box(app,align= "top",width = "fill")
#
Box(first_prayers_box,align="right",width = 60)
p = Text(first_prayers_box,text = "  صلاة الفجر",align="right",color="#FFAB4C")
p.size = 40
Box(first_prayers_box,align="right",width = 10)
Text(first_prayers_box,text = " الساعة",align="right")
fajr_hour = TextBox(first_prayers_box,align="right",width=5)
fajr_hour.tk.config(insertbackground="white") 
fajr_hour.bg = "#3F3351"
fajr_hour.text_color = "#E9A6A6"
Box(first_prayers_box,align="right",width = 20)
Text(first_prayers_box,text = " الدقيقة",align="right")
fajr_minute = TextBox(first_prayers_box,align="right",width=5)
fajr_minute.tk.config(insertbackground="white") 
fajr_minute.bg = "#3F3351"
fajr_minute.text_color = "#E9A6A6"
#
Box(first_prayers_box,align="right",width = 150)
p = Text(first_prayers_box,text = " وقت الشروق",align="right",color="#FFAB4C")
p.size = 40
Box(first_prayers_box,align="right",width = 10)
Text(first_prayers_box,text = " الساعة",align="right")
shrouk_hour = TextBox(first_prayers_box,align="right",width=5)
shrouk_hour.tk.config(insertbackground="white") 
shrouk_hour.bg = "#3F3351"
shrouk_hour.text_color = "#E9A6A6"
Box(first_prayers_box,align="right",width = 20)
Text(first_prayers_box,text = " الدقيقة",align="right")
shrouk_minute = TextBox(first_prayers_box,align="right",width=5)
shrouk_minute.tk.config(insertbackground="white") 
shrouk_minute.bg = "#3F3351"
shrouk_minute.text_color = "#E9A6A6"
#####
Box(app,align="top",height= 70)
second_prayers_box = Box(app,align= "top",width = "fill")
#
Box(second_prayers_box,align="right",width = 50)
p = Text(second_prayers_box,text = "  صلاة الظهر",align="right",color="#FFAB4C")
p.size = 40
Box(second_prayers_box,align="right",width = 10)
Text(second_prayers_box,text = " الساعة",align="right")
duhr_hour = TextBox(second_prayers_box,align="right",width=5)
duhr_hour.tk.config(insertbackground="white") 
duhr_hour.bg = "#3F3351"
duhr_hour.text_color = "#E9A6A6"
Box(second_prayers_box,align="right",width = 20)
Text(second_prayers_box,text = " الدقيقة",align="right")
duhr_minute = TextBox(second_prayers_box,align="right",width=5)
duhr_minute.tk.config(insertbackground="white") 
duhr_minute.bg = "#3F3351"
duhr_minute.text_color = "#E9A6A6"
#
Box(second_prayers_box,align="right",width = 150)
p = Text(second_prayers_box,text = " صلاة العصر",align="right",color="#FFAB4C")
p.size = 40
Box(second_prayers_box,align="right",width = 10)
Text(second_prayers_box,text = " الساعة",align="right")
asr_hour = TextBox(second_prayers_box,align="right",width=5)
asr_hour.tk.config(insertbackground="white") 
asr_hour.bg = "#3F3351"
asr_hour.text_color = "#E9A6A6"
Box(second_prayers_box,align="right",width = 20)
Text(second_prayers_box,text = " الدقيقة",align="right")
asr_minute = TextBox(second_prayers_box,align="right",width=5)
asr_minute.tk.config(insertbackground="white")
asr_minute.bg = "#3F3351"
asr_minute.text_color = "#E9A6A6"
#######
Box(app,align="top",height= 70)
third_prayers_box = Box(app,align= "top",width = "fill")
#
Box(third_prayers_box,align="right",width = 50)
p = Text(third_prayers_box,text = " صلاة المغرب",align="right",color="#FFAB4C")
p.size = 40
Box(third_prayers_box,align="right",width = 10)
Text(third_prayers_box,text = " الساعة",align="right")
mughrb_hour = TextBox(third_prayers_box,align="right",width=5)
mughrb_hour.tk.config(insertbackground="white")
mughrb_hour.bg = "#3F3351"
mughrb_hour.text_color = "#E9A6A6"
Box(third_prayers_box,align="right",width = 20)
Text(third_prayers_box,text = " الدقيقة",align="right")
mughrb_minute = TextBox(third_prayers_box,align="right",width=5)
mughrb_minute.tk.config(insertbackground="white")
mughrb_minute.bg = "#3F3351"
mughrb_minute.text_color = "#E9A6A6"
#
Box(third_prayers_box,align="right",width = 150)
p = Text(third_prayers_box,text = " صلاة العشاء",align="right",color="#FFAB4C")
p.size = 40
Box(third_prayers_box,align="right",width = 10)
Text(third_prayers_box,text = " الساعة",align="right")
isha_hour = TextBox(third_prayers_box,align="right",width=5)
isha_hour.tk.config(insertbackground="white")
isha_hour.bg = "#3F3351"
isha_hour.text_color = "#E9A6A6"
Box(third_prayers_box,align="right",width = 20)
Text(third_prayers_box,text = " الدقيقة",align="right")
isha_minute = TextBox(third_prayers_box,align="right",width=5)
isha_minute.tk.config(insertbackground="white")
isha_minute.bg = "#3F3351"
isha_minute.text_color = "#E9A6A6"
#
Box(app,align="top",height= 150)
control_box = Box(app,align= "top",width = "fill")
Box(control_box,align="right",width = 20)
next_save = PushButton(control_box,align="right",text = "حفظ/اليوم التالي",command=save)
next_save.bg = "#FE7E6D"
next_save.text_color = "#9B0000"
Box(control_box,align="left",width = 20)
last = PushButton(control_box,align="left",text = "السابق",command= last)
last.bg = "#FE7E6D"
last.text_color = "#9B0000"
Box(control_box,align="left",width = 20)
next = PushButton(control_box,align="left",text = "التالي",command= next)
next.bg = "#FE7E6D"
next.text_color = "#9B0000"
Box(control_box,align="left",width = 20)
edit = PushButton(control_box,align="left",text = "تــــــعــــــديــــــــــل",command= update)
edit.bg = "#FE7E6D"
edit.text_color = "#9B0000"
Box(control_box,align="left",width = 20)
edit = PushButton(control_box,align="left",text = "عرض كل البيانات",command= table)
edit.bg = "#FE7E6D"
edit.text_color = "#9B0000"

app.display()               