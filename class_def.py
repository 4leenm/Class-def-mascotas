class Mascota:
    def __init__(self, nombre, edad, energia=100):
        self.nombre = nombre
        self.edad = edad
        self.energia = energia

    def mostrar_info(self):
        print(f"\n==== MASCOTA ====")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Energía: {self.energia}")

    def jugar(self):
        self.energia -= 20

        if self.energia < 0:
            self.energia = 0
            
        print(f"\nTu mascota, {self.nombre}, está jugando.")

    def descansar(self):
        self.energia += 30

        if self.energia > 100:
            self.energia = 100

        print("\nTu mascota está descansando.")


try:
    nombre_mascota = input("Nombre: ")
    edad_mascota = int(input("Edad: "))

    m = Mascota(nombre_mascota, edad_mascota)

    m.mostrar_info()
    m.jugar()
    m.jugar()
    m.mostrar_info()
    m.descansar()
    m.mostrar_info()

except ValueError:
    print("Error: El valor no concuerda con el tipo requerido.")