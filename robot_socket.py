import servo
import Motor
#import camera_CV as camera
import socket
import time
import simplejson
import Adafruit_BBIO.PWM as PWM

#cam = camera.Camera()
#PWM.start("P8_13", 50, 100)
PWM.start("P9_14", 50, 100)
PWM.start("P9_42", 0, 100)
PWM.start("P9_21", 2, 50)
PWM.start("P9_28", 2, 50)


#cam.set_Address()
#cam.set_Cam()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('172.18.131.50', 5506 ))
cam_angle = [0.0, 0.0]

def robot_direction(direction, speed):

	if(direction == 2):
		#PWM.set_duty_cycle("P8_13", speed)
		PWM.set_duty_cycle("P9_14", 0)
		PWM.set_duty_cycle("P9_42", 0)

	elif(direction == 3):
                #PWM.set_duty_cycle("P8_13", 0)
                PWM.set_duty_cycle("P9_14", speed)
                PWM.set_duty_cycle("P9_42", 0)

	elif(direction == 0):
                #PWM.set_duty_cycle("P8_13", speed)
                PWM.set_duty_cycle("P9_14", speed)
                PWM.set_duty_cycle("P9_42", 0)

	elif(direction == 1):
                #PWM.set_duty_cycle("P8_13", 0)
                PWM.set_duty_cycle("P9_14", 0)
                PWM.set_duty_cycle("P9_42", speed)


	else:
                #PWM.set_duty_cycle("P8_13", 0)
                PWM.set_duty_cycle("P9_14", 0)
                PWM.set_duty_cycle("P9_42", 0)
		pass

def cam_direction(direction):
	
	if(direction == 2 ):
		
		if(cam_angle[0] >= 2):
			cam_angle[0] = cam_angle[0] - 1
                        duty_cycle = (cam_angle[0] / 18) + 2
                        PWM.set_duty_cycle("P9_21", duty_cycle)

        elif(direction == 3):
		if(cam_angle[0] <= 179):
                        cam_angle[0] = cam_angle[0] + 1
                        duty_cycle = (cam_angle[0] / 18) + 2
                        PWM.set_duty_cycle("P9_21", duty_cycle)

        elif(direction == 0):
		if(cam_angle[1] <= 179):
			cam_angle[1] = cam_angle[1] + 1
			duty_cycle = (cam_angle[1] / 18) + 2
			#PWM.stop("P9_21")
			#PWM.start("P9_22", duty_cycle, 50)
                       	PWM.set_duty_cycle("P9_28", duty_cycle)

	elif(direction == 1):
        	if(cam_angle[1] >= 2):
			cam_angle[1] = cam_angle[1] - 1
                	duty_cycle = (cam_angle[1] / 18) + 2
			#PWM.stop("P9_21")
                        #PWM.start("P9_22", duty_cycle, 50)
                        PWM.set_duty_cycle("P9_28", duty_cycle)	

while True:

	#cam.send_File()
	data, addr = sock.recvfrom(1024)
        info = simplejson.loads(data)
	print(info)
	robot_direction(info[0], info[2])
	cam_direction(info[1])
