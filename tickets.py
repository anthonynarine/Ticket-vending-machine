def perfume_tickets():
    for num in range (1,10000):
        yield f"P - {num}"

       
def medicine_tickets():
    for num in range (1,10000):
        yield f"M - {num}"


def cosmetic_tickets():
    for num in range (1,10000):
        yield f"C - {num}"

p = perfume_tickets()
m = medicine_tickets()
c = cosmetic_tickets()


def decorator(product):
    print("\n" + "*" * 23)
    print ("Your number is: ")

    if product == "P":
        print(next(p))
    elif product == "M":
        print(next(m))
    else:
        print(next(c))
    print ("Please wait for your turn")
    print("*" * 23 +"\n")