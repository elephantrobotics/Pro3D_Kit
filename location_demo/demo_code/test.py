from pymycobot import ElephantRobot
import time
robot_ip="192.168.1.159"
er=ElephantRobot(robot_ip,5001)
er.start_client()

if er.state_check()==False:
    er.start_robot()
    

er.write_angles([0,-90,0,-90,0,0],1500)
time.sleep(5)

er.set_digital_out(0,1)
time.sleep(2)
er.set_digital_out(0,0)