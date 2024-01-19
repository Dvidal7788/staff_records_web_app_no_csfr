x = 0

l = ['HI', 'BYE']

def func():
    # global x
    # x = 7000
    return x + 1

def func2():
    l.append('Good Evening')


def main():


    print(func())
    print(x)

    func2()

    print(l)


if __name__ == "__main__":
    main()