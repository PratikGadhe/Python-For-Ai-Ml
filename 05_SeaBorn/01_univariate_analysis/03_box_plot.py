import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('penguins')
data.describe()

sns.boxplot(data , x = 'species' , y = 'body_mass_g' , 
            hue = 'sex')
sns.set_style('darkgrid')