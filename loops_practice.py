class Loops:
    TARGET = 5
    def task1(self):
        numbers = list(range(1,8))
        for n in numbers:
            if n != Loops.TARGET:
                print(n)
            else:
                print(n)

    def task2(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word, sep=', ')



if __name__ == "__main__":
    pass