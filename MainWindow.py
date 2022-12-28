import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PackageCounter import countPackets


window = tk.Tk()


def createPieDiagramm():
    matplotlib.use('TkAgg')
    pie = plt.figure(figsize=(3.2, 3.2), facecolor="#F0F0F0")
    pie.labels = ['ARP', 'DHCP', 'DNS', 'TCP', 'UDP', 'Other']
    filepath = filedialog.askopenfilename()
    pie.sizes = countPackets(filepath)
    pie.patches, pie.text2, pie.text1 = plt.pie(pie.sizes,
                                                labels=pie.labels,
                                                autopct='% 3.1f %%',
                                                shadow=True,
                                                startangle=90,
                                                pctdistance=1.4,
                                                textprops={'fontsize': 8, 'color': '#000080'}
                                                )
    plt.axis('equal')

    canvas_statis = FigureCanvasTkAgg(pie, window)
    canvas_statis.get_tk_widget().place(x=10, y=60)



def execMainWindow():
    window.title("MOKS Lemaykin KI21-01-11M")
    window.geometry('600x400')

    create_button = ttk.Button(text="Create diagramm", command=createPieDiagramm)
    create_button.grid(column=1, row=1, padx=10, pady=10)

    window.mainloop()
