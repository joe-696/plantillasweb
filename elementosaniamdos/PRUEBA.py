import pandas as pd
import matplotlib.pyplot as plt

# Crea un DataFrame con los datos de producción
data = {
    'Año': [2010, 2011, ..., 2022],
    'Producción (millones de barriles)': [5100, 5300, ..., 7600]
}
df = pd.DataFrame(data)

# Crea la gráfica de líneas
ax = df.plot.line(x='Año', y='Producción (millones de barriles)')
plt.xlabel('Año')
plt.ylabel('Producción (millones de barriles)')
plt.title('Producción de Petróleo en Estados Unidos (2010-2022)')
plt.grid(True)
plt.show()
