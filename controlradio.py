from radio import Radio
Pradio= Radio("Pioner")
desea_continuar=True
print(Pradio.marca)
print(Pradio.encendido)
print(Pradio.en_FM)
print(Pradio.volumen)
while desea_continuar:
	if Pradio.encendido:
		opc=int(input("1.Apagar\n2.Subir/Bajar Volumen\n3.Subir/Bajar Estacion\n4.Cambiar Emisora\n \n"))
		if opc==1:
			Pradio.encendido=False
		if opc==2:
			res=int(input("1.Subir volumen\n 2.Bajar volumen "))
			if res==1:
				Pradio.subir_volumen()
			if res==2:
				Pradio.baja_volumen()	
		if opc==3:
			vol=int(input("1.Subir estacion\n 2.Bajar estacion "))	
			if vol==1:
				Pradio.subir_estacion()
			if vol==2:
				Pradio.bajar_estacion()	
	else:
		opc=int(input("1.Encender:\n2.Salir:\n\n"))
		if opc==1:
			Pradio.encendido=True
		else:	
			desea_continuar=False	
print(Pradio.marca)
print(Pradio.encendido)
print(Pradio.en_FM)
print(Pradio.volumen)
print(Pradio.emisoraFM)
print(Pradio.emisoraAM)

		