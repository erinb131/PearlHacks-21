import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from winsound import *
import pygame
import webbrowser
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

def callback(url):
    webbrowser.open_new(url)

pygame.mixer.init()
def play_music_rain():
    pygame.mixer.music.load("mixkit-forest-rain-loop-1225.wav")
    pygame.mixer.music.play()

pygame.mixer.init()
def play_music_wind():
    pygame.mixer.music.load("mixkit-campfire-night-wind-1736.wav")
    pygame.mixer.music.play()

pygame.mixer.init()
def play_music_waves():
    pygame.mixer.music.load("mixkit-close-sea-waves-loop-1195.wav")
    pygame.mixer.music.play()

pygame.mixer.init()
def play_music_fire():
    pygame.mixer.music.load("campfire.wav")
    pygame.mixer.music.play()

pygame.mixer.init()
def play_music_hike():
    pygame.mixer.music.load("mixkit-crunchy-road-fast-walking-loop-1274.wav")
    pygame.mixer.music.play()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GradeCalc, MentalHealth, CoursesZooms, Sounds, ToDos, ImportantLinks):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        label = tk.Label(self, text="Welcome to CovidCarolina", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

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
        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=5)
        button6.pack(pady=5)


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
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()