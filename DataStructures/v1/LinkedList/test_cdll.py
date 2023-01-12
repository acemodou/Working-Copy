
def test_head(circular_doubly_linked_list):
    print('Testing if we have a head ...')
    assert circular_doubly_linked_list.head.data == 'A'

def test_display(circular_doubly_linked_list):
    print('Testing stdout ')
    assert circular_doubly_linked_list.display() == "None-->A-->B-->C-->D-->None"

def test_add_after_node(circular_doubly_linked_list):
    print('Testing adding after a node ... ')
    assert circular_doubly_linked_list.add_after_node('C', 1) == "None-->A-->B-->C-->1-->D-->None"
    # assert circular_doubly_linked_list.add_after_node('D', 'E') == "None-->A-->B-->C-->1-->D-->E-->None"

# def test_add_before_node(doubly_linked_list):
#     print('Testing adding after a node ... ')
#     assert doubly_linked_list.add_before_node('C', 1) == "None-->A-->B-->1-->C-->D-->None"
#     assert doubly_linked_list.add_before_node('D', 'E') == "None-->A-->B-->1-->C-->E-->D-->None"

