import pandas
import matplotlib.pyplot as plt


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
print(atzime_list)
var_list = dati["Vards"].to_list()
print(var_list)
fig, ax = plt.subplots()

fruits = [atzime_list]
counts = [var_list]


ax.bar(1,10)

plt.show()