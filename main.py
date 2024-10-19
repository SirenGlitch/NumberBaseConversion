baseIn = input("What base is your number? (Hex, Decimal, Binary) ").strip()
numIn = input("What number would you like to convert? ").strip()
baseOut = input("What base would you like to convert it into? (Hex, Decimal, Binary) ").strip()

if baseIn.lower().startswith("h"):  # Hex Conversions
    if baseOut.lower().startswith("d"):  # Hex to Decimal
        numOut = int(numIn, 16)

    elif baseOut.lower().startswith("b"):  # Hex to Binary
        tmp = int(numIn, 16)
        numOut = bin(tmp)[2:]
    else:
        print("Invalid Base")

elif baseIn.lower().startswith("d"):  # Decimal Conversions
    if baseOut.lower().startswith("h"):  # Decimal to Hex
        numOut = hex(int(numIn))[2:]

    elif baseOut.lower().startswith("b"):  # Decimal to Binary
        tmp = int(numIn, 10)
        numOut = bin(tmp)[2:]
    else:
        print("Invalid Base")

elif baseIn.lower().startswith("b"):  # Binary Conversions
    if baseOut.lower().startswith("h"):  # Binary to Hex
        tmp = int(numIn, 2)
        numOut = hex(tmp)[2:]

    elif baseOut.lower().startswith("d"):  # Binary to Decimal
        tmp = int(numIn, 2)
        numOut = str(tmp)
    else:
        print("Invalid Base")

print(numOut)
