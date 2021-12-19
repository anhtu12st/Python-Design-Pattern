from unittest import TestCase

# My Answer:
# class Person:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# class PersonFactory:
#     list_id = []

#     def create_person(self, name):
#         id = len(self.list_id)
#         self.list_id.append(id)
#         return Person(id, name)


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person("Chris")
        self.assertEqual(p1.name, "Chris")
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person("Sarah")
        self.assertEqual(p2.id, 1)
