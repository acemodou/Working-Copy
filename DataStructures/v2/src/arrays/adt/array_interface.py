from abc import ABC, abstractmethod

class ArrayInterface(ABC):
    
    @abstractmethod
    def append_element(self, value):
        """Add an element to the end of an array"""
        pass
    
    @abstractmethod
    def insert_element(self, index, value):
        """Add an element to the specified index """
        pass 
    
    @abstractmethod
    def delete_element(self, index):
        """Delete an element from the specified index """
        pass 
    
    @abstractmethod
    def search(self, value):
        """Search a value from a specified index """
        pass 
    
    @abstractmethod
    def display(self):
        """Display values in our list """
        pass 