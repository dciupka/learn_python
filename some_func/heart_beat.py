import matplotlib.pyplot as plt

heart_rythm = [62, 60,62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
print(heart_rythm)
heart_rythm = heart_rythm[1:-2] * 10
print(heart_rythm)

plt.plot(heart_rythm)
plt.show()
