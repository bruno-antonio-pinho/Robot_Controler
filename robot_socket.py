import socket
import simplejson
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

# Inicia as portas PWM que controlam os motores.
PWM.start("P8_13", 0, 100)
PWM.start("P9_14", 0, 100)
PWM.start("P9_42", 0, 100)

# Inicia as portas PWM que controlam o suporte pan/tilt da camera.
PWM.start("P9_22", 2, 50)
PWM.start("P9_28", 2, 50)

# Inicia os saidas que contralam as passagem dos pulsos PWM do pan/tilt da camera.
GPIO.setup("P9_23",GPIO.OUT)
GPIO.setup("P9_30",GPIO.OUT)

# Coloca as portas P9_30 e P9_23 em nivel alto para bloquear a passagem do sinal PWM.
GPIO.output("P9_23", GPIO.HIGH)
GPIO.output("P9_30", GPIO.HIGH)


# Abre coneccao na porta 5506.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('172.18.131.50', 5506 ))

# Angulo inicial das cameras.
cam_angle = [0.0, 0.0]

def robot_direction(direction, speed):

	# Move o robo para a direita
	if(direction == 2):
		PWM.set_duty_cycle("P8_13", 0)
		PWM.set_duty_cycle("P9_14", speed)
		PWM.set_duty_cycle("P9_42", 0)

	# Move o robo para a esquerda.
	elif(direction == 3):
                PWM.set_duty_cycle("P8_13", speed)
                PWM.set_duty_cycle("P9_14", 0)
                PWM.set_duty_cycle("P9_42", 0)

	# Move o robo para frente.
	elif(direction == 0):
                PWM.set_duty_cycle("P8_13", speed)
                PWM.set_duty_cycle("P9_14", speed)
                PWM.set_duty_cycle("P9_42", 0)

	# Move o robo para tras.
	elif(direction == 1):
                PWM.set_duty_cycle("P8_13", 0)
                PWM.set_duty_cycle("P9_14", 0)
                PWM.set_duty_cycle("P9_42", speed)

	# Para os movimentos do robo;
	else:
                PWM.set_duty_cycle("P8_13", 0)
                PWM.set_duty_cycle("P9_14", 0)
                PWM.set_duty_cycle("P9_42", 0)
		pass

def cam_direction(direction):
	
	# Movimenta a camera para a direita.
	if(direction == 3 ):
		if(cam_angle[0] >= 2):
			cam_angle[0] = cam_angle[0] - 1
                        duty_cycle = (cam_angle[0] / 18) + 2
			GPIO.output("P9_23", GPIO.LOW)
                        PWM.set_duty_cycle("P9_21", duty_cycle)

	# Movimenta a camera para a esquerda.
        elif(direction == 2):
		if(cam_angle[0] <= 179):
                        cam_angle[0] = cam_angle[0] + 1
                        duty_cycle = (cam_angle[0] / 18) + 2
			GPIO.output("P9_23", GPIO.LOW)
                        PWM.set_duty_cycle("P9_21", duty_cycle)

	# Movimenta a camera para cima.
        elif(direction == 0):
		if(cam_angle[1] <= 179):
			cam_angle[1] = cam_angle[1] + 1
			duty_cycle = (cam_angle[1] / 18) + 2
			GPIO.output("P9_30", GPIO.LOW)
			PWM.set_duty_cycle("P9_28", duty_cycle)

	# Movimenta a camera para baixo.
	elif(direction == 1):
        	if(cam_angle[1] >= 2):
			cam_angle[1] = cam_angle[1] - 1
                	duty_cycle = (cam_angle[1] / 18) + 2
			GPIO.output("P9_30", GPIO.LOW)
                        PWM.set_duty_cycle("P9_28", duty_cycle)	

	# Para o movimento da camera.
	else:
		GPIO.output("P9_23", GPIO.HIGH)
		GPIO.output("P9_30", GPIO.HIGH)


while True:

	data, addr = sock.recvfrom(1024) # Espera o pacote com os comados.
        info = simplejson.loads(data) # Transforma a informacao do pacote em um vetor de inteir.
	print(info) # printa na tela o pacote recebido para Debug.
	robot_direction(info[0], info[2])
	cam_direction(info[1])
