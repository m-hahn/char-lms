
accLSTM = [[[0.7, 0.21, 0.09], [0.06, 0.9, 0.03], [0.2, 0.21, 0.59]],
           [[0.63, 0.2, 0.17], [0.15, 0.78, 0.07], [0.31, 0.21, 0.49]],
           [[0.67, 0.19, 0.14], [0.16, 0.76, 0.07], [0.31, 0.22, 0.48]],
           [[0.888646288209607, 0.036244541484716154, 0.07510917030567686], [0.4166298098186643, 0.518796992481203, 0.06457319770013269], [0.5418541854185418, 0.062106210621062106, 0.39603960396039606]]]

accNgram = [[[0.85, 0.08, 0.07], [0.39, 0.57, 0.04], [0.12, 0.08, 0.8]],
            [[0.34, 0.32, 0.34], [0.32, 0.34, 0.34], [0.33, 0.33, 0.34]],
            [[0.33, 0.33, 0.34], [0.34, 0.34, 0.33], [0.32, 0.34, 0.34]],
            [[0.33, 0.33, 0.34], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]]]

accRNN = [[[0.38, 0.47, 0.15], [0.08, 0.88, 0.05], [0.22, 0.45, 0.33]],
          [[0.2, 0.64, 0.15], [0.11, 0.79, 0.09], [0.19, 0.65, 0.16]],
          [[0.23, 0.54, 0.23], [0.19, 0.55, 0.26], [0.21, 0.55, 0.24]],
          [[0.1633187772925764, 0.30480349344978164, 0.5318777292576419], [0.11233967271118973, 0.33171163202122955, 0.5559486952675807], [0.1548154815481548, 0.30423042304230424, 0.540954095409541]]]

accWord = [[[0.77, 0.15, 0.08], [0.05, 0.92, 0.03], [0.11, 0.14, 0.74]],
           [[0.74, 0.11, 0.14], [0.06, 0.88, 0.06], [0.14, 0.12, 0.74]],
           [[0.83, 0.07, 0.1], [0.09, 0.87, 0.04], [0.18, 0.11, 0.71]],
           [[0.8748180494905385, 0.08224163027656478, 0.04294032023289665], [0.056133056133056136, 0.9203049203049203, 0.02356202356202356], [0.13671274961597543, 0.0890937019969278, 0.7741935483870968]]]

counts = [2290, 2261, 1111]

names = ["CNLM", "N-Grams", "RNN CNLM", "Word LSTM"]
accs = [accLSTM, accNgram, accRNN, accWord]
colors = ["blue", "orange", "green", "red"]

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import numpy as np

matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20) 

from math import sqrt

for name, acc, color in zip(names, accs, colors):
 ys = [sum([x[gender][gender] for gender in range(3)])/3 for x in acc]
 plt.plot(range(0, 4), ys, label=name, linewidth=4.0, color=color)
 se = [None for _ in acc]
 for i in range(len(acc)):
     se[i] = 2*sqrt(ys[i]*(1-ys[i])/(sum(counts)))
 print(se)
 plt.errorbar(x=range(0,4), y=ys, yerr=se, linewidth=4.0, color=color)
plt.xticks(range(0,4))
plt.show()
plt.savefig("german-gender-total-se.pdf", bbox_inches='tight')
plt.close()
  
