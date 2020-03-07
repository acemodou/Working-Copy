import multiprocessing


def insert_record(records, record):
    """
    Adding new record to a record list
    """
    records.update(record)
    print("New record added!\n")


def print_record(records):
    for key, value in records.items():
        print(f"Name: {key} \nScore: {value} \n")


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        """
        Creating a dictionary in server process memory
        """
        records = manager.dict({'Modou': 20, 'Aji': 10, 'Zakaria:': 99})

        """
        New record to be added
        """
        new_record = {"Aisha": 89}

        p1 = multiprocessing.Process(target=insert_record, args=(records, new_record))
        p2 = multiprocessing.Process(target=print_record, args=(records,))

        """
        Starting processes & wait until process finished 
        """
        p1.start()
        p1.join()


        """
        Starting processes & wait until process finished 
        """
        p2.start()
        p2.join()

        """
        Check if processes are alive 
        """
        print(f"Is p1 alive ?: {p1.is_alive()}")
        print(F"Is p2 alive ?: {p2.is_alive()}")



