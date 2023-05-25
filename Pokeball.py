import unittest

class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion

    def __str__(self):
        return f"La pokeball {self.nombre} pesa {self.peso} gramos y cuesta {self.precio} pesos"
    
class ListaPokeball:
     
    def __init__(self):
        self.head = None
    
    def insertar(self, pokeball):
        new_node = Nodo(pokeball)
        if self.head is None:
            self.head = new_node
        elif self.head.data.fecha_fabricacion > pokeball.fecha_fabricacion:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data.fecha_fabricacion < pokeball.fecha_fabricacion:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def modificar(self, pokeball, caracteristica, valor):
        current = self.head
        while current and current.data.nombre != pokeball.nombre:
            current = current.next
        if current:
            if caracteristica == "peso":
                current.data.peso = valor
            elif caracteristica == "nombre":
                current.data.nombre = valor
            elif caracteristica == "precio":
                current.data.precio = valor
            elif caracteristica == "fecha_fabricacion":
                current.data.fecha_fabricacion = valor
            else:
                print("Caracteristica no encontrada")
        else:
            print("pokeball no encontrado")


        


class TestPokeball(unittest.TestCase):
    def setUp(self):
        # Crear un numero arbitrario de pokeballs
        self.pokeball1 = Pokeball(100, "pokeball1", 1000, "01/01/2020")
        self.pokeball2 = Pokeball(200, "pokeball2", 2000, "02/02/2020")
        self.pokeball3 = Pokeball(300, "pokeball3", 3000, "03/03/2020")

    def test_pokeball(self):
        self.assertEqual(self.pokeball1.peso, 100)
        self.assertEqual(self.pokeball1.nombre, "pokeball1")
        self.assertEqual(self.pokeball1.precio, 1000)
        self.assertEqual(self.pokeball1.fecha_fabricacion, "01/01/2020")
        self.assertEqual(self.pokeball2.peso, 200)
        self.assertEqual(self.pokeball2.nombre, "pokeball2")
        self.assertEqual(self.pokeball2.precio, 2000)
        self.assertEqual(self.pokeball2.fecha_fabricacion, "02/02/2020")
        self.assertEqual(self.pokeball3.peso, 300)
        self.assertEqual(self.pokeball3.nombre, "pokeball3")
        self.assertEqual(self.pokeball3.precio, 3000)
        self.assertEqual(self.pokeball3.fecha_fabricacion, "03/03/2020")
    
    # comprobar que el metodo __str__ funciona correctamente
    def test_str(self):
        self.assertEqual(str(self.pokeball1), "La pokeball pokeball1 pesa 100 gramos y cuesta 1000 pesos")
        self.assertEqual(str(self.pokeball2), "La pokeball pokeball2 pesa 200 gramos y cuesta 2000 pesos")
        self.assertEqual(str(self.pokeball3), "La pokeball pokeball3 pesa 300 gramos y cuesta 3000 pesos")

    
if __name__ == "__main__":
    unittest.main()