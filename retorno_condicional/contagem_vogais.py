def get_count1(input_str):
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for x in input_str:
        if x in vowels:
            num_vowels += 1
    return num_vowels


def get_count2(input_str):
    return sum(1 for let in input_str if let in "aeiou")


def get_count3(input_str):
    return sum(c in "aeiou" for c in input_str)
