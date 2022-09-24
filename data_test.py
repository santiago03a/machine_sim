
#Las entrdas para pruebas es una tupla de duplas
# El primer elemento de la dupla es el indice del GP
# El segundo elemento de la dupla es el respectivo valor
 
input_test_data=(
(10,1),
(11,0),
(12,0),
(13,0),
(14,0),
(10,0),
(11,0),
(12,0),
(13,0),
(14,0),
(10,0),
(11,1),
(12,0),
(13,0),
(14,0),
(10,0),
(11,1),
(12,0),
(13,0),
(14,0),
(10,0),
(11,1),
(12,1),
(13,0),
(14,0),
(10,0),
(11,1),
(12,1),
(13,0),
(14,0),
(10,0),
(11,1),
(12,0),
(13,0),
(14,0),
(10,0),
(11,1),
(12,0),
(13,0),
(14,0),
(10,0),
(11,0),
(12,0),
(13,0),
(14,0),
(10,1),
(11,0),
(12,0),
(13,0),
(14,0),
(10,1),
(11,0),
(12,0),
(13,0),
(14,0),
)

input_cont=0

def input_test(gp_req):
	global input_cont
	gp_test, val_test = input_test_data[input_cont]
	#print(gp_test, val_test,input_cont)
	if gp_test != gp_req:
		raise  Exception(f'The required GP {gp_req} is different from the test GP {gp_test}')
	input_cont += 1
	if len(input_test_data)<=input_cont:
		raise  Exception(f'No more test data')
	return val_test
