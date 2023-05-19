import matplotlib.pyplot as plt

x = [100, 500, 1000, 2500, 5000, 7500, 10000]
linear = [0.7017581462860107, 0.0010218620300292969, 0.004763126373291016,
          0.010970830917358398, 0.0248260498046875, 0.03210186958312988, 0.05390596389770508]
binary = [0.9513442516326904, 0.00011277198791503906, 0.00011491775512695312,
          0.00012922286987304688, 0.0001308917999267578, 0.00012373924255371094, 0.0003478527069091797]
multimap = [3.504753112792969, 2.09808349609375, 2.4080276489257812,
               2.3603439331054688, 2.574920654296875, 2.7894973754882812, 2.193450927734375]

plt.plot(x, linear, label ="linear", color ='#5451B6', linewidth = 1.5, marker ='.')
plt.plot(x, binary, label ="binary", color ='#5E8CB8', linewidth = 1.5, marker ='*')
plt.plot(x, multimap, label ="multimap", color ='#CE81AD', linewidth = 1.5, marker = '+')
plt.legend()
plt.show()
