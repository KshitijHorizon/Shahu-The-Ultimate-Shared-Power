"""
   This  Shahu: Ultimate Shared Power software is made in tkinter library which is basic native GUI framework of Python.

   Developers::1>Kshitij Bajagain   -Main developer(coder)    (kshitij.bajagain123@gmail.com, 2019)
                2>Anupam Dhakal     -Documentation,2nd-coder  (anupamdhakal20@gmail.com, 2019)
                3>Dinesh Timalsina  -Tester,Idea generator    (timalsinadinesh2@gmail.com, 2019)
                4>Ram Ghimire       -Analyst                  (ramghimire733@gmail.com, 2019)

    Python Interpreter = Python 3.7.1
    IDLE Used = JetBrains Pycharm Professional(University License agreement)
    Designing software used = GIMP 2.10.8 and Photoshop 2018 CC
    Copyright = Illegal copy and distribution of this software is strictly prohibited .
                Developers can only change and make copy of this Shahu:Ultimate Shared Power Software

"""

                ## These are all library that we used during development of this software##


from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
from tkinter import Frame
import tkinter.messagebox
from tkinter import ttk
import time
import json
from datetime import date
import os
import calendar
import hashlib
from PIL import Image, ImageTk
from tkinter import Tk, filedialog



'''
            
This is SplashScreen Class which will initialize the software and redirects you to Register Page 

'''
class SplashScreenFrame(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, padx=2, pady=2)



        self.button = Button(master,text="Explore Shahu", font=("bold", 10), relief="groove", activebackground="green",command=self.command1).place(x=255, y=310)

        self.progress_bar = ttk.Progressbar(master, orient="horizontal",
                                        length=600, mode="determinate")
        self.progress_bar.place(x=0,y=280)


        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=90, y=340)

        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        title = Label(root, text="Shahu : The Ultimate Shared Power", width=30, font=("bold", 22))
        title.place(x=97, y=35)

        self.img2 = PhotoImage(file="Images\yup1.png")
        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=10, y=5)

        self.img1 = PhotoImage(file="Images\Background3.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=145, y=75)

    def open_terms(self):
        os.startfile("Terms.txt")



    def command1(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position

                root.state('withdrawn')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = RegistrationFrame(self.newWindow)
                self.newWindow.geometry('550x570+450+110')

                self.newWindow.title("Shared Power Registeration Form")

    def run(self):
        self.progress_bar.start()
        #self.progress_bar['maximum'] = 100






'''

This is LoginFrame Class which will login user into their respective UserPanels .Registered User Can enter their 
credentials inorder to start their session in our software. 

'''

class LoginFrame():
    def __init__(self, master):

        global entry_username, login_password

        self.master = master
        self.frame = tk.Frame(master)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17), relief="groove", activebackground="blue",
                                 command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_destroy = Button(master, text="X", width=2, font=("bold", 17), relief="groove", activebackground="red",
                                command=endProgram)
        self.button_destroy.place(x=515, y=3)


        self.label_username = Label(master, text="Username", width=20, font=("bold", 13))
        self.label_username.place(x=80, y=130)

        self.entry_username = Entry(master, bd=5)
        self.entry_username.place(x=240, y=130, width=180)

        self.label_password = Label(master, text="    Password", width=20, font=("bold",13))
        self.label_password.place(x=68,y=180)

        self.login_password = Entry(master, bd=5,show="*")
        self.login_password.place(x=240, y=180, width=180)

        var2 = IntVar()
        Checkbutton(master, text="Keep me logged in", variable=var2, font=('Times', 13,'underline'),cursor="hand1").place(x=190, y=225 , width=200)

        Button(master, text='Log In', font=("bold", 11), width=20, bg='brown', fg='white', command=self.login_info).place(
            x=208, y=280)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=23)

        self.img1 = PhotoImage(file="Images\login2.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=180,y=30)

        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=88, y=320)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        master.resizable(False, False)
        master.overrideredirect(True)



    def open_terms(self):
        os.startfile("Terms.txt")

    '''

    This login_info method will save the login info of user and as well as this will check the 
    credentials inorder to start their user session in our software. 

    '''

    def login_info(self):

        self.passw1=self.login_password.get()
        self.Username_Login = self. entry_username.get()
        self.Password_Login = hashlib.sha1(self.login_password.get().encode()).hexdigest()

        file = open("Text File Handling\database3.txt", "r")
        self.login1=file.read()

        if  self.Username_Login and self.Password_Login in self.login1:
            tm.showinfo("Login successful", "Welcome User")
            self.master.withdraw()

            #print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = UserPanelFrame(self.newWindow)
            self.newWindow.geometry('720x720+350+15')
            self.newWindow.title("Shared Power Login Form")

        elif self.Username_Login == "Insurance!" and self.passw1 =="INS!@#":
            self.master.withdraw()
            tm.showinfo("Login successful", "Welcome to Insurance Company Profile ")
            #print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = InsuranceCompany(self.newWindow)
            self.newWindow.geometry('550x550+450+140')
            self.newWindow.title("Insurance Company Form")

        else:
            tm.showerror("Login error", "Invalid Credentials")

    def minimizeProgram(self):
        #self.master.wm_state('iconic')
        self.master.withdraw()



    def _login_btn_clicked(self):


        # print("Clicked")
        username = self.entry_username.get()
        password = self.login_password.get()

        # print(username, password)

        if username == "Shahu" and password == "admin":
            tm.showinfo("Login info", "Welcome User")
            self.master.withdraw()

            #print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = UserPanelFrame(self.newWindow)
            self.newWindow.geometry('720x720+350+15')
            self.newWindow.title("Shared Power Login Form")
        else:
            tm.showerror("Login error", "Invalid Credentials")





'''

This is UserPanel Class. After getting loged in with correct credentials the user will be redirected to this 
panel.This user Panel gives the user the function like searching the tool , uploading the tool, hiring the tool
, returning the tool, and generating the invoice by clicking on respective functions.

'''


