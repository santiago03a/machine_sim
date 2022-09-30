from machine_sim import Pin
import time

led1 = Pin(21,Pin.OUT) 
led2 = Pin(20,Pin.OUT) 
led3 = Pin(19,Pin.OUT) 
led4 = Pin(18,Pin.OUT) 
led5 = Pin(17,Pin.OUT) 

button1 = Pin(10,Pin.IN,Pin.PULL_UP)
button2 = Pin(11,Pin.IN,Pin.PULL_UP)
button3 = Pin(12,Pin.IN,Pin.PULL_UP)
button4 = Pin(13,Pin.IN,Pin.PULL_UP)
button5 = Pin(14,Pin.IN,Pin.PULL_UP)

estado = 'S1'

def est_sig_sal(estado_actual,entrada):
  '''
  Esta función calcula el estado siguiente 
  y las salidas de una máquina de estados finitos
  a partir del estado actual y de las entradas
  '''

  # valor por defecto del estado siguiente
  estado_siguiente = estado_actual

  #Evalúa cada estado
  if estado_actual == 'S1':
    salida = [1,0,0,0,0]
    if entrada[0:2]==[0,1] :
      estado_siguiente = 'S2'  

  elif estado_actual == 'S2':
    salida = [0,1,0,0,0]
    if entrada[0:3] == [0,1,1]:
      estado_siguiente = 'S3'

  elif estado_actual == 'S3':
    salida = [0,0,1,0,0]
    if entrada[0:3] == [1,0,0] :
      estado_siguiente = 'S1'
      

  return estado_siguiente, salida



while True:    
  entrada = [button1.value(),button2.value(),button3.value(),button4.value(),button5.value()]
  print('Current state:'+estado,"Input:" +str(entrada),end=', ')
  
  estado, salida = est_sig_sal(estado,entrada)
  led1.value(salida[0])
  led2.value(salida[1])
  led3.value(salida[2])
  led4.value(salida[3])
  led5.value(salida[4])
  print("Output:" +str(salida),'Next state:'+estado)
  time.sleep(0.2)

# 
#         


