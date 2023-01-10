from stack_adt_linkedlist import STACKLIST

class Node:
    def __init__(self, value):
        self.lchild = None 
        self.value = value
        self.rchild = None 


def create_from_preorder(pre):
    # Create initial node 
    i = 0
    root = Node(pre[i])
    i += 1
    root.lchild = None 
    root.rchild = None 

    ptr = root
    st = STACKLIST()

    while i < len(pre):
        # left child case 
        if pre[i] < ptr.value:
            t = Node(pre[i])
            i += 1
            t.lchild = None 
            t.rchild = None 
            ptr.lchild = t 
            st.push(ptr)
            ptr = t
        else:
            # We don't push address when we create right child 
            # This is just a h
            # if pre[i] > ptr.value and pre[i] < st.top.value or st.isEmpty() and pre[i] < float("inf"):
            # stk_value = st.stackTop()
            # val = int(stk_value.value)
          

            if pre[i] > ptr.value and not st.isEmpty() and pre[i] < st.stackTop().value:
                t = Node(pre[i])
                i +=1
                t.lchild = None 
                t.rchild = None 
                ptr.rchild = t
                ptr = t
            elif st.isEmpty() and  pre[i] > ptr.value:
                t = Node(pre[i])
                i +=1
                t.lchild = None 
                t.rchild = None 
                ptr.rchild = t
                ptr = t
            else:
                ptr = st.stackTop()
                st.pop()
                
pre = [30,20,10,15,25,40,50,45]
create_from_preorder(pre)
