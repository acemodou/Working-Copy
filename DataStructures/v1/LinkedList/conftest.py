import pytest 
from singly_ll_operations import SinglyLinkedList
from circly_ll_operations import CircularLinkedList
from doubly_ll_operations import DoubleLinkedList
from circly_dll_operations import CircularDoubleLinkedList

@pytest.fixture()
def my_linked_list():
    print('Connecting to our Node structure ...')
    sllist = SinglyLinkedList()
   
    sllist.append(3)
    sllist.append(6)
    sllist.append(7)
    sllist.append(8)
    sllist.append(12)
    yield sllist

@pytest.fixture()
def circular_linked_list():
    print('Connecting to our Circular list ...')
    cllist = CircularLinkedList()
    cllist.append('A')
    cllist.append('B')
    cllist.append('C')
    cllist.append('D')
    return cllist

@pytest.fixture()
def doubly_linked_list():
    print('Connecting to our Circular list ...')
    dllist = DoubleLinkedList()
    dllist.append('A')
    dllist.append('B')
    dllist.append('C')
    dllist.append('D')
    yield dllist

@pytest.fixture()
def circular_doubly_linked_list():
    print('Connecting to our Circular list ...')
    dllist = CircularDoubleLinkedList()
    dllist.append('A')
    dllist.append('B')
    dllist.append('C')
    dllist.append('D')
    yield dllist