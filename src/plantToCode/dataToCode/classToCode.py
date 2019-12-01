from src.plantToCode.classData import ClassData
from src.plantToCode.modifier import Modifier
from dataToCode.methodToCode import MethodToCode
from dataToCode.interfaceToCode import InterfaceToCode
from dataToCode.inheritanceToCode import InheritanceToCode


class ClassToCode:

    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        self.method_to_code = MethodToCode(self.class_data.methods)
        self.inheritance_to_code = InheritanceToCode(self.class_data.inheritances)

    def convert(self) -> str:
        return (f"{self.__formatted_class_header()}"
                f"{self.__formatted_fields()}\n\n"
                f"{self.method_to_code.get_formatted_methods()}\n"
                f"}}")

    def __formatted_class_header(self):
        return (f"{self.class_data.visibility.name} {self.class_data.modifier.value}"
                f"{'' if self.class_data.modifier is Modifier.none else ' '}"
                f"class {self.class_data.name}{self.inheritance_to_code.get_formatted()}"
                f"{InterfaceToCode.codeImplementedInterfaces(self.class_data.implementations)}"
                f" {{\n")

    def __formatted_fields(self):
        class_fields = [f"\t{fields.visibility.value} {fields.type_} {fields.name};"
                        for fields in self.class_data.fields]
        return '\n'.join(class_fields)