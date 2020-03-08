import multiprocessing

def sender(conn, msg):
    """
    Function to send messages to other end of pipe
    """
    for message in msg:
        conn.send(message)
        print(F"Sent the following message: {message}")
    conn.close()


def receiver(conn):
    """
    Function to print the message receive from other end of pipe
    """
    while 1:
        msg = conn.recv()
        if 'END' in msg:
            break
        print(F"Receive the messages: {msg}")


if __name__ == "__main__":
    msgs = ["hello", "hey", "hru?", "END"]

    """
    Create a PIPE()
    """
    parent_conn, child_conn = multiprocessing.Pipe()

    """
    Creating new processes
    """
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn, ))


    """
    Starting process and waiting until process is finished
    """
    p1.start()
    p2.start()


    p1.join()
    p2.join()

    """
    Checking if processes are alive 
    """
    print(f"Is p1 alive ? {p1.is_alive()}")
    print(f"Is p2 alive ? {p2.is_alive()}")