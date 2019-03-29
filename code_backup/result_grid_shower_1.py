import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
w=10
h=10
fig =plt.figure(figsize=(8, 8))
columns = 16
rows = 16
for i in range(1,columns*rows+1):
#     img = open("name")
    
#     img = np.random.randint(10,size=(h,w))
    img_id = str(i-1)
#     img = mpimg.imread("d_dataset/number_1.png")
#     img = mpimg.imread("t_dataset/number_"+img_id+".png")
#     img = mpimg.imread("d_dataset_overall/number_"+img_id+".png")
#     img = mpimg.imread("t_dataset_overall/number_"+img_id+".png")
    img = mpimg.imread("encod_image/number_"+img_id+".png")
    
#     img.axes.get_xaxis().set_visible(False)
#     img.axes.get_yaxis().set_visible(False)
    
    fig.add_subplot(rows,columns,i)
    plt.imshow(img)
    plt.axis("off")
plt.savefig("grid_plate/grid_plate_16x16.png")
# plt.savefig("t_dataset_overall/t_dataset_overall5x5.png")
plt.show()




