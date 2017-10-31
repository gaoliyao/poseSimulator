import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def draw():
    rect_file = np.loadtxt('data/outputData.txt')
    shape = rect_file.shape

    FRAME_LENGTH = 50
    PEOPLE_NUM = int(shape[1] / 4)

    im = np.zeros((1080, 1980))

    fig, ax = plt.subplots(1)

    ax.imshow(im)

# rect = patches.Rectangle((50.83, 100), 300, 500, linewidth=1, edgecolor='r', facecolor='none')

# ax.add_patch(rect)

# show the initial frame
# rect_data = rect_file[0,:].reshape(3,4)
# for i in range(PEOPLE_NUM):
# 	x = rect_data[i, 0]
# 	y = rect_data[i, 1]
# 	w = rect_data[i, 2] - x
# 	h = rect_data[i, 3] - y
# 	rect = patches.Rectangle((x, y), w, h, linewidth = 1, edgecolor = 'r', facecolor = 'none')
# 	ax.add_patch(rect)

# plt.show()

    for frameIdx in range(FRAME_LENGTH):
        rect_data = rect_file[frameIdx, :].reshape(PEOPLE_NUM, 4)
        for i in range(PEOPLE_NUM):
            x = rect_data[i, 0]
            y = rect_data[i, 1]
            w = rect_data[i, 2] - x
            h = rect_data[i, 3] - y
            if frameIdx == 0:
                rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
            else:
                rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(rect)

    plt.show()
