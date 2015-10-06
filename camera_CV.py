import cv2
import socket

class Camera():

	def __init__(self):
        	self._UDP_IP = None
    		self._UDP_PORT = None
    		self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    		self._camera = cv2.VideoCapture(0)

    	def set_Address(self, ip_address="172.18.131.137", port=5505):
        	self._UDP_IP = ip_address
        	self._UDP_PORT = port

	def send_File(self):
        	while(True):
    			# Captura uma imagem e grava no arquivo image.jpg.
    			ret, frame = self._camera.read()
    			cv2.imwrite('image.jpg', frame)

    			# Le o arquivo image.jpg e manda a informacao em pacotes de 1 K.
    			img = open('image.jpg', 'rb')
    			data = img.read(1024)

    			while (data):
        			self._sock.sendto(data, (self._UDP_IP, self._UDP_PORT))
        			data = img.read(1024)

    			# Avisa para o receptor que a transmissao da imagem foi finalizada.
    			data = 'end'
    			self._sock.sendto(data, (self._UDP_IP, self._UDP_PORT))
    			img.close()
