def try_generator(y: object) -> object:
    n = y
    n += 1
    print("Performed addition")
    yield n

    n *= 2
    print("Performed multiplication")
    yield n


result = try_generator(15)

print(type(result))
print(next(result))
print(next(result))
