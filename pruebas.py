import matplotlib.pyplot as plt

# Valores de y para graficar
y_values = range(-10, 11)  # Valores de y desde -10 hasta 10

# Valores constantes de x
x_values = [69] * len(y_values)

# Graficar los puntos y la línea vertical
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, 'bo')  # Puntos en la línea
plt.axvline(x=69, color='r', linestyle='--')  # Línea vertical x = 69

# Configurar la gráfica
plt.title('Línea Recta Vertical x = 69')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.xlim(60, 80)
plt.ylim(-10, 10)
plt.grid(True)
plt.show()
