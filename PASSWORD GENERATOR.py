import string
import random
print("WELCOME TO THE PASSWORD GENERATOR")
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.hexdigits

    plen = int(input("Enter password length\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("Your password is: ")
    print("".join(random.sample(s, plen)))
    print("Thanks For Using Password Generator!")
