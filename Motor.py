import Adafruit_BBIO.PWM as PWM
import time

class Motor:

	def __init__(self, porta1, porta2):
		self._pin = [porta1, porta2]
		PWM.cleanup()
		PWM.start(porta1, 10, 100)
		PWM.start(porta2, 10, 100)

	def change_speed(self, velocidade, porta):
		PWM.set_duty_cycle(self._pin[porta], velocidade)

	def stop(self, porta):
		PWM.stop(self._pin[porta])

	def start(self, velocidade, porta):
		PWM.start(self._pin[porta], velocidade)
