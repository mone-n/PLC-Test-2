import re
from syntax_analyzer import RDA

def main():
	# dictionary defining each token code 
	token_definitions = {
		0 : "program beginning",
		1 : "program ending",
		2 : "1 byte integer declaration",
		3 : "2 byte integer declaration",
		4 : "4 byte integer declaration",
		5 : "8 byte integer declaration",
		6 : "while loop",
		7 : "for loop",
		8 : "do while loop",
		9 : "if statement",
		10: "add",
		11: "sub",
		12: "multiply",
		13: "divide",
		14: "modulus",
		15: "lessthan or equal",
		16: "greaterthan or equal",
		17: "lessthan",
		18: "greaterthan",
		19: "equal to",
		20: "not equal to",
		21: "variable assignment",
		22: "left paren",
		23: "right paren",
		24: "separator",
		25: "left bracket",
		26: "right bracket",
		27: "1 byte integer",
		28: "2 byte integer",
		29: "4 byte integer",
		30: "8 byte integer",
		31: "variable"
	}

	# initialize list of tokens
	tokens = []

	# get the code file to be tested
	test_1 = open("test3.txt", "r")
	
	# regex separated into individual matching groups for readability
	# each group directly corresponds to a single token code
	symbols = ["(start)", "(end)", "(tiny)", "(medi)", "(big)", "(huge)",
	 "(conloop)", "(forloop)", "(perform)", "(\?)", "(\+)", "(-)", "(\*)",
	 "(\/)", "(%)", "(<=)", "(>=)", "(<)", "(>)", "(==)", "(\!=)", "(=)",
	 "(\()", "(\))", "(\|)", "(\{)", "(\})", "([0-9]+t)", "([0-9]+m)",
	 "([0-9]+B)", "([0-9]+H)", "([a-zA-Z_]{6,8})"]

	# read the test code file
	file = test_1.read()

	# combine the separate regex groups into one regex pattern
	pattern = "|".join(symbols)

	
	lexeme_index = 0
	
	# re.match gets the first match in a string. so this gets
	# the first match
	match = re.match(pattern, file)

	# individually read the next token and determine if it is a valid
	# token until EOF is reached.
	while match is not None and match[0]:

		# replace the current match with nothing
		file = file.replace(match[0], '', 1)

		# then remove whitespace at the front of the string
		file = file.lstrip()

		# add the current token to the tokens list
		tokens.append(match[0])

		# print current token in the format:
		# Lexeme at index  1 is var_name  Next token is (28) variable
		print("Lexeme at index {:2d} is: {:10s}Token is ({:2d}) {:s}".format(
			lexeme_index,
			match[0],
			match.groups().index(match[0]),
			token_definitions[match.groups().index(match[0])]
			)
		)

		# increment lexeme index
		lexeme_index += 1

		# get the next token if any
		match = re.match(pattern, file)
	
	# since re.match only matches at the beginning of a string
	# it will return null when an invalid token is processed,
	# and break the while loop above.
	# If the while loop condition fails early, a token at the
	# current index is invalid
	if len(file) > 0:
		print("lexeme at index {:2d} is invalid\n".format(len(tokens)))

	# otherwise, all lexemes are valid, and the syntax_analyzer
	# can be run.
	else:
		syntax_analyzer = RDA(tokens)
		if syntax_analyzer.validated:
			print("syntax analysis passed")
		else:
			print("syntax analysis failed")




if __name__ == "__main__":
	main()