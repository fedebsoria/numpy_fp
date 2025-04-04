import numpy as np

min_temps = [12, 14, 11, 10, 9, 15, 13]  # Mínimas
max_temps = [22, 24, 20, 19, 18, 25, 23]  # Máximas

#1.	Convertir las listas a arrays de NumPy.

tempsMinNP = np.array(min_temps)
tempsMaxNP = np.array(max_temps)

print(type(tempsMinNP))
print(type(tempsMaxNP))

#2.	Calcular la temperatura promedio de la semana para mínimas y máximas.

minPromedio = np.mean(tempsMinNP)
maxPromedio = np.mean(tempsMaxNP)

print("La temp min promedio es {}".format(minPromedio))
print("La temp max promedio es {}".format(maxPromedio))

#3.	Determinar la temperatura mínima y máxima de la semana.

maxSemana = np.max(tempsMaxNP)
minSemana = np.min(tempsMinNP)

print("La temp. más alta de la semana fue: {}".format(maxSemana))
print("La temp. más baja de la semana fue: {}".format(minSemana))

#4.	Calcular la amplitud térmica diaria (diferencia entre temperatura máxima y mínima para cada día).
ampliTerm = np.subtract(tempsMaxNP, tempsMinNP)

for i in ampliTerm:
    print("Amplitud terminca diaria: {}".format(i))

#5.	Determinar el día con la mayor amplitud térmica.
dia_max_ampli = np.argmax(ampliTerm)

print("El día con mayor amplitud térmica fue el {}º día".format(dia_max_ampli+1))
