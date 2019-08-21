from SimpleCalculator import Calculator

calculator_instance = Calculator()

def test_addition():
    assert calculator_instance.addition(3,3) == 6
    assert calculator_instance.addition(3, 3,3) == 9
    assert calculator_instance.addition(3, 3,3,3) == 12


def test_multiplyy():
    assert calculator_instance.multiply(3,3) == 9
    assert calculator_instance.multiply(3,2,3) == 18
    assert calculator_instance.multiply(3,5,9,7) == 945

def test_remember_the_last():
    assert calculator_instance.addition(2,2,2) == 6
    assert calculator_instance.last() == 6

    assert calculator_instance.multiply(2,6,2) == 24
    assert calculator_instance.last() == 24

def test_using_last_as_string_param():
    assert calculator_instance.addition(2,2,2) == 6
    assert calculator_instance.last() == 6
    assert calculator_instance.addition("LAST",5) == 11

    assert calculator_instance.multiply(2,2,2) == 8
    assert calculator_instance.last() == 8
    assert calculator_instance.multiply("LAST",5) == 40

def test_memory_slots():
    assert calculator_instance.addition(1,2) == 3
    assert calculator_instance.set_slot(1) == 'Set'
    assert calculator_instance.get_slot(1) == 3
    assert calculator_instance.addition(10,20) == 30
    assert calculator_instance.set_slot(2) == 'Set'
    assert calculator_instance.get_slot(2) == 30 
    assert calculator_instance.addition(100,200) == 300 
    assert calculator_instance.get_slot(1) == 3 
    assert calculator_instance.get_slot(2) == 30 
    assert calculator_instance.last() == 300

def test_memory_and_last_as_args():
    assert calculator_instance.addition(1,2) == 3
    assert calculator_instance.set_slot(1) == 'Set' 
    assert calculator_instance.addition("LAST",10) == 13
    assert calculator_instance.addition("SLOT_1",5) == 8
    assert calculator_instance.addition("SLOT_1",'LAST') == 11