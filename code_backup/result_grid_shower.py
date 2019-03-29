import matplotlib.pyplot as plt

import numpy as np
w=10
h=10
fig =plt.figure(figsize=(8,8))
columns = 4
rows = 5
for i in range(1,columns*rows+1):
#     img = open("name")
    img = np.random.randint(10,size=(h,w))
    fig.add_subplot(rows,columns,i)
    plt.imshow(img)
plt.show()




