import re
from collections import defaultdict

def main():
	tokens = defaultdict(list)
	test_1 = open("test2.txt", "r")

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
		27: "integer",
		28: "variable name"
	}
	
	symbols = ["(start)", "(finish)", "(tiny)", "(medi)", "(big)", "(huge)",
	 "(conloop)", "(forloop)", "(perform)", "(\?)"]

	symbols += ["(\+)", "(-)", "(\*)", "(\/)", "(%)", "(<=)", "(>=)", "(<)", "(>)", "(==)",
	 "(\!=)", "(=)", "(\()", "(\))", "(\|)", "(\{)", "(\})", "([0-9]+)", "([a-zA-Z_]{6,8})"]

	pattern = "|".join(symbols)
	result = re.findall(pattern, test_1.read())

	for match in result:
		token = next(s for s in match if s)
		print("Next lexeme is: {:10s}Next token is ({:2d}) {:s}".format(
			token,
			match.index(token),
			token_definitions[match.index(token)]
			)
		)




if __name__ == "__main__":
	main()