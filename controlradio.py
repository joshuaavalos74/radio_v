from radio import Radio
Pradio= Radio("Pioner")
desea_continuar=True
print(Pradio.marca)
print(Pradio.encendido)
print(Pradio.en_FM)
print(Pradio.volumen)
while desea_continuar:
	if Pradio.encendido:
		opc=input("1.Apagar\n2.Subir/Bajar Volumen\n3.Subir/Bajar Estacion\n4.Cambiar Emisora\n ")
		if opc==1:
			Pradio.encendido=False
		if opc==2:
			Pradio.volumen
		if opc==3:
			Pradio.en_FM		
	else:
		opc=input("1.Encender:\n2.Salir:")
		if opc==1:
			Pradio.encendido=True
		else:	
			desea_continuar=False	
		