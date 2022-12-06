import re

class RDA:
	def __init__(self, tokens):
		self.tokens = tokens
		self.index = 0
		self.validated_tokens = []
		self.currToken = self.tokens[self.index]
		self.validated = False
		self.block()
		self.validated = True


	# raises an error giving the token at fault
	# and the index of the token at fault
	def error(self):
		raise Exception('error with token: (' + self.currToken + ") at token index: " + str(self.index))


	# adds the previous token to a list of validated tokens
	# then increments the current token index
	# and sets the current token to the next token
	def nextToken(self):
		self.validated_tokens.append(self.currToken)
		if self.index < len(self.tokens) - 1:
			self.index += 1
		self.currToken = self.tokens[self.index]
		

	# returns true the current token integer is valid variable name
	# returns false otherwise
	def validate_var(self):
		if re.findall('[a-zA-Z_]{6,8}', self.currToken) != []:
			return re.findall('[a-zA-Z_]{6,8}', self.currToken)[0] == self.currToken
		return False


	# returns true the current token integer is a number
	# returns false otherwise
	def validate_int(self):
		if re.findall('[0-9]+[tmBH]?', self.currToken) != []:
			return re.findall('[0-9]+[tmBH]?', self.currToken)[0] == self.currToken
		return False


	# <block> --> 'start' {<statement>} 'end'
	def block(self):
		if self.currToken == "start":
			self.nextToken()

			while self.currToken in ['?', 'conloop', 'perform', 'tiny', 'medi', 'big', 'huge'] \
			or self.validate_var():
				self.statement()

			if self.currToken == 'end':
				self.nextToken()

			else:
				self.error()
		else:
			self.error()


	# <Statement> --> <if> | <while> | <do> | <initialize> | <assignment> 
	def statement(self):
		# test for if statement
		if self.currToken == '?':
			self.if_statement()

		# test for while loop
		elif self.currToken == 'conloop':
			self.while_loop()

		# test for do while loop
		elif self.currToken == 'perform':
			self.do_while_loop()

		# test for variable initialization
		elif self.currToken in ['tiny', 'medi', 'big', 'huge']:
			self.initialize()

		# test for a variable assignment
		elif self.validate_var():
			self.assignment()

		# throw error
		else:
			self.error()


	# <if> --> '?' '(' <brel> ')' '{' {<statement>} '}'
	def if_statement(self):
		if self.currToken == '?':
			self.nextToken()

			if self.currToken == '(':
				self.nextToken()
				self.brel()
			
				if self.currToken == ')':
					self.nextToken()
			
					if self.currToken == '{':
						self.nextToken()

						while self.currToken != '}':
							self.statement()
						self.nextToken()
						
					else:
						self.error()
				else:
					self.error()
			else:
				self.error()
		else:
			self.error()


	# <while> --> 'conloop' '(' <brel> ')' '{' {<statement>} '}'
	def while_loop(self):
		if self.currToken == 'conloop':
			self.nextToken()

			if self.currToken == '(':
				self.nextToken()
				self.brel()

				if self.currToken == ')':
					self.nextToken()

					if self.currToken == '{':
						self.nextToken()
						
						while self.currToken in ['?', 'conloop', 'perform', 'tiny', 'medi', 'big', 'huge'] \
						or self.validate_var():
							self.statement()

						if self.currToken == '}':
							self.nextToken()

						else:
							self.error()
					else:
						self.error()
				else:
					self.error()
			else:
				self.error()
		else:
			self.error()


	# <do> --> 'perform' '{' {<statemen>} '}' 'conloop' '(' <brel> ')'
	def do_while_loop(self):
		if self.currToken == 'perform':
			self.nextToken()

			if self.currToken == '{':
				self.nextToken()
				
				while self.currToken in ['?', 'conloop', 'perform', 'tiny', 'medi', 'big', 'huge'] \
				or self.validate_var():
					self.statement()

				if self.currToken == '}':
					self.nextToken()
					
					if self.currToken == 'conloop':
						self.nextToken()

						if self.currToken == '(':
							self.nextToken()
							self.brel()

							if self.currToken == ')':
								self.nextToken()

							else:
								self.error()
						else:
							self.error()
					else:
						self.error()
				else:
					self.error()
			else:
				self.error()
		else:
			self.error()


	#<initialize> --> ('tiny'|'medi'|'big'|'huge') [a-zA-Z_]{6,8} '|'
	def initialize(self):
		if self.currToken in ['tiny', 'medi', 'big', 'huge']:
			self.nextToken()

			if self.validate_var():
				self.nextToken()

				if self.currToken == '|':
					self.nextToken()

				else:
					self.error()
			else:
				self.error()
		else:
			self.error()


	#<assignment> --> [a-zA-Z_]{6,8} '=' <expr> '|'
	def assignment(self):
		if self.validate_var:
			self.nextToken()

			if self.currToken == '=':
				self.nextToken()
				self.expr()
				
				if self.currToken == '|':
					self.nextToken()

				else:
					self.error()
			else:
				self.error()
		else:
			self.error()


	#<bool_relation> --> <bexpr> {'!='|'==' <bexpr>} 
	def brel(self):
		self.bexpr()
		while self.currToken in ['!=', '==']:
			self.nextToken()
			self.bexpr()


	#<bexpr> --> <expr> {'<='|'>='|'<'|'>' <expr>}
	def bexpr(self):
		self.expr()
		while self.currToken in ['<=', '>=', '<', '>']:
			self.nextToken()
			self.expr()


	#<expr> --> <term> {'*'|'/'|'%' <term>}
	def expr(self):
		self.term()
		while self.currToken in ['*', '/', '%']:
			self.nextToken()
			self.term()


	#<term> --> <bnot> {'+'|'-'|'^' <bnot>}
	def term(self):
		self.bnot()
		while self.currToken in ['+', '-', '^']:
			self.nextToken()
			self.bnot()


	#<bnot> --> [!] <factor>
	def bnot(self):
		if self.currToken == '!':
			self.nextToken()
		self.factor()


	# <factor> --> [0-9]+[tmBH]? | [a-zA-Z_]{6,8} | '(' <bexpr> ')'
	def factor(self):
		if self.validate_var() or self.validate_int():
			self.nextToken()
			return

		elif self.currToken == '(':
			self.nextToken()
			self.bexpr()

			if self.currToken == ')':
				self.nextToken()

			else:
				self.error()

		else:
			self.error()
			
