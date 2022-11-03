def repeat(msg,k):
    result = ""
    for bit in msg:
        result = result + bit*k
    return result



def restore3(bits):
    result = ""
    for i in range(0, len(bits), 3):
        triplet = bits[i] + bits[i+1] + bits[i+2]
        if triplet.count("0") >= 2:   # 2 or 3 zeros
            result = result + "0"
        else:
            result = result + "1"
    return result


bits = "011111111"
print(restore3(bits))


def restore_single(single_msg):
    # We initialize counters
    cnt1 = 0
    cnt0 = 0

    # We go over the characters in the message
    for bit in single_msg:
        if bit == "1":
            cnt1 = cnt1 + 1
        else:
            cnt0 = cnt0 + 1

    if cnt1 > cnt0:
        return "1"
    else:
        return "0"


print(restore_single("1111111"))
print(restore_single("0101010"))
print(restore_single("100000000000001"))


# The complete solution
def restore(msg, k):
    # We initialize an empty string
    result = ""
    # We got over the message in k-bit blocks
    for i in range(0, len(msg), k):
        # We get the next block
        k_bits = get_block(msg, i, k)

        # We restore it
        bit = restore_single(k_bits)

        # We add the bit to our result
        result = result + bit
    return result


def get_block(msg, i, k):
    # We initialize an empty string
    k_bits = ""

    # We go over the characters in the appropriate indices
    for j in range(i, i + k):
        k_bits = k_bits + msg[j]

    # We return the result
    return k_bits


def restore_single(single_msg):
    # We initialize counters
    cnt1 = 0
    cnt0 = 0

    # We go over the characters in the message
    for bit in single_msg:
        if bit == "1":
            cnt1 = cnt1 + 1
        else:
            cnt0 = cnt0 + 1

    if cnt1 > cnt0:
        return "1"
    else:
        return "0"


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Decoding '1111100000' with k = 5")
ans = restore('1111100000', 5)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Decoding '0111101010' with k = 5")
ans = restore('0111100110', 5)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Decoding '11110000101010' with k = 7")
ans = restore('11110000101010', 7)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)


    def restore(msg, k):
        restoreK = ""
        k_bits = msg[:]
        for k in msg:

            def restore(msg, k):
                restoreK = ""
                for i in (msg):
                    k_bits = msg[:k + 1]
                    for i in k_bits:
                        zero = k_bits.count("0")
                        one = k_bits.count("1")
                        if one > zero:
                            k_bits = k_bits + "1"
                        else:
                            k_bits = k_bits + "0"
                        msg = msg[k:]


    # The complete solution
    def restore(msg, k):
        # We initialize an empty string
        result = ""
        # We got over the message in k-bit blocks
        for i in range(0, len(msg), k):
            # We get the next block
            k_bits = get_block(msg, i, k)

            # We restore it
            bit = restore_single(k_bits)

            # We add the bit to our result
            result = result + bit
        return result