class UserPanelFrame(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

        self.title = Label(master, text="  Current Time", font=("bold", 11))
        self.title.place(x=605, y=80)

        self.q = Canvas(master)
        self.q.place(x=600, y=97)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.q.create_text(14, 28, text=self.localtime, font=('arial', 12, 'bold'))

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=661, y=2)

        self.button_destroy = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=endProgram)
        self.button_destroy.place(x=685, y=3)


        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9),cursor="hand2")
        self.label_6.place(x=196, y=682)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)


        self.title = Label(master, text="Welcome !! Explore Shahu  ", width=30, font=("bold", 22))
        self.title.place(x=110, y=35)

        self.tool = PhotoImage(file="Images\Tool1.png")

        self.tool1 = Label(master, image=self.tool)
        self.tool1.place(x=125, y=90)

        self.tool1 = PhotoImage(file="Images\Tool1.png")

        self.tool12 = Label(master, image=self.tool1)
        self.tool12.place(x=520, y=90)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=10, y=5)

        #self.img3 = PhotoImage(file="Sp1234.png")

        #self.lab1 = Label(master, image=self.img3)
        #self.lab1.place(x=590, y=620)

        master.resizable(False, False)
        master.overrideredirect(True)

        self.button_cal = Button(master, text="Browse Calendar", font=("bold", 9), relief="groove",
                                 activebackground="red", command=self.cal1)
        self.button_cal.place(x=10, y=680)

        self.show_profile = Button(master, text="View User Info", font=("bold", 9), relief="groove",
                                 activebackground="red", command=self.show_info)
        self.show_profile.place(x=564, y=180)

        self.logout = PhotoImage(file="Images\logout.png")
        self.user_logout = Button(master, image=self.logout, width=55, height=55,cursor="hand1", relief="flat",
                                   activebackground="red", command=self.logOut)
        self.user_logout.place(x=659, y=659)



        self.man = PhotoImage(file="Images\Man.png")

        self.manphoto = Label(master, image=self.man)
        self.manphoto.place(x=10, y=160)


        self.fetch = Label(master, text="Fetch your Desire with Shahu! ", width=25, font=("bold", 16))
        self.fetch.place(x=203, y=100)
        self.s1 = PhotoImage(file="Images\s1.png")
        self.search_tools = Button(master, text="Search Tools",  width=210, height=160, image=self.s1,
                                   font=('arial', 16, "bold"), cursor="hand1",  command=self.search,
                                   activebackground="blue")
        self.search_tools.place(x=210, y=215)

        self.search1 = Label(master, text="Search Tools ", font=("arial", 16,"bold"))
        self.search1.place(x=240, y=395)


        self.upload1 = PhotoImage(file="Images\yup1.png")
        self.up = PhotoImage(file="Images\Vis3.png")
        self.up = PhotoImage(file="Images\pload1.png")
        self.upload_tools = Button(master, text="Upload Tools", width=210, height=160, image=self.up,
                                   font=('arial', 7, "bold"), cursor="hand1",command=self.upload,
                                   activebackground="green",
                                   activeforeground="red")
        self.upload_tools.place(x=438, y=215)

        self.upload1 = Label(master, text="Upload Tools ", font=("arial", 16,"bold"))
        self.upload1.place(x=475, y=395)

        self.hire = PhotoImage(file="Images\hire1.png")
        self.hire_tools = Button(master, text="Hire Tools",  width=210, height=160, image=self.hire,
                                 font=('arial', 16, "bold"), cursor="hand1",command=self.hire1,
                                 activebackground="cyan")
        self.hire_tools.place(x=210, y=445)

        self.hire13 = Label(master, text="Hire Tools ", font=("arial", 16,"bold"))
        self.hire13.place(x=257, y=623)

        self.pay = PhotoImage(file="Images\paynow1.png")
        self.pay_tools = Button(master, text="Payment & Delivery", width=210, height=160, image=self.pay,
                                font=('arial', 16, "bold"), cursor="hand1",command=self.pay1,
                                activebackground="brown",
                                activeforeground="green")
        self.pay_tools.place(x=438, y=445)

        self.pay13 = Label(master, text="Payment & Delivery ", font=("arial", 16,"bold"))
        self.pay13.place(x=446, y=623)

        # self.image_tk = PhotoImage(self.select_image())
        # self.canvas.create_image(0, 0, image=self.image_tk)

    def open_terms(self):
        os.startfile("Terms.txt")

    def search(self):

                self.master.withdraw()
                self.newWindow = tk.Toplevel(self.master)
                self.app = SearchTools(self.newWindow)
                self.newWindow.geometry('650x550+450+140')
                self.newWindow.title("Search Tools Form")



    # This will redirect the user to upload tools GUI where after entering some details we can upload tools.
    def upload(self):


                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = uploadTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Upload Tools Form")


    # This will redirect the user to Payment GUI where after entering some details we can generate invoice
    # after returning the tool.

    def pay1(self):

                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = payTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Payment Tools Form")


    # This will redirect the user to hire tools GUI where after entering some details we can sucessfully hire uploaded tools.

    def hire1(self):


                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = hireTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Hire Tools Form")


    # This will show the user to Calendar which will be easy and convenient to know current time and date.

    def cal1(self):



                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = CalendarShow(self.newWindow)
                self.newWindow.title("Calendar")
                # def select_image(self):

    # This will redirect the user to search tools GUI where user can search the uploaded tools inorder to hire those tools.
    def profile(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = SearchTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Search Tools Form")



    # This will preview the instance information of newly registered user
    def show_info(self):
        os.startfile("Text File Handling\ViewUserInfo.txt")



    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    # This logOut function will help user to logout him or her from software .
    def logOut(self):
        #print("This will logout you from user panel.")

        tm.showwarning("Confirm LogOut",
                    "Are You sure want to LogOut from  Shahu:The Ultimate Shared Power? ")

        self.master.withdraw()

        #print('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = LoginFrame(self.newWindow)
        self.newWindow.geometry('550x350+450+220')
        self.newWindow.title("Shared Power Login Form")



def onRegister():
        # json_data = open(file_directory).read()
        tkinter.messagebox.showinfo("Successful!!","Boom!! Boom !! You are successfully registered!!")


def minimizeProgram():
    #root.wm_state('iconic')
    root.withdraw()
    #root.state("withdrawn")

def endProgram():
    # top.quit()
    tm.showinfo("Confirm Exit",
                   "Are You sure want to exit Shahu:The Ultimate Shared Power? " )
    root.destroy()






# This will show the user to Calendar which will be easy and convenient to know current time and date.


class CalendarShow(Frame):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

        self.label1 = Label(master, text="Year:")
        self.label1.pack()

        self.e1 = Entry(master)
        self.e1.pack()

        self.label2 = Label(master, text="Month:")
        self.label2.pack()

        self.e2 = Entry(master)
        self.e2.pack()

        self.button = Button(master, text="Show", command=self.cal)
        self.button.pack()
        master.title("Shahu-Calendar")

        master.resizable(False, False)
        master.overrideredirect(False)

    def cal(self):
            self.y = self.e1.get()
            self.m = self.e2.get()
            self.cal_x = calendar.month(int(self.y), int(self.m), w=2, l=1)
            #print(self.cal_x)
            self.cal_out = Label( self.master,text=self.cal_x, font=('courier', 12, 'bold'), bg="#0984e3")
            self.cal_out.pack(padx=3, pady=10)




'''

This is RegisterationFrame Class which will help the visitor user to registered into our software inorder to 
use search , hire , upload, return tools and monthly invoice generation. 
 
'''


class RegistrationFrame(Frame):

    def __init__(self, master):
        global entry_fullname, \
            entry_Email, \
            entry_password, \
            entry_citizenshipno, \
            country, \
            var_P, \
            var_nonP, \
            register_gender, gender_value

        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_destroy = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=endProgram)
        self.button_destroy.place(x=515, y=3)

        self.label_1 = Label(master, text="FullName",width=20,font=("bold", 13))
        self.label_1.place(x=80,y=130)

        self.fullname=StringVar()
        self.entry_fullname = Entry(master,bd =5, textvariable=self.fullname)
        self.entry_fullname.place(x=240,y=130 ,width=180)


        self.label_2 = Label(master, text="Email",width=20,font=("bold", 13))
        self.label_2.place(x=68,y=180)

        self.entry_Email = Entry(master,bd =5)
        self.entry_Email.place(x=240,y=180,width=180)

        self.label_password = Label(master, text="    Password", width=20, font=("bold", 13))
        self.label_password.place(x=70, y=230)

        self.entry_password = Entry(master, bd=5,show="*")
        self.entry_password.place(x=240, y=230, width=180)

        self.label_3 = Label(master, text="Gender",width=20,font=("bold", 13))
        self.label_3.place(x=70,y=280)

        gender_value = StringVar()
        gender_value.set(' ')

        Radiobutton(master, text="Male", font=("bold", 10), padx=5 , variable=gender_value, value="Male",
                    command=RegistrationFrame.selected_gender).place(x=235, y=280)
        Radiobutton(master, text="Female", variable=gender_value, value="Female",
                    command=RegistrationFrame.selected_gender).place(x=290, y=280)

        '''
        var = IntVar()
        Radiobutton(master, text="Male",font=("bold", 10),padx = 5, variable=var, value=1).place(x=235,y=280)
        Radiobutton(master, text="Female",font=("bold", 10),padx = 20, variable=var, value=2).place(x=290,y=280)
        '''


        self.label_4 = Label(master, text="Country",width=20,font=("bold", 13))
        self.label_4.place(x=70,y=330)

        list1 = ['Afghanistan','Algeria','Andorra','Angola','Antigua and Barbuda','Bangladesh', 'Thailand','Canada','India','UK','Nepal','Iceland','South Africa','Uganda','Maldives'];
        country=StringVar()

        country_droplist =OptionMenu(master,country, *list1, command=RegistrationFrame.countey_selected)
        country_droplist.config(width=20)

        country.set('Select your Country')
        country_droplist.place(x=240,y=330)

        label_q = Label(master, text="    CitizenNo.", width=20, font=("bold", 13))
        label_q.place(x=70, y=380)

        self.entry_citizenshipno = Entry(master, bd=5)
        self.entry_citizenshipno.place(x=240, y=380, width=180)

        label_4 = Label(master, text="      Applied Account",width=20,font=("bold", 13))
        label_4.place(x=85,y=430)

        var_nonP = IntVar()
        Checkbutton(master, text="Non-Premium", variable=var_nonP,command=RegistrationFrame.selected_account).place(x=265,y=430)

        var_P = IntVar()
        Checkbutton(master, text="Premium", variable=var_P, command=RegistrationFrame.selected_account).place(x=375,y=430)


        self.registerButton=Button(master, text='Register',font=("bold", 11),width=20,bg='brown',fg='white' ,command =self.save_info).place(x=208,y=462)


        self.label_5 = Button(master, text="Already registered Login with your info", width=65, font=('Times', 12,'underline'),cursor="hand1",activebackground="blue",command=self.command)
        self.label_5.place(x=0, y=500)



        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=80, y=542)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)


        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=23)

        self.img1 = PhotoImage(file="Images\Regfinal1.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=160,y=35)

        master.resizable(False, False)
        master.overrideredirect(True)

    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    @staticmethod
    def selected_gender(event=None):
        global gender_selected
        gender_selected = gender_value.get()
        #print(gender_selected)

    @staticmethod
    def countey_selected(event=None):
        global country_selected, name
        country_selected = country.get()
        #print(country_selected)

    @staticmethod
    def selected_account(event=None):
        global account_selected2 , account_selected1
        account_selected1 = var_nonP.get()
        account_selected2 = var_P.get()
        account_selected1=str(account_selected1)
        account_selected2= str(account_selected2)

        #print(account_selected2)
        #print(account_selected1)


    def command(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = LoginFrame(self.newWindow)
                self.newWindow.geometry('550x350+450+220')
                self.newWindow.title("Shared Power Login Form")



            #File handling by normal text format


    def valid(self):
        self.username = self.entry_fullname.get()
        self.password = self.entry_password.get()

        if len(self.username) == 0 and len(self.password)==0:
            tm.showerror("Registration Error",
                         "Registration is unsucessful. Can be validation error or may be one or more field is empty.Please Register again with required Validation")
        else:
            print("Its ok Fine")


    def save_info(self):


       self.name = self.entry_fullname.get()
       self.passw = self.entry_password.get()
       self.Username = self.entry_Email.get()
       self.Password = hashlib.sha1(self.entry_password.get().encode()).hexdigest()
       self.CNo = self.entry_citizenshipno.get()
       self.account_selected1 = var_nonP.get()
       self.account_selected2 = var_P.get()
       self.account_selected1 = str(self.account_selected1)
       self.account_selected2 = str(self.account_selected2)
       self.gender_selected = gender_value.get()
       self.country_selected = country.get()

       self.Date = date.today()

       if (len(self.name) == 0 and len(self.passw) == 0) and (len(self.passw) != 8):
           tm.showerror("Registration Error",
                        "Registration is unsucessful. Can be validation error or may be one or more field is empty.Please Register again with required Validation")


       else:
           self.name = self.entry_fullname.get()
           self.passw = self.entry_password.get()
           self.Username = self.entry_Email.get()
           self.Password = hashlib.sha1(self.entry_password.get().encode()).hexdigest()
           self.CNo = self.entry_citizenshipno.get()
           self.account_selected1 = var_nonP.get()
           self.account_selected2 = var_P.get()
           self.account_selected1 = str(self.account_selected1)
           self.account_selected2 = str(self.account_selected2)
           self.gender_selected = gender_value.get()
           self.country_selected = country.get()
           self.Date = date.today()

           file = open("Text File Handling\database3.txt", "a")

           file.write("\n")
           file.write("                  #####Registered User Information#####")
           file.write("\n")
           file.write("\n")

           file.write("Name of user:        ")
           file.write(self.name)

           file.write("\n")
           file.write("UserName:            ")
           file.write(self.Username)

           file.write("\n")
           file.write("Password:            ")
           file.write(self.Password)

           file.write("\n")

           file.write("Account Selected:      Non-Premium        ")
           file.write(self.account_selected1)
           file.write("\n")

           file.write("                       Premium            ")
           file.write(self.account_selected2)

           file.write("\n")
           file.write("Gender:               ")
           file.write(self.gender_selected)

           file.write("\n")
           file.write("Country:              ")
           file.write(self.country_selected)

           file.write("\n")
           file.write("Citizenship Number:    ")
           file.write(self.CNo)
           file.write("\n")
           file.write("Registered Date:            ")
           file.write(str(self.Date))

           file.write("\n")
           file.close()

           file1 = open("Text File Handling\ViewUserInfo.txt", "w")

           file1.write("\n")
           file1.write("                  #####Registered User Information#####")
           file1.write("\n")
           file1.write("\n")

           file1.write("Name of user:        ")
           file1.write(self.name)

           file1.write("\n")
           file1.write("UserName:            ")
           file1.write(self.Username)

           file1.write("\n")
           file1.write("Password:            ")
           file1.write(self.Password)

           file1.write("\n")

           file1.write("Account Selected:      Non-Premium        ")
           file1.write(self.account_selected1)
           file1.write("\n")

           file1.write("                       Premium            ")
           file1.write(self.account_selected2)

           file1.write("\n")
           file1.write("Gender:               ")
           file1.write(self.gender_selected)

           file1.write("\n")
           file1.write("Country:              ")
           file1.write(self.country_selected)

           file1.write("\n")
           file1.write("Citizenship Number:    ")
           file1.write(self.CNo)
           file1.write("\n")
           file1.write("Regsitered Date:            ")
           file1.write(str(self.Date))

           file1.write("\n")
           file1.close()

           tm.showinfo("Successful!!",
                       "Boom!! Boom !! You are successfully registered!! Now yo will be redirected to LoginPage")

           self.master.withdraw()

           self.newWindow = tk.Toplevel(self.master)
           self.app = LoginFrame(self.newWindow)
           self.newWindow.geometry('550x350+450+220')
           self.newWindow.title("Shared Power Login Form")





        #File handling from JSON by using comparative understanding
'''
    
    def onRegister(self):
    
    
        self.name = self.entry_fullname.get()

        self.Username = self.entry_Email.get()
        self.Password = hashlib.sha1(self.entry_password.get().encode()).hexdigest()
        self.CNo = self.entry_citizenshipno.get()
        self.account_selected1 = var_nonP.get()
        self.account_selected2 = var_P.get()
        self.account_selected1 = str(self.account_selected1)
        self.account_selected2 = str(self.account_selected2)
        self.gender_selected = gender_value.get()
        self.country_selected = country.get()
    
    
    
        # json_data = open(file_directory).read()
        # tkinter.messagebox.showinfo("Successful!!","Boom!! Boom !! You are successfully registered!!")
        # Button(root, text='Redirect ', font=("bold", 11), width=20, bg='brown', fg='white')

        self.open_db = json.load(open("database1.txt"))  # Loads the json file as dictionary
        self.profile = [{"Name": self.entry_fullname.get(),
                    "Username": self.entry_Email.get(),
                    "Password": hashlib.sha1(self.entry_password.get().encode()).hexdigest(),
                    # The password from the password entry box is encoded with SHA1 in "Pass" value
                    "CNo": self.entry_citizenshipno.get(),
                    "Gender": self.gender_selected,
                    "Country": self.country_selected,
                    "Account1": self.account_selected1,
                    "Account2": self.account_selected2,
                    "Own_Tools": {},
                    "Hired_Tools": {}
                    }]
        self.open_db[self.entry_fullname.get()] = profile  # Assigning the Name  from entry box as a key
        try:
            json.dump(open_db, open("database.txt",
                                    'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file

            tm.showinfo("Successful!!", "Boom!! Boom !! You are successfully registered!!")

        except:
            tm.showinfo("UnSuccessful!!", "Invalid!! Something went wrong")
            
'''










'''

This is Upload Image class which give the user the function of to upload the desired image of respective tools
while uploading the tools details.  

'''


class UploadImage(Frame):
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.master.resizable(False, False)

    def create_widgets(self):

        self.select = Button(self.master,text='Select Image', font=("arial", 13, "bold"), bg="green", fg='white',command=self.select_image)
        self.select.pack()
        self.canvas = Canvas(self.master, width= 400, height=400, bg="grey")
        self.canvas.pack()

        self.store = Button(self.master, text='Store Image', font=("arial", 13, "bold"), bg="#e37b17", fg='white',
                            command=self.store_image)
        self.store.pack()


    def select_image(self):
        global file_path

        file_path = filedialog.askopenfilename()
        des = Image.open(file_path)
        bg_image = ImageTk.PhotoImage(des)
        self.canvas.bg_image = bg_image
        self.canvas.create_image(200 , 200, image=self.canvas.bg_image)
        print(file_path)

    def store_image(self):



        #print("The selected tool image has been uploaded to our database.")

        self.store = file_path

        file = open("Text File Handling\YUploadTools.txt", "a")
        file.write("ToolImage:    ")
        file.write(self.store)
        file.write("\n")
        file.close()

        tm.showinfo("Successfully Uploaded ToolImage!", "Your selected image is uploaded in ToolImage Database. !! Keep Exploring Shahu")
        self.master.withdraw()

        # print('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = SearchTools(self.newWindow)
        self.newWindow.geometry('650x550+450+140')
        self.newWindow.title("Upload Tools Form")




'''

This is upload Tools class which enables the function of uploading Tool Details into our database which is carried out by
registered user so that the other registered user can hire the tools .

'''

class uploadTools(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=515, y=3)

        self.label_name = Label(master, text="Tool Name",width=20,font=("arial", 17))
        self.label_name.place(x=30,y=165)

        self.entry_toolname = Entry(master,bd =5,font=("arial", 13))
        self.entry_toolname.place(x=280,y=165 ,width=200, height=38)

        self.label_tooldes = Label(master, text="Description",width=20,font=("arial", 17))
        self.label_tooldes.place(x=30,y=235)

        self.entry_tooldes = Entry(master,bd =5, font=("arial", 13))
        self.entry_tooldes.place(x=280,y=235,width=200, height=38)

        self.label_toolcondition = Label(master, text="Condition", width=20, font=("arial", 17))
        self.label_toolcondition.place(x=23, y=305)

        self.entry_toolcondition = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolcondition.place(x=280, y=305, width=200, height=38)

        self.label_rate = Label(master, text="Tool Rate",width=20,font=("arial", 17))
        self.label_rate.place(x=30,y=375)
        self.entry_toolrate = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolrate.place(x=280, y=375, width=90, height=38)

        self.label_fullrate = Label(master, text="Full Day",width=20,font=("arial", 10))
        self.label_fullrate.place(x=243,y=418)

        self.entry_toolrate2 = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolrate2.place(x=390, y=375, width=90, height=38)

        self.label_halfrate = Label(master, text="Half Day",width=20,font=("arial", 10))
        self.label_halfrate.place(x=353,y=418)

        Button(master, text='Upload Tools',font=("arial", 13,"bold"),width=15,bg='#e37b17',fg='white', command=self.upload_info).place(x=298,y=464)

        Button(master, text='Upload Image', font=("arial", 13, "bold"), bg="green", fg='white',
               command=self.upload_image1).place(x=58, y=464)

        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=80, y=512)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=23)

        self.upload12 = PhotoImage(file="Images\pload12.png")

        self.ph = Label(master, image=self.upload12)
        self.ph.place(x=160,y=35)

        master.resizable(False, False)
        master.overrideredirect(True)

    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def upload_image(self):
        print("Lets begin to upload")


    def upload_image1(self):
                tm.showwarning("Before Uploading TooolImage!",
                       "You should upload details of tool first then you need to upload Tool Image.\n If you have uploaded ToolDetails then Click OK  to continue")

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                # self.master = master

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UploadImage(self.newWindow)
                self.newWindow.title("Upload Tools Form")
                # def select_image(self):
                # file_path = filedialog.askopenfilename()
                # return Image.open(file_path)

    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+15')
                self.newWindow.title("Shared Power Login Form")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")


    def upload_info(self):
       # global gender_selected

        #global country_selected
        #global account_selected2, account_selected1
        #global name, Username, Password,CNo

       self.nameTool = self.entry_toolname.get()

       self.ToolDescription = self.entry_tooldes.get()

       self.Toolcondition = self.entry_toolcondition.get()

       self.FullRate = self.entry_toolrate2.get()

       self.HalfRate = self.entry_toolrate.get()

       self.nameTool = self.entry_toolname.get()

       self.list1 = [self.nameTool, self.ToolDescription, self.Toolcondition, self.FullRate, self.HalfRate]
       #print(self.list1)

       self.Dict = {'Name of Tool:': self.nameTool, 'Tool Description:': self.ToolDescription, 'Tool Condition:':self.Toolcondition,'FullDayRate':self.FullRate,'HalfDayRate':self.HalfRate }

       if len(self.nameTool) == 0 and len(self.ToolDescription) == 0 and len(self.Toolcondition) == 0 :
           tm.showerror("Upload Tool Error",
                        "UploadTool is unsucessful. May be one or more field is empty.")
       else:

            self.ToolDescription = self.entry_tooldes.get()

            self.Toolcondition = self.entry_toolcondition.get()

            self.FullRate = self.entry_toolrate2.get()

            self.HalfRate = self.entry_toolrate.get()

            self.Date = date.today()



            file = open("Text File Handling\YUploadTools.txt", "a")

            file.write("\n")
            file.write("    #####Registered User Upload Tools Info#####")
            file.write("\n")
            file.write("\n")

            file.write("Name of Tool:            ")
            file.write(self.nameTool)
            file.write("\n")
            file.write("Tool Description:        ")
            file.write(self.ToolDescription)
            file.write("\n")
            file.write("Tool Condition:          ")
            file.write(self.Toolcondition)
            file.write("\n")
            file.write("Tool Rate:     HalfDay   ")
            file.write(self.FullRate)
            file.write("\n")
            file.write("               Fullday   ")
            file.write(self.HalfRate)
            file.write("\n")
            file.write("Uploaded Date:           ")
            file.write(str(self.Date))
            file.write("\n")


            file.close()

            file1 = open("Text File Handling\YUploadYes.txt", "a+")
            #file1.write(str(self.list1))
            file1.write(str(self.Dict))
            file1.close()

            #with open("uploadYes.txt", "w") as f:
                #json.dump(self.Dict, f)

            tm.showinfo("Successfully Uploaded Tool!", "Now your tool can be hired other Registered User . !! Keep Exploring Shahu")




