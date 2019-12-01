from src.plantToCode.interface import Interface
from dataToCode.methodToCode import MethodToCode


class InterfaceToCode:
    @staticmethod
    def convert(interface: Interface) -> str:
        method_to_code = MethodToCode(interface.methods)

        interfaces_code = InterfaceToCode.codeImplementedInterfaces(interface.interfaces)
        return (f"{interface.visibility.name} interface {interface.name}"
                f"{interfaces_code} {{\n"
                f"{method_to_code.get_formatted_methods()}\n"
                f"}}")

    @staticmethod
    def codeImplementedInterfaces(interfaces_list: [Interface]) -> str:
        if len(interfaces_list) > 0:
            interfaces_names = [x.name for x in interfaces_list]
            interfaces_string = ", ".join(interfaces_names)
            result = f" implements {interfaces_string}"
        else:
            result = ""
        return result
