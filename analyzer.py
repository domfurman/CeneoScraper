import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep='\n')
product_id = input('Podaj identyfikator produktu: ')

opinions = pd.read_json(f'opinions/{product_id}.json')
#print(opinions)

opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",", ".")))
opinions_count = len(opinions.index)
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean().round(2)

recommendation = opinions.recommendation.value_counts(dropna = False).sort_index()
recommendation.plot.pie(label="",
 autopct="%1.1f%%",
  colors = ["crimson", "forestgreen", "lightskyblue"],
  labels = ["Nie polecam", "Polecam", "Nie mam zdania"]
  )
plt.title("Rekomendacja")
plt.savefig(f'plots/{product_id}_recommendations.png')
plt.close()

stars = opinions.stars.value_counts().sort_index().reindex(list(np.arange(0, 5.5, 0.5)), fill_value=0)
stars.plot.bar()
plt.title("Ocena produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.xticks(rotation=0)
plt.savefig(f'plots/{product_id}_stars.png')
plt.close()