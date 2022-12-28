import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from PackageCounter import countPackets


window = tk.Tk()


def createDiagramm():
    matplotlib.use('TkAgg')
    pie = plt.figure(figsize=(4, 4), facecolor="#F0F0F0")
    pie.labels = ['ARP', 'DHCP', 'DNS', 'TCP', 'UDP', 'Other']
    filepath = filedialog.askopenfilename()
    pie.sizes = countPackets(filepath)
    pie.patches, pie.text2, pie.text1 = plt.pie(pie.sizes,
                                                labels=pie.labels,
                                                autopct='%1.1f%%',
                                                shadow=True,
                                                startangle=90,
                                                pctdistance=1.4,
                                                textprops={'fontsize': 8, 'color': '#000080'},
                                                wedgeprops={'lw': 1, 'ls':'--', 'edgecolor':"k"},
                                                rotatelabels=True
                                                )
    plt.axis('equal')

    canvas_statis = FigureCanvasTkAgg(pie, window)
    canvas_statis.get_tk_widget().place(x=10, y=60)

    colors = [["r", "b", "g"][int(np.random.randint(0, 3, 1))] for _ in pie.sizes]
    bar = plt.figure(figsize=(4, 4), facecolor="#F0F0F0")
    bar.patches = plt.bar(pie.labels,
                                                pie.sizes,
                                                alpha=0.6,
                                                bottom=2,
                                                color=colors,
                                                edgecolor="k",
                                                linewidth=2)
    figureCanvas = FigureCanvasTkAgg(bar, window)
    figureCanvas.get_tk_widget().place(x=400, y=60)




def execMainWindow():
    window.title("MOKS Lemaykin KI21-01-11M")
    window.geometry('800x600')

    create_button = ttk.Button(text="Create diagramm", command=createDiagramm)
    create_button.grid(column=1, row=1, padx=10, pady=10)

    window.mainloop()
