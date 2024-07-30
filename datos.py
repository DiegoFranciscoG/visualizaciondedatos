import pandas as pd
import matplotlib.pyplot as plt


datos = pd.read_csv('Iris.csv')


print(datos.shape)  
print(datos.head())  
print(datos.info())  

# Análisis exploratorio
print(datos.describe())  


plt.hist(datos['sepal length (cm)'])  
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Sepal Length')
plt.show()

plt.scatter(datos['sepal length (cm)'], datos['sepal width (cm)'])  
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Scatter Plot de Sepal Length vs Sepal Width')
plt.show()