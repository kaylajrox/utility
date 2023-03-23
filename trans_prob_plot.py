"""
Author: Kayla Rodriguez
Purpose: Plot the transmission probability of various aspect ratios using vac tech data
"""
import pandas as pd
import matplotlib.pyplot as plt

# table 3.1 pg 36 in A User's Guide to Vacuum Technology
TRANS_PROB_DATA_FILE = 'trans_prob_round_pipes.csv'

data = pd.read_csv(TRANS_PROB_DATA_FILE)

LAST_POINTS_RM = 2

all_aspect_ratios = data['l/d']
aspect_ratios = all_aspect_ratios[: len(all_aspect_ratios)-LAST_POINTS_RM]
trans_prob_all = data['a']
trans_prob = trans_prob_all[: len(all_aspect_ratios)-LAST_POINTS_RM]

fig = plt.figure()
plt.ylabel("Transmission Probability a",fontsize=12)
plt.xlabel("Aspect ratio l/d",fontsize=12)
plt.title("Transmission Probability for Round Pipes")
plt.plot(aspect_ratios,trans_prob,'m.')
plt.grid()
plt.show()
