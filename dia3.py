# %% 
import numpy as np
import pandas as pd
import seaborn as sns
# %%
lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)

#print(lista * 10)
# print(nplista * 2)
# print(pdlista * 2)

# %%
df = pd.read_csv("insurance.csv")
#print(df)

# %%
#print(df.tail(3))
#df['age'][0:1]
#df['bmi'][0:1]
#df[10:11]

# %% 
sns.set_theme(style="white")
sns.displot(x="region", data=df)