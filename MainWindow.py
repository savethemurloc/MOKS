import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


window = tk.Tk()
window.title("MOKS Lemaykin KI21-01-11M")
window.geometry('600x400')

matplotlib.use('TkAgg')
pie = plt.figure(figsize=(2.2, 2.2), facecolor="#F0F0F0")
pie.labels = ['lol', 'kek', 'cheburek']
pie.sizes = [5, 6, 7]
pie.colors = ['green', 'red', 'blue']
pie.explode = (0.05, 0.05, 0.05)
pie.patches, pie.text2, pie.text1 = plt.pie(pie.sizes,
                                            labels=pie.labels,
                                            explode=pie.explode,
                                            colors=pie.colors,
                                            autopct='% 3.1f %%',
                                            shadow=True,
                                            startangle=90,
                                            pctdistance=1.4,
                                            textprops={'fontsize': 8, 'color': '#000080'}
                                            )
plt.axis('equal')

canvas_statis = FigureCanvasTkAgg(pie, window)
canvas_statis.get_tk_widget().place(x=40, y=40)
window.mainloop()