'''

This is SearchTool Class which gives a function of searching  uploaded tools inorder to get directed
to HireTool GUI for hiring a specific tool.  

'''

class SearchTools(Frame):

    def __init__(self, master):

        global entry_ToolName
        global Searched_Tool

        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=591, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=615, y=3)

        self.label_ToolName = Label(master, text="Tool Name",font=("arial", 22))
        self.label_ToolName.place(x=125,y=140)

        Searched_Tool = StringVar()


        self.entry_ToolName = Entry(master,bd =5, font=("arial", 14), textvariable=Searched_Tool)
        self.entry_ToolName.place(x=296,y=140 ,width=230, height=40)
        self.searched_Tool = self.entry_ToolName.get()

        self.imgi = PhotoImage(file="Images\Vis3.png")
        self.button_vis = Button(master, image=self.imgi, font=("bold", 17),
                                     activebackground="red", command=self.search_results)
        self.button_vis.place(x=508, y=140)

        Button(master, text='Wanna Hire This Tool', font=("arial", 13, "bold"),  bg='#e37b17', fg='white', command=self.hire1).place(x=259,
                                                                                                                  y=470)


        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=140, y=512)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=10)

        self.img1 = PhotoImage(file="Images\search3.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=200,y=5)


        master.resizable(False, False)
        master.overrideredirect(True)

    #def open_terms(self):
        #os.startfile("Terms.txt")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    def hire1(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                # self.master = master
                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = hireTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Upload Tools Form")
                # def select_image(self):
                # file_path = filedialog.askopenfilename()
                # return Image.open(file_path)

    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+22')
                self.newWindow.title("Shared Power Login Form")

    def search_results(self):

        global Searched_Tool

        with open('Text File Handling\YUploadYes.txt', 'r') as f:
            self.d = json.loads(f.read().replace("'", '"'))

        #print (self.d['Name of Tool:'])
        #self.a, self.b, self.c , self.d , self.e= self.d.split(',')
        self.Searched_Tool = self.entry_ToolName.get()
        #print(self.Searched_Tool)

        # print(self.a)
        # print(self.b)
        # print(self.c)
        # print(self.d)
        # print(self.e)


        print(self.d['Name of Tool:'])
        file = open("Text File Handling\YUploadTools.txt", "r")

        self.searchTool = file.read()

        self.yes=self.d['Tool Condition:']


        if self.Searched_Tool and self.Searched_Tool != "            " in self.searchTool:
            self.show_gui = Label(self.master, text=self.searchTool, font=('courier', 12, 'bold'), bg="#0984e3")
            self.show_gui.place(x=44, y=215)
            #self.show_gui.pack(padx=6, pady=200)
        else:
            tm.showerror("Invalid ToolName", "No Such Tool Is Uploaded By Any Registered User In Our Database")


    def searchYes(self):
        self.Searched_Tool = self.entry_ToolName.get()
        return self.Searched_Tool


'''

This is HireTools Class .This will enable a function of hiring a uploaded tool . Registered user can search tool
first and can be redirected to this page too for hiring the specific tool if he doesnt know the tool name.

'''


class hireTools(SearchTools):

    def __init__(self, master):

        global entry_toolname
        # self.showyes = ok.searched_Tool
        # self.var2 = master.var2

        self.master = master
        self.frame = tk.Frame(master)

        # self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17), relief="groove",
                                      activebackground="blue", command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17), relief="groove", activebackground="red",
                                  command=self.back)
        self.button_back.place(x=515, y=3)

        self.label_toolname = Label(master, text="Tool Name", width=20, font=("arial", 17))
        self.label_toolname.place(x=30, y=165)

        with open('Text File Handling\YUploadYes.txt', 'r') as f:
            self.d = json.loads(f.read().replace("'", '"'))


        # self.controller.get_page("searchTools").Searched_Tool.get()
        # label = tk.Label(self, text=VertexNumber)

        # self.searchget = self.object1.searchYes()
        self.entry_toolname = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolname.place(x=280, y=165, width=200, height=38)
        #self.entry_toolname.insert(0, "Wire Cutter")
        self.entry_toolname.insert(0, self.d['Name of Tool:'])
        # self.entry_toolname.insert(0, master.searched_Tool)
        # self.entry_toolname.insert(0, "Wire Cutter")

        self.label_hireDate = Label(master, text="Hire Date", width=20, font=("arial", 17))
        self.label_hireDate.place(x=30, y=235)

        self.Date = date.today()
        self.entry_hireDate = Entry(master, bd=5, font=("arial", 13))
        self.entry_hireDate.place(x=280, y=235, width=200, height=38)
        self.entry_hireDate.insert(0, self.Date)

        self.label_hireDays = Label(master, text="Hire Days", width=20, font=("arial", 17))
        self.label_hireDays.place(x=23, y=305)

        self.entry_hireDays = Entry(master, bd=5, font=("arial", 13))
        self.entry_hireDays.place(x=280, y=305, width=200, height=38)
        self.entry_hireDays.insert(0, " Max 3 Days")

        # self.entry_hireDays.bind("<FocusIn>", hireTools.clear_hireDays)

        self.label_rate = Label(master, text="Tool Rate", width=20, font=("arial", 17))
        self.label_rate.place(x=30, y=375)
        self.tool_rate = Entry(master, bd=5, font=("arial", 13))
        self.tool_rate.place(x=280, y=375, width=90, height=38)
        self.tool_rate.insert(0, "234")

        self.label_fullrate = Label(master, text="Full Day", width=20, font=("arial", 10))
        self.label_fullrate.place(x=243, y=418)

        self.tool_rate2 = Entry(master, bd=5, font=("arial", 13))
        self.tool_rate2.place(x=390, y=375, width=90, height=38)
        self.tool_rate2.insert(0, "123")

        self.label_halfrate = Label(master, text="Half Day", width=20, font=("arial", 10))
        self.label_halfrate.place(x=353, y=418)

        Button(master, text='Hire This Tool', font=("arial", 13, "bold"), width=18, bg='#1f3a93', fg='white'
               , command=self.hired_tools).place(x=210,
                                                 y=464)

        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9),
                             cursor="hand2")
        self.label_6.place(x=80, y=512)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=23)

        self.hire1 = PhotoImage(file="Images\hiretool.png")

        self.hire12 = Label(master, image=self.hire1)
        self.hire12.place(x=173, y=43)

        master.resizable(False, False)
        master.overrideredirect(True)

    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    def hired_tools(self):
        # global gender_selected

        # global country_selected
        # global account_selected2, account_selected1
        # global name, Username, Password,CNo

        self.nameTool = self.entry_toolname.get()

        self.HireDate = self.entry_hireDate.get()

        self.HireDays = self.entry_hireDays.get()

        self.FullRate = self.tool_rate2.get()

        self.HalfRate = self.tool_rate.get()

        if len(self.nameTool) == 0 and len(self.HireDays) == 0 :
            tm.showerror("Upload Tool Error",
                         "UploadTool is unsucessful. May be one or more field is empty.")

        else:

            self.nameTool = self.entry_toolname.get()

            self.HireDate = self.entry_hireDate.get()

            self.HireDays = self.entry_hireDays.get()

            self.FullRate = float(self.tool_rate2.get())

            self.HalfRate = float(self.tool_rate.get())

            self.InsurancePlus = self.HalfRate + 5.00

            self.InsurancePlus2 = self.FullRate + 5.00

            self.Date = date.today()

            file = open("Text File Handling\hiredTools.txt", "a")

            file.write("\n")
            file.write("                  #####Registered User Hired Tools Info#####")
            file.write("\n")
            file.write("\n")

            file.write("Name of Tool:           ")
            file.write(self.nameTool)

            file.write("\n")
            file.write("Hired Date:             ")
            file.write(self.HireDate)

            file.write("\n")
            file.write("Hire Days:              ")
            file.write(self.HireDays)

            file.write("\n")

            file.write("Tool Rate:    HalfDay   $")
            file.write(str(self.FullRate))
            file.write("\n")

            file.write("              Fullday   $")
            file.write(str(self.HalfRate))

            file.write("\n")

            file.write("\n")
            file.close()

            file1 = open("Text File Handling\displayReturn.txt", "a+")
            file1.write(self.nameTool)
            file1.write("\n")

            file1.close()

            file2 = open("Text File Handling\Invoice.txt", "w")

            file2.write("\n")
            file2.write("               #####   Auto generated Invoice Monthly  #####")
            file2.write("\n")
            file2.write("\n")

            file2.write("Name of Tool:                ")
            file2.write(self.nameTool)

            file2.write("\n")
            file2.write("Hired Date:                  ")
            file2.write(self.HireDate)

            file2.write("\n")
            file2.write("Hire Days:                   ")
            file2.write(self.HireDays)

            file2.write("\n")

            file2.write("Tool Rate:    HalfDay        $")
            file2.write(str(self.FullRate))
            file2.write("\n")

            file2.write("              Fullday        $")
            file2.write(str(self.HalfRate))

            file2.write("\n")

            file2.write("InsuranceCharge              $5.00")

            file2.write("\n")
            file2.write("Total:        Fullday        $")
            file2.write(str(self.InsurancePlus))

            file2.write("\n")
            file2.write("              Halfday        $")
            file2.write(str(self.InsurancePlus2))

            file2.write("\n")
            file2.write("Generated Date:               ")
            file2.write(str(self.Date))
            file2.write("\n")

            file2.close()

            tm.showinfo("Hired Tools Sucessful!! ",
                        "Your desired tool has been successfully added to your hired tool list. !!Keep Exploring Shahu!! ")
            self.master.withdraw()

            # print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = UserPanelFrame(self.newWindow)
            self.newWindow.geometry('720x720+350+22')
            self.newWindow.title("Shared Power Login Form")

    def back(self):
        # print(self.showyes)
        # I need make windows itself destroy after clicking on this button and make other window appear in same position
        # self.master = master
        self.master.withdraw()

        # print ('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserPanelFrame(self.newWindow)
        self.newWindow.geometry('720x720+350+22')
        self.newWindow.title("Shared Power Login Form")


