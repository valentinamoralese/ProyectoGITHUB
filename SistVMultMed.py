from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 

    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
  
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
    
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
        self.__dic_felinos = {}
        self.__dic_caninos = {}
    
    # Defino método para eliminar medicamento
    def eliminarMedicamento(self, historia, nombre_medicamento):
        for masc in self.__lista_mascotas: #recorre la lista de mascotas buscando la historia clinica
            if historia == masc.verHistoria():
                lista = masc.verLista_Medicamentos() #se obtiene la lista de medicamentos de la mascota
                for med in lista:
                    if med.verNombre().lower() == nombre_medicamento.lower(): #comparo todo pasando a minuscula para evitar errores
                        lista.remove(med) #elimina el medicamento de la lista
                        print(f"Medicamento '{nombre_medicamento}' eliminado correctamente.") #mensaje de confirmación
                        return True
                print("El medicamento no fue encontrado.") #cuando se ingresa un medicamento que no está en la lista
                return False
        print("No existe una mascota con esa historia clínica.") #historia clinica invalida
        return False
      
      # Definí dos métodos para ver en un string ordenado, el contenido de cada paciente almacenado en el diccionario correspondiente

    def verFelinosHospitalizados(self):
      if not self.__dic_felinos:
        print("No hay felinos hospitalizados.")
        return
      print("Felinos hospitalizados:")
      for historia, mascota in self.__dic_felinos.items():
        print(f"- Historia: {historia}, Nombre: {mascota.verNombre()}, Tipo: {mascota.verTipo()}, Peso: {mascota.verPeso()}, Fecha de ingreso: {mascota.verFecha()}")


    def verCaninosHospitalizados(self):
      if not self.__dic_caninos:
        print("No hay caninos hospitalizados.")
        return
      print("Caninos hospitalizados:")
      for historia, mascota in self.__dic_caninos.items():
        print(f"- Historia: {historia}, Nombre: {mascota.verNombre()}, Tipo: {mascota.verTipo()}, Peso: {mascota.verPeso()}, Fecha de ingreso: {mascota.verFecha()}")

      #Definí dos métodos para agregar los felinos/ caninos al diccionario correspondiente
    def ingresarFelino(self,mascota):
        historia = mascota.verHistoria()
        self.__dic_felinos[historia] = mascota
        print("Felino agregado correctamente a la base de datos.")
        #print("Diccionario actual de felinos:", self.__dic_felinos)

    def ingresarCanino(self,mascota):
        historia = mascota.verHistoria()
        self.__dic_caninos[historia] = mascota
        print("Canino agregado correctamente a la base de datos.")
        #print("Diccionario actual de caninos:", self.__dic_caninos)

    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                if historia in self.__dic_felinos:
                  del self.__dic_felinos[historia] #Eliminar del diccionario
                elif historia in self.__dic_caninos:
                  del self.__dic_caninos[historia] #Eliminar del diccionario
                return True #Eliminado con exito
        return False



def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota
                       \n6- Eliminar medicamento de una mascota
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                while True:
                  tipo=input("Ingrese el tipo de mascota (felino o canino): ") #Creo un bucle para asegurarme de que se ingrese un tipo de mascota correcto
                  if tipo == "Felino" or tipo == "felino" or tipo == "Canino" or tipo == "canino":
                    peso=int(input("Ingrese el peso de la mascota: "))
                    while True:
                      fecha = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                      try:
                        datetime.strptime(fecha, "%d/%m/%Y")  # Intenta convertir la fecha al formato
                        break  # Si no hay error, sal del bucle
                      
                      except ValueError:
                        print("Formato de fecha incorrecto. Intenta de nuevo con el formato dd/mm/aaaa.")
                    nm=int(input("Ingrese cantidad de medicamentos: "))
                    lista_med=[]
                    Nmed= [] #Creo lista vacia para agregar los nombres de medicamento que el usuario ingrese
                    break

                  else:
                    print("Ingrese un tipo correcto (Felino o Canino)")

                for i in range(0,nm):
                    while True: #creo un bucle para que se repita la pregunta si el medicamento está repetido
                        nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                        
                        if nombre_medicamentos in Nmed:
                            print("Está repetido :c, intenta de nuevo") #vuelve  a preguntar hasta que ingrese un nuevo medicamento
                        else:
                            Nmed.append(nombre_medicamentos) #Agrego el nuevo medicamento a mi lista
                            dosis =int(input("Ingrese la dosis: "))
                            medicamento = Medicamento()
                            medicamento.asignarNombre(nombre_medicamentos)
                            medicamento.asignarDosis(dosis)
                            lista_med.append(medicamento)
                            break #Si el medicamento no está repetido, me salgo del bucle y continuo
                    
                       

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                if tipo == "felino" or tipo == "Felino":
                    servicio_hospitalario.ingresarFelino(mas)
                elif tipo == "Canino" or tipo == "canino":
                    servicio_hospitalario.ingresarCanino(mas)
                #servicio_hospitalario.verFelinosHospitalizados()
                #servicio_hospitalario.verCaninosHospitalizados()


            

                

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
                servicio_hospitalario.verFelinosHospitalizados()
                servicio_hospitalario.verCaninosHospitalizados()
                
            else:
                print("No se ha podido eliminar la mascota")
        elif menu==6: #añado nueva opcion al menú
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            nombre_medicamento = input("Ingrese el nombre del medicamento que desea eliminar: ")
            servicio_hospitalario.eliminarMedicamento(historia, nombre_medicamento) #aplico método

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()