def factorial(x):
	if x == 1:
		return 1
	else:
		return x * factorial(x-1)

def palindrome(string):
	print(string)
	if len(string) <= 1:
		return True
	if string[0] != string[-1]:
		return False
	return palindrome(string[1:-1])

def bottles(original):

	def actual_bottles(num):

		if num == 1:
			return f"{num} bottle of beers on the wall, {num} bottle of beer. Take one down, pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {original} bottles of beer on the wall."
		
		print(f"{num} bottles of beers on the wall, {num} bottles of beer. Take one down, pass it around, {num-1} bottles of beer on the wall.")

		return actual_bottles(num-1)

	return actual_bottles(original)

def roman_num(num):
	number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
	rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
	i = 12

	while num:
		div = num // number[i]
		num %= number[i]

		while div:
			print(rom[i], end = "")
			div -= 1
		i -= 1

print(factorial(10))
print(palindrome("rarecar"))
print(bottles(10))
roman_num(1234)