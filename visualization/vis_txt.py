import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_xlim([0, 200])
ax2.set_ylim([0, 200])

txt = open("/data/out.txt")
for l in txt:
    arrs = l.split()
    print(arrs)
    ax2.add_patch(
        patches.Rectangle(
            (int(arrs[1]), int(arrs[2])),
            int(arrs[3]),
            int(arrs[4]),
            fill=False      # remove background
        )
    )
txt.close()

fig2.savefig('rect2.png')
