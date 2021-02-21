import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from winsound import *
import pygame
import webbrowser
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

def callback(url):
    webbrowser.open_new(url)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, StartPage, GradeCalc, MentalHealth, CoursesZooms, Sounds, ToDos):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller

        self.controller.title("CovidCarolina")
        self.controller.state("zoomed")
        self.controller.iconphoto(False,
        tk.PhotoImage(file="C:/Users/erinb/PearlHacks-21/bacteria.png"))

        welcomeBanner = tk.Label(self, text="Welcome to CovidCarolina", font=("Helvetica", 45, "bold"), fg="royalblue")
        welcomeBanner.pack(side="top", fill="x", pady=70)

        space_label = tk.Label(self, height=4, bg="light blue")
        space_label.pack()

        onyen_label = tk.Label(self, text="Enter your ONYEN", font=("Helvetica", 18), fg="royalblue", bg="lightblue")
        onyen_label.pack(pady=10)

        my_onyen = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_onyen, font=("Helvetica", 12), width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=6)

        space_label2 = tk.Label(self, height=1, bg="light blue")
        space_label2.pack()

        password_label = tk.Label(self, text="Enter your password", font=("Helvetica", 18), fg="royalblue", bg="lightblue")
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, font=("Helvetica", 12), width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=6)

        def handle_focus_in(_):
            password_entry_box.configure(fg="black", show="*")

        password_entry_box.bind("<FocusIn>", handle_focus_in)


        def check_password():
            if my_password.get() == "#goHeels":
                controller.show_frame("StartPage")
            else:
                incorrect_password_label["text"]="Incorrect ONYEN/Password"

        enter_button=tk.Button(self, text="Enter", command=check_password, relief="groove", borderwidth=3, width=12, height=1)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self, text="", font=("Helvetica", 12), fg="midnightblue", bg="lightblue", anchor="n")
        incorrect_password_label.pack(fill="both", expand=True)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller

        # self.controller.title("CovidCarolina")
        # self.controller.state("zoomed")
        # self.controller.iconphoto(False,
        # tk.PhotoImage(file="C:/Users/erinb/PearlHacks-21/bacteria.png"))

        welcomeBanner = tk.Label(self, text="Welcome to CovidCarolina", font=("Helvetica", 45, "bold"), foreground="royalblue")
        welcomeBanner.pack(side="top", fill="x", pady=25)

        label_small = tk.Label(self, text="The organization app in the retro ConnectCarolina style you know and love.")
        label_small.pack()

        button1 = tk.Button(self, text="Grade Calculator",
                            command=lambda: controller.show_frame("GradeCalc"))
        button2 = tk.Button(self, text="Mental Health",
                            command=lambda: controller.show_frame("MentalHealth"))
        button3 = tk.Button(self, text="Courses and Zoom Links",
                            command=lambda: controller.show_frame("CoursesZooms"))
        button4 = tk.Button(self, text="Calming Sounds",
                            command=lambda: controller.show_frame("Sounds"))
        button5 = tk.Button(self, text="To-Do List",
                            command=lambda: controller.show_frame("ToDos"))
        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=5)


class GradeCalc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Grade Calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class MentalHealth(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Mental Health", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label_body = tk.Label(self, text="Your mental health is important. Below are some resources you might find helpful. ")
        label_body.pack()
        caps_button = tk.Button(self, text="UNC CAPS", command=lambda:callback("caps.unc.edu"))
        caps_button.pack(pady=5)
        sevencups_button = tk.Button(self, text="7 Cups", command=lambda:callback("www.7cups.com/"))
        sevencups_button.pack(pady=5)
        findatherapist_button = tk.Button(self, text="Find a Therapist", command=lambda:callback("https://www.psychologytoday.com/us/therapists"))
        findatherapist_button.pack(pady=5)
        self_care_tips_button = tk.Button(self, text="Self Care Tips", command=lambda:callback("https://www.everydayhealth.com/wellness/top-self-care-tips-for-being-stuck-at-home-during-the-coronavirus-pandemic/"))
        self_care_tips_button.pack(pady=5)
        suicide_hotline_button = tk.Button(self, text="Suicide Hotline", command=lambda:callback("https://suicidepreventionlifeline.org/"))
        suicide_hotline_button.pack(pady=5)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=5)


class CoursesZooms(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Courses and Zoom Links", font=controller.title_font)
        label.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class Sounds(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Calming Sounds", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top", fill="x", pady=10)
        label_body = tk.Label(self, text="Relax and click a button below to be transported to bliss.")
        label_body.pack(pady=5)

        button_fire = tk.Button(self, text="Fire")
        button_fire.pack(pady=5)

        button_wind = tk.Button(self, text="Wind")
        button_wind.pack(pady=5)

        button_waves = tk.Button(self, text="Waves")
        button_waves.pack(pady=5)

        button_rain = tk.Button(self, text="Rain")
        button_rain.pack(pady=5)

        button_piano = tk.Button(self, text="Piano")
        button_piano.pack(pady=5)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=5)


class ToDos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="To-Do List", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()