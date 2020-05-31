import unittest
from personService import PersonService
from person import Person
from parameterized import parameterized
from repository import Repository


class TestPersonService(unittest.TestCase):
    @parameterized.expand([
        ("Mariano", "Saez", 20, 0),
        ("Esteban", "Vargas", 23, 1),
        ("Bruno", "Bonil", 19, 2),
        ("Laura", "Paez", 39, 3),
        ("Jesse", "Ponkman", 23, 4)
    ])
    def testA_AddPerson(self, name, surname, age, key):
        p1 = Person(name, surname, age)
        service = PersonService()
        service.add_person(p1)
        self.assertEqual(Repository.person[key], p1.__dict__)

    # Dado que se comparte el repositorio, no es necesaria
    # la carga de nuevos ejemplos. Es posible utilizar los
    # añadidos en el test anterior (Que siempre se ejecutara
    # antes que testUpdatePerson())
    @parameterized.expand([
        (0, ),
        (1, ),
        (2, )
    ])
    def testBI_UpdatePersonName(self, key):
        service = PersonService()
        service.update_person(key, 1, "PruebaName")
        self.assertEqual(Repository.person[key]['_name'], "PRUEBANAME")

    @parameterized.expand([
        (0, ),
        (1, ),
        (2, )
    ])
    def testBII_UpdateSurname(self, key):
        service = PersonService()
        service.update_person(key, 2, "PruebaSurname")
        self.assertEqual(Repository.person[key]['_surname'], "PRUEBASURNAME")

    @parameterized.expand([
        (0, ),
        (1, ),
        (2, )
    ])
    def testBIII_UpdatePersonAge(self, key):
        service = PersonService()
        service.update_person(key, 3, 12)
        self.assertEqual(Repository.person[key]['_age'], 12)

    @parameterized.expand([
        (0, ),
        (2, ),
        (3, )
    ])
    def testC_DeletePerson(self, key):
        service = PersonService()
        service.delete_person(key, False)
        listKeys = Repository.person.keys()
        self.assertIsNot(listKeys, key)

    @parameterized.expand([
        ("Ronnie", "Coleman", 50, 5),
        ("Jo", "Lidnder", 39, 6)
    ])
    def testD_AddAfterDeletion(self, name, surname, age, key):
        p1 = Person(name, surname, age)
        service = PersonService()
        service.add_person(p1)
        self.assertEqual(Repository.person[key], p1.__dict__)


if __name__ == "__main__":
    unittest.main()
