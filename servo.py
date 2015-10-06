import Adafruit_BBIO.PWM as PWM
import time

class Servo:
	
	def __init__(self, porta):
		self._pin = porta
		self._started = True
		PWM.start(porta, 2, 50)
		

	def change_angle(self, angulo):
		PWM.set_duty_cycle(self._pin, ((angulo / 18) + 2))
		
	def stop(self):
		self._started = False
		PWM.stop(self._pin)
		PWM.cleanup()
		

	def start(self, angulo):
		self._started = True
		PWM.start(self._pin, ((angulo / 18) + 2), 50)

