from program import Program
from queue import Queue

grid = {}
robot_pos = (0,0)
robot_dir = 0

inp_s = Queue()
out_s = Queue()
p = Program([], inp_s, out_s).run_from_file('input.txt')
while (p.is_alive()):
    inp_s.put(grid.get(robot_pos, 0))
    paint = out_s.get()
    dir = out_s.get()

    grid[robot_pos] = paint
    robot_dir += (-1 if (dir == 0) else 1)
    robot_dir %= 4

    if (robot_dir == 0):
        robot_pos = (robot_pos[0], robot_pos[1]-1)
    elif (robot_dir == 1):
        robot_pos = (robot_pos[0]+1, robot_pos[1])
    elif (robot_dir == 2):
        robot_pos = (robot_pos[0], robot_pos[1]+1)
    elif (robot_dir == 3):
        robot_pos = (robot_pos[0]-1, robot_pos[1])
    print(robot_pos)

    #count += 1
print(len(grid))