'''

This is ReturnTool Class which enables the function of returning a hired tool which is most essential 
in printing the invoice . 

'''


class ReturnTools(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17), relief="groove",
                                      activebackground="blue", command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17), relief="groove", activebackground="red",
                                  command=self.back)
        self.button_back.place(x=515, y=3)

        self.listOfTools = Listbox(master, selectmode=EXTENDED, exportselection=0,font=("arial", 17, "bold")
                                   ,width=30, height=10,bg='#808e9b',fg='white',highlightcolor="green")
        self.listOfTools.place(x=95, y=160)

        self.data = []
        with open("Text File Handling\displayReturn.txt", "r") as f:
            for line in f:
                self.data += line.splitlines()

        # Create your listbox here.
        for i in range(len(self.data)):
            self.listOfTools.insert(i + 1, self.data[i])


        Button(master, text='Return This Tool', font=("arial", 13, "bold"), width=18, bg='#1f3a93', fg='white'
               , command=self.delete_selected_item).place(x=205,
                                                                                                                  y=464)

        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9),
                             cursor="hand2")
        self.label_6.place(x=80, y=512)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        self.img2 = PhotoImage(file="Images\Returnlogo.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=10, y=31)

        self.return1 = PhotoImage(file="Images\ReturnTools.png")

        self.return12 = Label(master, image=self.return1)
        self.return12.place(x=153,y=38)

        master.resizable(False, False)
        master.overrideredirect(True)

    def delete_selected_item(self):

        tm.showwarning("Confirm ReturnTool",
                       "Are You sure want to return this tool ? If you return this tool , this tool will be deleted from "
                       "your hired tool database. ")
        self.indexes = self.listOfTools.curselection()
        for index in self.indexes:
            self.listOfTools.delete(index)



    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")
    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")




    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+22')
                self.newWindow.title("Shared Power Login Form")



'''

This is Return Tool and Payment Class which enables the function of this GUI whhich are returning a tool
and after returning tool the user can only preview invoice and inoreder to print the iinvoice it need to be last
day of month

'''

class payTools(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=515, y=3)

        self.returnTool = PhotoImage(file="Images\Tool2.png")
        self.returnTool1 = Button(master, width=210, height=160, image=self.returnTool,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="pink",
                                activeforeground="green", command=self.return1)
        self.returnTool1.place(x=45, y=168)
        self.ret13 = Label(master, text=" Return Tools ", font=("arial", 16, "bold"))
        self.ret13.place(x=77, y=358)

        #if draw.drawing == False:
            #resetall.config(state=DISABLED)
        #elif draw.drawing == True:
            #resetall.config(state=NORMAL)

        self.pay = PhotoImage(file="Images\invoice12.png")
        self.pay_tools = Button(master, text="Payment & Delivery", width=210, height=160, image=self.pay,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="cyan",
                                activeforeground="green", command=self.print_invoice)
        self.pay_tools.place(x=295, y=168)



        self.pay13 = Label(master, text="  Print Invoice ", font=("arial", 16, "bold"))
        self.pay13.place(x=318, y=358)

        self.thankYou = Label(master, text="Thank You !! For Using Shahu  ", width=30, font=("bold", 23))
        self.thankYou.place(x=20, y=438)

        '''
        self.label_name = Label(master, text="Tool Name",width=20,font=("bold", 13))
        self.label_name.place(x=80,y=130)

        self.entry_name = Entry(master,bd =5)
        self.entry_name.place(x=240,y=130 ,width=180)

        self.label_des = Label(master, text="Description",width=20,font=("bold", 13))
        self.label_des.place(x=68,y=180)

        self.entry_des = Entry(master,bd =5)
        self.entry_des.place(x=240,y=180,width=180)

        self.label_condition = Label(master, text="Condition", width=20, font=("bold", 13))
        self.label_condition.place(x=70, y=230)

        self.entry_condition = Entry(master, bd=5)
        self.entry_condition.place(x=240, y=230, width=180)

        self.label_rate = Label(master, text="Tool Rate",width=20,font=("bold", 13))
        self.label_rate.place(x=70,y=280)
        self.entry_rate = Entry(master, bd=5)
        self.entry_rate.place(x=240, y=280, width=180)
        '''
        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=80, y=512)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=21)

        self.pay1 = PhotoImage(file="Images\Cash.png")

        self.pay12 = Label(master, image=self.pay1)
        self.pay12.place(x=194,y=27)

        master.resizable(False, False)
        master.overrideredirect(True)


    def print_invoice(self):

        self.date=date.today()

        if self.date == self.date:
            tm.showwarning("Something went wrong while generating invoice","Today is not the last of month \n.You cannot print the invoice but inorder to preview invoice click OK ")

            os.startfile("Text File Handling\Invoice.txt")
            file = open("Text File Handling\Invoice.txt", "r")
            self.searchTool = file.read()
            print(self.searchTool)

        # if self.Searched_Tool== "   ":
        # tm.showerror("Invalid ToolName", "No Such Tool Is Uploaded By Any Registered User In Our Database")


        #self.show_gui = Label(self.master, text=self.searchTool, font=('courier', 12, 'bold'), bg="#0984e3")
        #self.show_gui.place(x=18, y=220)



    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+22')
                self.newWindow.title("Shared Power Login Form")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")



    def return1(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                # self.master = master
                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = ReturnTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Upload Tools Form")



'''

This is Insurance Company Profile .Insurance Agent can login in our system by providing their valid 
credentials inorder to start their session in our software. 

'''


class InsuranceCompany(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=515, y=3)
        self.title = Label(master, text="Welcome !! Explore Shahu  ", width=30, font=("bold", 20))
        self.title.place(x=55, y=55)

        self.logout = PhotoImage(file="Images\logout.png")
        self.user_logout = Button(master, image=self.logout, width=55, height=55, cursor="hand1", relief="flat",
                                  activebackground="red", command=self.logOut)
        self.user_logout.place(x=489, y=489)


        self.title2 = Label(master, text=" Insurance Agent Profile", width=30, font=("bold", 17))
        self.title2.place(x=91, y=125)

        self.view = PhotoImage(file="Images\Viewinfo.png")
        self.view_info = Button(master,  width=210, height=160, image=self.view,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="cyan",
                                activeforeground="green", command=self.view_info1)
        self.view_info.place(x=45, y=198)

        self.view13 = Label(master, text=" View User Info ", font=("arial", 16, "bold"))
        self.view13.place(x=70, y=408)


        self.view2 = PhotoImage(file="Images\Viewtool.png")
        self.view_info1 = Button(master, width=210, height=160, image=self.view2,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="cyan",
                                activeforeground="green", command=self.view_info12)
        self.view_info1.place(x=295, y=198)

        self.view132 = Label(master, text="  View All Uploaded Tool", font=("arial", 16, "bold"))
        self.view132.place(x=270, y=408)


        '''
        self.entry_condition = Entry(master, bd=5)
        self.entry_condition.place(x=240, y=230, width=180)

        self.label_rate = Label(master, text="Tool Rate",width=20,font=("bold", 13))
        self.label_rate.place(x=70,y=280)
        self.entry_rate = Entry(master, bd=5)
        self.entry_rate.place(x=240, y=280, width=180)
        '''
        self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=55, font=('Helvetica', 9), cursor="hand2")
        self.label_6.place(x=80, y=512)
        self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=5, y=21)


        master.resizable(False, False)
        master.overrideredirect(True)

    def view_info1(self):
        os.startfile("Text File Handling\database3.txt")

    def view_info12(self):
        os.startfile("Text File Handling\YUploadTools.txt")

        # if self.Searched_Tool== "   ":
        # tm.showerror("Invalid ToolName", "No Such Tool Is Uploaded By Any Registered User In Our Database")


        #self.show_gui = Label(self.master, text=self.searchTool, font=('courier', 12, 'bold'), bg="#0984e3")
        #self.show_gui.place(x=18, y=220)


    def logOut(self):
        #print("This will logout you from user panel.")

        tm.showwarning("Confirm LogOut",
                    "Are You sure want to LogOut from  Shahu:The Ultimate Shared Power? ")

        self.master.withdraw()

        #print('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = LoginFrame(self.newWindow)
        self.newWindow.geometry('550x350+450+220')
        self.newWindow.title("Shared Power Login Form")



    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def back(self):
                tm.showwarning("Confirm Exit",
                       "Are You sure want to exit from  Shahu:The Ultimate Shared Power? ")


        # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = LoginFrame(self.newWindow)
                self.newWindow.geometry('550x350+450+220')
                self.newWindow.title("Shared Power Login Form")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")





root = Tk()
root.geometry('600x370+340+190')
root.title("Shared Power Registration Form")
rf = SplashScreenFrame(root)         #in this i need to change and try to implement all the frames in one coding
root.resizable(False, False)
root.overrideredirect(True)
#root.wm_iconbitmap('Icon1.ico')

'''  

Now this lines of codes are replaced by Kshitij Bajagain because ...these lines are not needed at all because
we are using photos for every windows through Calling Inside each classes(windows) 

img1= PhotoImage(file="regfinal1.png")

lab1=Label(root, image=img1)
lab1.place(x=160,y=35)

img2= PhotoImage(file="yup1.png")

lab2=Label(root, image=img2)
lab2.place(x=20,y=23)
'''

root.mainloop()