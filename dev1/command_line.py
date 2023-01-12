import sys, webbrowser



# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])
#     print(address)

# webbrowser.open(address)

fibonacci_cache = {}
def MemoizationFibonaaci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        return n
    elif n > 1:
        value = MemoizationFibonaaci(n-1) + MemoizationFibonaaci(n-2)
    
    # Cache the value and return it 
    fibonacci_cache[n] = value
    yield value

def run_main(parsed_args):
    if parsed_args.verbose:
        print(f'The {parsed_args.n} ":"fibonacci number is {MemoizationFibonaaci(parsed_args.n)}')
    elif parsed_args.n:
        return MemoizationFibonaaci(parsed_args.n)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Display the fibonacci of a number')
    parser.add_argument('n', default=None, type=int, help='Nth fibonacci number')
    parser.add_argument('-v', '--verbose', action='store_true')
    run_main(parsed_args=parser.parse_args())
    
