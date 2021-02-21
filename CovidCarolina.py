import tkinter as tk
from tkinter import font as tkfont
from typing import List
from prettytable import PrettyTable
from tkinter import *
from tkinter import ttk
from winsound import *
import pygame
import webbrowser
import datetime
import time
from typing import List, Dict

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
        button.pack(pady=5)
                
        def gradecalc_main() -> None:
            """Calculates grades based on inputs from the user."""
            categories: List[str] = [] 
            all_grades: Dict[str, Dict[str, float]] = {} 
            weights: Dict[str, int] = {}
            num_assignments: Dict[str, int] = {}
            assignment_lists: Dict[str, List[str]] = {}
            category_avgs: Dict[str, float] = {}
            weighted_avgs: List[float] = []

            num_categories: int = int(input("# of categories in final grade breakdown: "))

            for i in range(num_categories):
                category: str = input("Name of Category: ")
                categories.append(category)
                weights[category] = int(input("Percent of Final Grade: ")) / 100
                num_assignments[category] = int(input("Number of Assignments in Category: "))

            for item in categories:
                category_grades: Dict[str, float] = {}
                category_assignments: List[str] = []
                grade_list: List[float] = []

                print(item + " Grades")

                for j in range(num_assignments[item]):
                    assignment: str = input("Assignment Name: ")
                    category_assignments.append(assignment)
                    grade: float = float(input("Grade: "))
                    category_grades[assignment] = grade
                    grade_list.append(grade)

                all_grades[item] = category_grades
                assignment_lists[item] = category_assignments
                category_avgs[item] = sum(grade_list) / num_assignments[item]
                weighted_avgs.append(category_avgs[item] * weights[item])

            # current_grade: float = 0.0
            final_grade: float = sum(weighted_avgs)
            letter_grade: str = get_letter_grade(final_grade)

            create_treeview(categories, category_avgs, weights, assignment_lists, all_grades)

            grade_label = tk.Label(self, text=("Final Grade:    " + str(final_grade) + "    " + letter_grade), 
                                    font=controller.title_font)
            grade_label.pack(pady=5)

        def get_letter_grade(num_grade: float) -> str:
            """Takes a numerical grade as input and returns a letter grade
            according to the UNC standard grading scale."""
            letter: str = ""

            if num_grade >= 93:
                letter = "A"
            elif num_grade >= 90:
                letter = "A-"
            elif num_grade >= 87:
                letter = "B+"
            elif num_grade >= 83:
                letter = "B"
            elif num_grade >= 80:
                letter = "B-"
            elif num_grade >= 77:
                letter = "C+"
            elif num_grade >= 73:
                letter = "C"
            elif num_grade >= 70:
                letter = "C-"
            elif num_grade >= 65:
                letter = "D+"
            elif num_grade >= 60:
                letter = "D"
            else:
                letter = "F"

            return letter

        def create_treeview(headers: List[str], avg_grades: Dict[str, float], 
                            weights_dict: Dict[str, int], children: Dict[str, List[str]],
                            gradebook: Dict[str, Dict[str, float]]) -> None:
            """Displays the input and calculated output from GradeCalc as a table."""
            my_tree = ttk.Treeview(self)

            # Define columns
            my_tree["columns"] = ["Gradebook Item", "Grade", "Weight"]

            # Format columns
            my_tree.column("#0", width=120, minwidth=25)
            my_tree.column("Gradebook Item", anchor=W, width=120)
            my_tree.column("Grade", anchor=CENTER, width=80)
            my_tree.column("Weight", anchor=W, width=120)

            # Create headings
            my_tree.heading("#0", text="Label", anchor=W)
            my_tree.heading("Gradebook Item", text="Gradebook Item", anchor=W)
            my_tree.heading("Grade", text="Grade", anchor=CENTER)
            my_tree.heading("Weight", text="Weight", anchor=W)

            # Add data
            count: int = 0
            count2: int = len(headers) + count

            for k in headers:
                my_tree.insert(parent="", index="end", iid=count, text="Category", 
                                values=(k, str(avg_grades[k]), str(weights_dict[k])))

                for child in children[k]:
                    my_tree.insert(parent=count, index="end", iid=count2, 
                                    text="Assignment", values=(child, gradebook[k][child], "-"))
                    count2 += 1
                    
                count += 1

            # Pack to the screen
            my_tree.pack(pady=20)

        button = tk.Button(self, text="Calculate Class Grades", command=gradecalc_main())
        button.pack(pady=10)


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

        button = tk.Button(self, text="Go back to the main page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=15)

        def undelimit(delimited: str) -> List[str]:
            """Returns a list of the groups of chracters in the given string separated by the commas."""
            undelimited: List[str] = []
            item: str = ""

            for char in delimited:
                if char == " ":
                    undelimited.append(item)
                    item = ""
                else:
                    item += char

            undelimited.append(item)

            return undelimited


        def click():
            added_class = my_class.get() + "\n" + my_time.get() + "\n" + my_zoom_link.get() + "\n" + my_zoom_pwd.get() + "\n\n"
            days_of_week = undelimit(my_days.get())
 
            i = 0
            while i < len(days_of_week):
                if days_of_week[i] == "Monday":
                    new_class.append(added_class)
                    monday.insert(tk.END, new_class[len(new_class)-1])
                elif days_of_week[i] == "Tuesday":
                    new_class.append(added_class)
                    tuesday.insert(tk.END, new_class[len(new_class)-1])
                elif days_of_week[i] == "Wednesday":
                    new_class.append(added_class)
                    wednesday.insert(tk.END, new_class[len(new_class)-1])
                elif days_of_week[i] == "Thursday":
                    new_class.append(added_class)
                    thursday.insert(tk.END, new_class[len(new_class)-1])
                elif days_of_week[i] == "Friday":
                    new_class.append(added_class)
                    friday.insert(tk.END, new_class[len(new_class)-1])

                i += 1


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

        monday = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        monday.pack(side = "left")

        tuesday = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        tuesday.pack(side = "left")

        wednesday = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        wednesday.pack(side = "left")

        thursday = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        thursday.pack(side = "left")

        friday = tk.Text(self, font=("Helvetica", 12), width=22, height=26)
        friday.pack(side = "left")
    

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