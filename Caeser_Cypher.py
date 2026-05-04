alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
encoded = []


def caesercypher(shift, words):
    words = words.lower()
    wordslist = list(words)
    for i in range(len(wordslist)):
        if wordslist[i] not in alpha:
            encoded.append(wordslist[i])
        else:
            z = alpha.index(wordslist[i])  # sets the start number to the letter of the word
            for k in range(shift):
                z += 1  # Shifting it over repeatedly
                if z == 26:
                    z = 0  # sets it back to 0 once it hits 26
            encoded.append(alpha[z])


def uncaesercypher(shift, words):
    words = words.lower()
    wordslist = list(words)
    for i in range(len(wordslist)):
        if wordslist[i] not in alpha:
            encoded.append(wordslist[i])
        else:
            z = alpha.index(wordslist[i])
            for k in range(shift):
                z -= 1  # same as the first function but just subtracting
                if z == 0:
                    z = 26
            encoded.append(alpha[z])


choice = int(input("choose option 1 to encode and 2 to decode\n"))
if choice == 1:
    try:
        words = input("select a word to encode\n")
        shift = int(input("how much should it be shifted by?\n"))
    except ValueError:
        print("please input the correct things")
    caesercypher(shift, words)
    g = "".join(encoded)
    print(g)
else:
    decode = input("what do you want to decode?\n")
    shift = int(input("how much was it shifted by?\n"))
    uncaesercypher(shift, decode)
    g = "".join(encoded)
    print(g)
