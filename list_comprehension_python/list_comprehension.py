# IMPORTS #
# None

def run_list_comprehension():
    squares = [n**2 for n in range(10)]
    print(squares)

    squares = []
    for n in range(10):
        squares.append(n**2)
    print(squares)

if __name__ == "__main__":
    run_list_comprehension()