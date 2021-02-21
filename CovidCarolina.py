import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from winsound import *
import pygame
import webbrowser

import datetime
import time

def callback(url):
    webbrowser.open_new(url)

pygame.mixer.init()
def play_music_rain():
    pygame.mixer.music.load("mixkit-forest-rain-loop-1225.wav")
    pygame.mixer.music.play(-1)

pygame.mixer.init()
def play_music_wind():
    pygame.mixer.music.load("mixkit-campfire-night-wind-1736.wav")
    pygame.mixer.music.play(-1)

pygame.mixer.init()
def play_music_waves():
    pygame.mixer.music.load("mixkit-close-sea-waves-loop-1195.wav")
    pygame.mixer.music.play(-1)

pygame.mixer.init()
def play_music_fire():
    pygame.mixer.music.load("Crackling_Fire.wav")
    pygame.mixer.music.play(-1)

pygame.mixer.init()
def play_music_hike():
    pygame.mixer.music.load("mixkit-crunchy-road-fast-walking-loop-1274.wav")
    pygame.mixer.music.play(-1)

pygame.mixer.init()
def play_silence():
    pygame.mixer.music.load("silence.wav")
    pygame.mixer.music.play(-1)


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, StartPage, GradeCalc, MentalHealth, CoursesZooms, Sounds, ToDos, ImportantLinks):
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
        tk.PhotoImage(file="bacteria.png"))


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
        button6 = tk.Button(self, text="Important Links",
                            command=lambda: controller.show_frame("ImportantLinks"))

        label_time = tk.Label(self, text="The time in Chapel Hill is " +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=5)
        button6.pack(pady=5)
        label_time.pack(pady=5)


class GradeCalc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Grade Calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to the main page",
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
        button = tk.Button(self, text="Go back to the main page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=5)


class CoursesZooms(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Courses and Zoom Links", font=controller.title_font)
        label.pack()
<<<<<<< HEAD

        button = tk.Button(self, text="Go to the start page",
=======
        button = tk.Button(self, text="Go back to the main page",
>>>>>>> 7240d0cc417ffff19a80600cda6c595875a71c01
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=15)

        def click():
            added_class = my_class.get() + "\n" + my_days.get() + "\n" + my_time.get() + "\n" + my_zoom_link.get() + "\n" + my_zoom_pwd.get()
            class_data.delete(0.0, tk.END)
            new_class.append(added_class)
            class_data.insert(tk.END, new_class)


        class_name = tk.Label(self, text="Name of Class:", font=("Helvetica", 12), fg="royalblue", bg="lightblue")
        class_name.pack()

        my_class = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_class, font=("Helvetica", 12), width=30)
        password_entry_box.focus_set()
        password_entry_box.pack()

        days = tk.Label(self, text="Days:", font=("Helvetica", 12), fg="royalblue", bg="lightblue")
        days.pack()

        my_days = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_days, font=("Helvetica", 12), width=30)
        password_entry_box.focus_set()
        password_entry_box.pack()

        time = tk.Label(self, text="Time:", font=("Helvetica", 12), fg="royalblue", bg="lightblue")
        time.pack()

        my_time = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_time, font=("Helvetica", 12), width=30)
        password_entry_box.focus_set()
        password_entry_box.pack()

        zoom_link = tk.Label(self, text="Zoom Link:", font=("Helvetica", 12), fg="royalblue", bg="lightblue")
        zoom_link.pack()

        my_zoom_link = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_zoom_link, font=("Helvetica", 12), width=30)
        password_entry_box.focus_set()
        password_entry_box.pack()

        zoom_pwd = tk.Label(self, text="Zoom Password (type \"N/A\" if none):", font=("Helvetica", 12), fg="royalblue", bg="lightblue")
        zoom_pwd.pack()

        my_zoom_pwd = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_zoom_pwd, font=("Helvetica", 12), width=30)
        password_entry_box.focus_set()
        password_entry_box.pack()

        submit_btn = tk.Button(self, text="Add Class", command=click)
        submit_btn.pack(pady=15)

        new_class: List[str] = []

        space_label = tk.Label(self, height=6, bg="light blue")
        space_label.pack(pady=10)


        label = tk.Label(self, 
                        text="Monday              Tuesday            Wednesday           Thursday              Friday", 
                        font=controller.title_font, bg="lightblue")
        label.pack()

        space_label = tk.Label(self, height=6, bg="light blue")
        space_label.pack(padx=150, side="left")

        class_data = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        class_data.pack(side = "left")

        class_data2 = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        class_data2.pack(side = "left")

        class_data3 = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        class_data3.pack(side = "left")

        class_data4 = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        class_data4.pack(side = "left")

        class_data5 = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        class_data5.pack(side = "left")
    

class Sounds(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Calming Sounds", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top", fill="x", pady=10)
        label_body = tk.Label(self, text="Relax and click a button below to be transported to bliss.")
        label_body.pack(pady=5)

        button_wind = tk.Button(self, text="Wind", command=play_music_wind)
        button_wind.pack(pady=5)

        button_waves = tk.Button(self, text="Waves", command=play_music_waves)
        button_waves.pack(pady=5)

        button_rain = tk.Button(self, text="Rain", command=play_music_rain)
        button_rain.pack(pady=5)

        button_hike = tk.Button(self, text="Hike", command=play_music_hike)
        button_hike.pack(pady=5)

        button_fire = tk.Button(self, text="Fire", command=play_music_fire)
        button_fire.pack(pady=5)

        button_stop = tk.Button(self, text="Stop Music", command=play_silence)
        button_stop.pack(pady=5)

        button = tk.Button(self, text="Go back to the main page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=5)


class ToDos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="To-Do List", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go back to the main page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class ImportantLinks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Important Links", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label_body = tk.Label(self, text="All the links you need for success...in one page!")
        label_body.pack()
        sakai_button = tk.Button(self, text="Sakai", command=lambda:callback("sakai.unc.edu"))
        sakai_button.pack(pady=5)
        connectcarolina_button = tk.Button(self, text="ConnectCarolina", command=lambda:callback("https://connectcarolina.unc.edu/"))
        connectcarolina_button.pack(pady=5)
        coursicle_button = tk.Button(self, text="Coursicle", command=lambda:callback("https://www.coursicle.com/unc/"))
        coursicle_button.pack(pady=5)
        groupme_button = tk.Button(self, text="GroupMe", command=lambda:callback("https://web.groupme.com/chats"))
        groupme_button.pack(pady=5)
        google_docs_button = tk.Button(self, text="Google Docs", command=lambda:callback("https://www.google.com/docs/about/"))
        google_docs_button.pack(pady=5)
        heelmail_button = tk.Button(self, text="Heelmail", command=lambda:callback("http://heelmail.unc.edu/"))
        heelmail_button.pack(pady=5)
        netflix_button = tk.Button(self, text="Netflix", command=lambda:callback("https://www.netflix.com/browse"))
        netflix_button.pack(pady=5)
        button = tk.Button(self, text="Go back to the main page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()