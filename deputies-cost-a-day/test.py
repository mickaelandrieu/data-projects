import matplotlib.pyplot as plt

deputies = {
    "LREM": 299,
    "LR": 104,
    "MODEM": 46,
    "SOC": 30,
    "UDI-AGIR": 27,
    "LT": 20,
    "FI": 17,
    "NI": 18,
    "GDR": 16
    }

labels = deputies.keys()
values = deputies.values()

figure, axes = plt.subplots()
axes.axis("equal")
axes.pie(values,
    labels = labels,
    autopct="%1.1f%%")
plt.title("Répartition des députes par groupe parlementaire")
plt.show()