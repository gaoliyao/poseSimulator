from random import randint

out = open("out.txt","w")
start_position = (0,0)
box_width_height = (10,10)
moving_speed = 10
gap = 1

# Write the first data
out.write("{} {} {} {} {}\n".format(0,start_position[0],start_position[1],box_width_height[0],box_width_height[1]))

# Generate horizontal moving box
loop_p = start_position
for i in range(1,10):
    moving_speed = randint(10,20)
    (tmp_x,tmp_y) = loop_p
    tmp_x += moving_speed + gap
    out.write("{} {} {} {} {}\n".format(i,tmp_x,tmp_y,box_width_height[0],box_width_height[1]))
    loop_p = (tmp_x,tmp_y)

# Generate vertical moving box
loop_p = start_position
for i in range(1,10):
    moving_speed = randint(10,20)
    (tmp_x,tmp_y) = loop_p
    tmp_y += moving_speed + gap
    out.write("{} {} {} {} {}\n".format(i,tmp_x,tmp_y,box_width_height[0],box_width_height[1]))
    loop_p = (tmp_x,tmp_y)

# Generate diagonal moving box
moving_speed = 14
loop_p = start_position
for i in range(1,10):
    moving_speed = randint(14,20)
    (tmp_x,tmp_y) = loop_p
    tmp_x += moving_speed + gap
    tmp_y += moving_speed + gap
    out.write("{} {} {} {} {}\n".format(i,tmp_x,tmp_y,box_width_height[0],box_width_height[1]))
    loop_p = (tmp_x,tmp_y)

out.close()
