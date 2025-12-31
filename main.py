def f(x):
    yield x + 12
    yield x + 24


def main():
    for n in f(12):
        print(n)
    print("Hello from base!")


if __name__ == "__main__":
    main()
