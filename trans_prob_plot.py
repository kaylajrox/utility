import pandas as pd
import numpy as np
from utlility_func import find_nearest_idx
import matplotlib.pyplot as plt

# table 3.1 pg 36 in A User's Guide to Vacuum Technology
trans_prob_round_tube_data_file = 'trans_prob_round_pipes.csv'

data = pd.read_csv(trans_prob_round_tube_data_file)

last_points_del = 2

all_aspect_ratios = data['l/d']
aspect_ratios = all_aspect_ratios[: len(all_aspect_ratios)-last_points_del]
trans_prob_all = data['a']
trans_prob = trans_prob_all[: len(all_aspect_ratios)-last_points_del]

fig = plt.figure()
plt.ylabel("Transmission Probability a",fontsize=12)
plt.xlabel("Aspect ratio l/d",fontsize=12)
plt.title("Transmission Probability for Round Pipes")
plt.plot(aspect_ratios,trans_prob,'m.')
plt.grid()
fig.show()