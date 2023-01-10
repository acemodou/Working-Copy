class inclusive_range:
    def __init__(self, *args):
        num_args = len(args)
        self._start = 0
        self._step = 1

        if num_args < 1:
            raise TypeError(f'expected at least 1 argument, got {num_args}')
        elif num_args == 1:
            self._stop = args[0]
        elif num_args == 2:
            (self._start, self._stop) = args
        elif num_args == 3:
            (self._start, self._stop, self._step) = args
        else:TypeError(f'expected at most 3 arguments, got {num_args}')
        self._next = self._start 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
        return _r    
def main():
    for n in inclusive_range(5, 10):
        print(n, end=' ')
    print()

if __name__ == '__main__': main()