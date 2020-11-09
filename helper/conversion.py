import re

amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"

word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"
value_re = rf"\${number}"
'''
money_conversion("$12.2 million") --> 12200000	## Word syntax
money_conversion("$790,000") --> 790000			## Value syntax
'''
def word_to_value(word):
	value_dict = {"thousand": 1000, "million":1000000, "billion":1000000000}
	return value_dict[word]

def parse_word_syntax(string):
	value_string = re.search(number, string).group()
	value = float(value_string.replace(",", ""))
	word_string = re.search(amounts, string).group()
	word = float(word_to_value(word_string))
	return value * word

def parse_value_syntax(string):
	value_string = re.search(number, string).group()
	value = float(value_string.replace(",", ""))
	return value

def money_conversion(money):

	if isinstance(money, list):
		money = money[0]
	
	word_syntax = re.search(word_re, money)
	value_syntax = re.search(value_re, money)

	if word_syntax:
		return parse_word_syntax(word_syntax.group())
		# print(word_syntax.group())

	elif value_syntax:
		return parse_value_syntax(value_syntax.group())
		# print(value_syntax.group())

print(money_conversion("$3.5–4 million"))
