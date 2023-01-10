from doubly_ll_operations import DoubleLinkedList
def test_head(doubly_linked_list):
    print('Testing if we have a head ...')
    assert doubly_linked_list.head.data == 'A' 

def test_prepend(doubly_linked_list):
    print('Testing prepend module ...')
    assert doubly_linked_list.prepend('E') == 'E'

def test_display(doubly_linked_list):
    print('Testing stdout ')
    assert doubly_linked_list.display() == "None-->A-->B-->C-->D-->None"

def test_insert(doubly_linked_list):
    print('Testing insert at any position ...')
    assert doubly_linked_list.insert('E', 2) == "None-->A-->B-->E-->C-->D-->None"

def test_append(doubly_linked_list):
    print('Testing prepend module ...')
    assert doubly_linked_list.append('E') == 'E'

def test_add_after_node(doubly_linked_list):
    print('Testing adding after a node ... ')
    assert doubly_linked_list.add_after_node('C', 1) == "None-->A-->B-->C-->1-->D-->None"
    assert doubly_linked_list.add_after_node('D', 'E') == "None-->A-->B-->C-->1-->D-->E-->None"

def test_add_before_node(doubly_linked_list):
    print('Testing adding after a node ... ')
    assert doubly_linked_list.add_before_node('C', 1) == "None-->A-->B-->1-->C-->D-->None"
    assert doubly_linked_list.add_before_node('D', 'E') == "None-->A-->B-->1-->C-->E-->D-->None"

def test_delete(doubly_linked_list):
    print('Testing deleting a node ...')
    assert doubly_linked_list.delete('A') == "None-->B-->C-->D-->None"
    assert doubly_linked_list.delete('Z') == "None-->B-->C-->D-->None" # Deleting a node that doesn't exist
    assert doubly_linked_list.delete('B') == "None-->C-->D-->None"
    assert doubly_linked_list.delete('D') == "None-->C-->None"
    assert doubly_linked_list.delete('C') == "None-->None"

def test_delete_at_index(doubly_linked_list):
    print('Testing deleting a node at any index ...')
    # assert doubly_linked_list.delete_at_index(0) == "None-->B-->C-->D-->None"
    assert doubly_linked_list.delete_at_index(1) == "None-->B-->C-->D-->None" 
    assert doubly_linked_list.delete_at_index(3) == "None-->B-->C-->None"
    # assert doubly_linked_list.delete_at_index('D') == "None-->C-->None"
    # assert doubly_linked_list.delete_at_index('C') == "None-->None"

def test_reverse(doubly_linked_list):
    print('Testing reversing a linked list ...')
    assert doubly_linked_list.reverse() == "None-->D-->C-->B-->A-->None"

def test_remove_dup(doubly_linked_list):
    print('Removing duplicates in our linked list ... ')
    doubly_linked_list.append('A')
    doubly_linked_list.append('B')
    doubly_linked_list.append('A')
    assert doubly_linked_list.remove_dup() == "None-->A-->B-->C-->D-->None"

def test_pairs_with_sum():
    print('Testing pairs that sum up to a value ...')
    dllist = DoubleLinkedList()
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.append(5)
    assert dllist.pairs_with_sum(5) == ['1, 4', '2, 3']

def test_convert_array_to_linked_list(doubly_linked_list):
    print('Convert and array to a doubly linked list ...')
    A = [10 , 20, 30, 40, 50]
    assert doubly_linked_list.convert_array_to_linked_list(A) == 'None-->10-->20-->30-->40-->50-->None'
   