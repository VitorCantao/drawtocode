import pytest
from src.plantToCode.dataToCode.ToJava.methodToJava import MethodToJava
from src.plantToCode.method import Method
from src.plantToCode.visibility import Visibility
from src.plantToCode.attribute import Attribute
from src.plantToCode.modifier import Modifier
from typing import List


def test_formatted_method():
    method = Method("example")
    method_to_java = MethodToJava([method])
    assert method_to_java.get_formatted_methods() == "\tpublic void example();"

def test_formatted_methods():
    method1 = Method("example")
    method2 = Method("example2")
    method_to_java = MethodToJava([method1, method2])
    assert method_to_java.get_formatted_methods() == (f"\tpublic void example();"
                                                     f"\n\n\tpublic void"
                                                     f" example2();")

visibility_data = [
    (Visibility.public, "\tpublic void example();"),
    (Visibility.private, "\tprivate void example();"),
    (Visibility.package, "\tpackage void example();"),
    (Visibility.protected, "\tprotected void example();"), 
]
@pytest.mark.parametrize("visibility, expected", visibility_data)
def test_formatted_method_visibility(visibility, expected):
    method = Method("example", visibility=visibility)
    method_to_java = MethodToJava([method])
    assert method_to_java.get_formatted_methods() == expected


type_data = [
    ("int", "\tpublic int example();"),
    ("float", "\tpublic float example();"),
]
@pytest.mark.parametrize("type_name, expected", type_data)
def test_formatted_method_type(type_name, expected):
    method = Method("example", return_type=type_name)
    method_to_java = MethodToJava([method])
    assert method_to_java.get_formatted_methods() == expected
    

parameter_data = [
    ([["a", "int"]], "\tpublic void example(int a);"),
    ([["a", "int"], ["b", "float"]], "\tpublic void example(int a, float b);"),
]
@pytest.mark.parametrize("parameters, expected", parameter_data)
def test_formatted_method_parameters(parameters, expected):
    parameter_list: List[Attribute] = []
    for parameter in parameters:
        name, return_type = parameter
        new_parameter = Attribute(name, return_type)
        parameter_list.append(new_parameter)

    method = Method("example", parameters=parameter_list)
    method_to_java = MethodToJava([method])
    assert method_to_java.get_formatted_methods() == expected

