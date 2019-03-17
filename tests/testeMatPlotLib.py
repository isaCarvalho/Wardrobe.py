import matplotlib.pyplot as plt
import pandas as pd

aux = { "x": [1.93, 1.64, 1.88, 1.82, 1.84, 1.82, 2.00], 
        "y": [20.99, 100.00, 33.33, 65.4, 81, 90, 90.1] 

        }

grafico = pd.DataFrame(aux)

grafico.plot(x="x", y="y")
plt.figure(figsize=(12, 6))
plt.show()