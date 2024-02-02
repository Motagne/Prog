import pandas
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np

dati = pandas.read_csv("Tabula.csv",encoding='utf-8')
skaitlis=(dati["Atzime"].mean())
print("Vidējā atzīme")
print(skaitlis)
print("Vidējā noapaļotā atzīme")
print(skaitlis.round())

pun=(dati["Punkti"].mean())
print("Vidējie punkti")
print(pun)
print("Vidējie noapaļotie punkti")
print(pun.round())

proc=(dati["Procenti"].mean())
print("Vidējie procenti")
print(proc)
print("Vidējie noapaļotie procenti")
print(proc.round())

atzime_list = dati["Atzime"].to_list()
print("Skolēnu atzīmju lists")
print(atzime_list)
var_list = dati["Vards"].to_list()
print("Skolēnu vārdu lists")
print(var_list)


sg.theme('DarkBrown1')
layout = [[sg.Text('Ieraksti "procenti", ja gribi iegūt vidējos procentus, ieraksti "atzime", ja gribi iegūt vidējo atzīmi, ieraksti "punkti", ja gribi iegūt vidējos punktus ')],
         [sg.InputText(key='-IN-')],
         [sg.Submit(), sg.Cancel()]]
window = sg.Window('Window Title', layout)
event, values = window.read()
window.close()
text_input = values['-IN-']
if text_input.lower() == 'procenti':
    sg.popup('Vidējie noapaļotie procenti ir', proc.round())
if text_input.lower() == 'atzime':
    sg.popup('Vidējā noapaļotā atzīme ir', skaitlis.round())
if text_input.lower() == 'punkti':
    sg.popup('Vidējie noapaļotie punkti ir', pun.round())

x = np.array(['Maksims', 'Zanne', 'Guntars', 'Anna', 'Sandijs', 'Zanete', 'Vilijs', 'Elija', 'Janis', 'Orests', 'Eduarts', 'Lolija', 'Harijs', 'Lolita', 'Larijs', 'Terijs', 'Alise', 'Katrina', 'Zans', 'Davis', 'Jekabs', 'Zita', 'Bobs'])
y = np.array([8, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2])

plt.bar(x,y)
plt.xlabel('Vārdi')  
plt.ylabel('Atzīmes')    
plt.title('Skolēnu atzīmes')  
plt.show()
