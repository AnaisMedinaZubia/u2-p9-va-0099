# Anais Medina NC 0099 fecha 3 noviembre 2026
import matplotlib.pyplot as plt
import numpy as pd

materias = ['ML', 'VA', 'Matematicas', 'Ciencias', 'Humanidades']
califas = [90, 84, 100, 60, 70]

plt.pie(califas, labels=materias, autopct='%1.1f%%', startangle=90)
plt.title("grafica de califas 0099")
plt.xlabel(materias)
plt.ylabel(califas)
plt.show()

print("Anais Medina NC 0099")