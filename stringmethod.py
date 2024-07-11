name="^^Vibhanshu Singh^^"
print(len(name))
print(name.lower())
print(name.upper())
print(name.strip("^^"))
#strip ko gayab karne ke liye aage piche dono
print(name.rstrip("^"))
#rstrip se hide ho jati h strip but only in end
print(name.replace("Vibhanshu","vibhu"))
print(name.split())
print(name.capitalize())
print(name.center(45))
print(name.count("s"))
print(name.endswith("!"))
print(name.find("xxx"))
print(name.index("n"))
#The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(name.isalnum())
#The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
print(name.isalpha())
#The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(name.islower())#
#The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(name.isprintable())
#The isprintable() method returns True if all the values within the given string are printable, if not, then return False
print(name.isspace())
#The isspace() method returns True only and only if the string contains white spaces, else returns False.
print(name.istitle())
#The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False
print(name.isupper())
#The isupper() method returns True if all the characters in the string are upper case, else it returns False.
print(name.startswith("python"))
print(name.swapcase())
#The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case
print(name.title())
#title capitalizes each first lettter of word



