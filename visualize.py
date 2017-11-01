import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw():
	rect_file = np.loadtxt('/Users/mars/Desktop/PData/outputData.txt')
	shape = rect_file.shape

	FRAME_LENGTH = 50
	PEOPLE_NUM = int(shape[1] / 4) # Number of people in each frame.

	FRAME_SHOW = 1 # Which frame sequence you want to visualize? Change this if you want
	START_FRAME = (FRAME_SHOW-1) * FRAME_LENGTH
	END_FRAME = FRAME_SHOW * FRAME_LENGTH

	# get an empty image
	im = np.zeros((1080, 1980))
	fig, ax = plt.subplots(1)
	ax.imshow(im)

# rect = patches.Rectangle((50.83, 100), 300, 500, linewidth=1, edgecolor='r', facecolor='none')

# ax.add_patch(rect)

#show the initial frame
# rect_data = rect_file[0,:].reshape(3,4)
# for i in range(PEOPLE_NUM):
# 	x = rect_data[i, 0]
# 	y = rect_data[i, 1]
# 	w = rect_data[i, 2] - x
# 	h = rect_data[i, 3] - y
# 	rect = patches.Rectangle((x, y), w, h, linewidth = 1, edgecolor = 'r', facecolor = 'none')
# 	ax.add_patch(rect)

# plt.show()

# this plot the first 50 frames(FRAME_LENGTH = 50) in the label2.txt, if you want to see other data, change PEOPLE_NUM
	for frameIdx in range(START_FRAME, END_FRAME):
		rect_data = rect_file[frameIdx, :].reshape(PEOPLE_NUM, 4)
		for i in range(PEOPLE_NUM):
			x = rect_data[i, 0]
			y = rect_data[i, 1]
			w = rect_data[i, 2] - x
			h = rect_data[i, 3] - y
			if frameIdx == START_FRAME: # the first box of a person will be draw in RED
				rect = patches.Rectangle((x, y), w, h, linewidth = 1, edgecolor = 'r', facecolor = 'none')
			else: # other box will be in BLUE
				rect = patches.Rectangle((x, y), w, h, linewidth = 1, edgecolor = 'b', facecolor = 'none')
			ax.add_patch(rect)

	plt.show()