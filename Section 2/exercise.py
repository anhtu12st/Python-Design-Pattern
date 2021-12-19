from unittest import TestCase


class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return "self.%s = %s" % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ["class %s:" % self.name]
        if not self.fields:
            lines.append("  pass")
        else:
            lines.append("  def __init__(self):")
            for f in self.fields:
                lines.append("    %s" % f)
        return "\n".join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


class Evaluate(TestCase):
    @staticmethod
    def preprocess(s=""):
        return s.strip().replace("\r\n", "\n")

    def test_empty(self):
        cb = CodeBuilder("Foo")
        self.assertEqual(self.preprocess(str(cb)), "class Foo:\n  pass")

    def test_person(self):
        cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        self.assertEqual(
            self.preprocess(str(cb)),
            """class Person:
  def __init__(self):
    self.name = \"\"
    self.age = 0""",
        )


# My Answer:
# class Code:
#     def __init__(self, name):
#         self.name = name
#         self.attr = []

#     def __str__(self):
#         lines = []
#         lines.append("class {}:".format(self.name))
#         if len(self.attr) == 0:
#             lines.append("  pass")
#             return '\n'.join(lines)
#         lines.append("  def __init__(self):")
#         for a in self.attr:
#             lines.append("    self.{} = {}".format(a[0], a[1]))
#         return '\n'.join(lines)


# class CodeBuilder:
#     def __init__(self, root_name):
#         self.code = Code(root_name)

#     def add_field(self, type, name):
#         self.code.attr.append((type, name))
#         return self

#     def clear(self):
#         self.code = Code(self.code.name)

#     def __str__(self):
#         return str(self.code)
