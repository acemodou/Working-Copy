from singly_ll_operations import SinglyLinkedList

def test_head(my_linked_list):
    print('Testing if we have a head ...')
    assert my_linked_list.head.data == 3

def test_prepend(my_linked_list):
    print('Testing prepend module ...')
    assert my_linked_list.prepend(11) == 11

def test_insert(my_linked_list):
    print('Testing our insert module ... ')
    assert my_linked_list.insert(4, 10) == 10

def test_display(my_linked_list):
    print('Testing stdout ')
    assert my_linked_list.display() == "3-->6-->7-->8-->12-->None"

def test_recursive_display(my_linked_list):
    print('Testing stdout recursively')
    assert my_linked_list.recursive_display(my_linked_list.head) == None 

def test_get_length(my_linked_list):
    print('Testing our linked list size ... ')
    assert my_linked_list.get_length() == 5

def test_recursive_get_length(my_linked_list):
    print('Testing our length recursively ... ')
    assert my_linked_list.recursive_get_length(my_linked_list.head) == 5

def test_sum(my_linked_list):
    print('Testing our sum ... ')
    assert my_linked_list.sum() == 36

def test_recursive_sum(my_linked_list):
    print('Testing our sum recursively ... ')
    assert my_linked_list.recursive_sum(my_linked_list.head) == 36

def test_max_element(my_linked_list):
    print('Testing max element in a list ... ')
    assert my_linked_list.max() == 12

def test_max_element_recursively(my_linked_list):
    print('Testing max element in a list recursively ... ')
    assert my_linked_list.recursive_max(my_linked_list.head) == 12

def test_search_element_(my_linked_list):
    print('Searching for and element in our list ')
    assert my_linked_list.linear_search(12) == True 
    assert my_linked_list.linear_search(-3) == False 

def test_search_element_(my_linked_list):
    print('Searching for and element recursively ')
    assert my_linked_list.recursive_linear_search(my_linked_list.head, 12) == True 
    assert my_linked_list.recursive_linear_search(my_linked_list.head, -3) == False  

def test_improve_linear_search(my_linked_list):
    print('Improving linear search so that the next time we search what we are searching is up front')
    assert my_linked_list.improve_linear_search(8) == "8-->3-->6-->7-->12-->None"

def test_insert_sorted_list(my_linked_list):
    print('Inserting in a sorted list')
    assert my_linked_list.insert_in_sorted_list(2) == "2-->3-->6-->7-->8-->12-->None"
    assert my_linked_list.insert_in_sorted_list(11) == "2-->3-->6-->7-->8-->11-->12-->None"

def test_delete(my_linked_list):
    print('Deleting and element in a linked list ...')
    assert my_linked_list.delete(0) == 3

def test_is_sorted(my_linked_list):
    print('Checking if a list is sorted ... ')
    assert my_linked_list.is_sorted() == "Is sorted"

def test_remove_dup(my_linked_list):
    print('Testing removing duplicates in a list')
    my_linked_list.insert(2, 6)
    my_linked_list.insert(4, 8)
    assert my_linked_list.remove_dup() == "3-->6-->7-->8-->12-->None"

def test_reverse_elements(my_linked_list):
    print('Reverse a linked list using auxiliary array')
    assert my_linked_list.reverse_elements() == "12-->8-->7-->6-->3-->None"
    
def test_reverse_links(my_linked_list):
    print('Reverse a linked list with secondListiding pointers')
    assert my_linked_list.reverse_links() == "12-->8-->7-->6-->3-->None"
    
def test_recursive_reverse_links(my_linked_list):
    print('Recursive reverse linked linked using head recursion')
    my_linked_list.recursive_reverse_links(None, my_linked_list.head)
    assert my_linked_list.display() == "12-->8-->7-->6-->3-->None"
    
def test_concatenate(my_linked_list):
    print('Join two linked list together')
    secondList = SinglyLinkedList()
    secondList.append(2)
    secondList.append(4)
    secondList.append(9)
    secondList.append(11)
    secondList.append(15)
    assert my_linked_list.concatenate(secondList) == "3-->6-->7-->8-->12-->2-->4-->9-->11-->15-->None" 

def test_merge_sorted_lists(my_linked_list):
    print(''' Merge two sorted list together and return a final list ''')
    secondList = SinglyLinkedList()
    secondList.append(2)
    secondList.append(4)
    secondList.append(9)
    secondList.append(11)
    secondList.append(15)
    assert my_linked_list.merge_sorted_lists(secondList) == "2-->3-->4-->6-->7-->8-->9-->11-->12-->15-->None"
   



    
    