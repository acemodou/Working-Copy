from singly_ll_operations import SinglyLinkedList

def test_head(circular_linked_list):
    print('Testing if we have a head ...')
    assert circular_linked_list.head.data == 'A' 

def test_prepend(circular_linked_list):
    print('Testing prepend module ...')
    assert circular_linked_list.prepend('E') == 'E'

def test_display(circular_linked_list):
    print('Testing stdout ')
    assert circular_linked_list.display() == "A-->B-->C-->D-->Head"

def test_recursive_display(circular_linked_list):
    print('Testing circular recursive stdout ')
    assert circular_linked_list.recursive_display(circular_linked_list.head) == "A-->B-->C-->D-->Head"

def test_append(circular_linked_list):
    print('Testing prepend module ...')
    assert circular_linked_list.append('E') == 'E'

def test_remove_node(circular_linked_list):
    print('Removing a node from a list ')
    assert circular_linked_list.remove('D') == "A-->B-->C-->Head"
    assert circular_linked_list.remove('A') == "B-->C-->Head"
    assert circular_linked_list.remove('C') == "B-->Head"
    assert circular_linked_list.remove('F') == "F is not in our list "

def test_split_list(circular_linked_list):
    print('Diving a list into two halves ... ')
    assert circular_linked_list.split_list() == ('A-->B-->Head', 'C-->D-->Head')

def test_josephus_problem(circular_linked_list):
    print('Checking the joesphus problem ')
    assert circular_linked_list.josephus(circular_linked_list.head, 2) == 'A-->Head'

def test_is_circular_list(circular_linked_list):
    print('Checking if a list is sequential or circular ... ')
    sllist = SinglyLinkedList()
    sllist.append('A')
    sllist.append('B')
    sllist.append('C')
    sllist.append('D')
    assert circular_linked_list.is_circular_list(circular_linked_list) == True 
    assert circular_linked_list.is_circular_list(sllist) == False

def test_is_loop(circular_linked_list):
    ''' Checking if we have a loop '''
    assert circular_linked_list.is_loop() == True 
   
