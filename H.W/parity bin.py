def parity(string):
    par = 0
    for chr in string:
        if chr == "1":
            par = par + 1
    return par % 2



def restore3(bits):
    result = ""
    for i in range(0, len(bits), 3):
        triplet = bits[i] + bits[i+1] + bits[i+2]
        if triplet.count("0") >= 2:   # 2 or 3 zeros
            result = result + "0"
        else:
            result = result + "1"
    return result


bits = "000111111"
print(restore3(bits))
