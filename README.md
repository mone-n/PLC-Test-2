# PLC Test 2
# Regular Expressions
(start)|(finish)|(tiny)|(medi)|(big)|(huge)|(conloop)|(forloop)|(perform)|(\?)|(\+)|(-)|(\*)|(\/)|(%)|(<=)|(>=)|(<)|(>)|(==)|(\!=)|(=)|(\()|(\))|(\|)|(\{)|(\})|([0-9]+)|([a-zA-Z_]{6,8})

regular expression matches keywords, symbols, and variable names in separate
matching groups.

# integer token codes
0 : "program beginning"
1 : "program ending"
2 : "1 byte integer declaration"
3 : "2 byte integer declaration"
4 : "4 byte integer declaration"
5 : "8 byte integer declaration"
6 : "while loop"
7 : "for loop"
8 : "do while loop"
9 : "if statement"
10: "add"
11: "sub"
12: "multiply"
13: "divide"
14: "modulus"
15: "lessthan or equal"
16: "greaterthan or equal"
17: "lessthan"
18: "greaterthan"
19: "equal to"
20: "not equal to"
21: "variable assignment"
22: "left paren"
23: "right paren"
24: "separator"
25: "left bracket"
26: "right bracket"
27: "integer"
28: "variable name"

# example output of lexer.py
Next lexeme is: start     Next token is ( 0) program beginning
Next lexeme is: tiny      Next token is ( 2) 1 byte integer declaration
Next lexeme is: var_aa    Next token is (28) variable name
Next lexeme is: |         Next token is (24) separator
Next lexeme is: var_aa    Next token is (28) variable name
Next lexeme is: =         Next token is (21) variable assignment
Next lexeme is: (         Next token is (22) left paren
Next lexeme is: 1         Next token is (27) integer
Next lexeme is: +         Next token is (10) add
Next lexeme is: 2         Next token is (27) integer
Next lexeme is: /         Next token is (13) divide
Next lexeme is: 3         Next token is (27) integer
Next lexeme is: )         Next token is (23) right paren
Next lexeme is: %         Next token is (14) modulus
Next lexeme is: 12        Next token is (27) integer
Next lexeme is: /         Next token is (13) divide
Next lexeme is: 2         Next token is (27) integer
Next lexeme is: |         Next token is (24) separator
Next lexeme is: perform   Next token is ( 8) do while loop
Next lexeme is: {         Next token is (25) left bracket
Next lexeme is: var_aa    Next token is (28) variable name
Next lexeme is: =         Next token is (21) variable assignment
Next lexeme is: var_aa    Next token is (28) variable name
Next lexeme is: +         Next token is (10) add
Next lexeme is: 1         Next token is (27) integer
Next lexeme is: |         Next token is (24) separator
Next lexeme is: }         Next token is (26) right bracket
Next lexeme is: conloop   Next token is ( 6) while loop
Next lexeme is: (         Next token is (22) left paren
Next lexeme is: var_aa    Next token is (28) variable name
Next lexeme is: <=        Next token is (15) lessthan or equal
Next lexeme is: 100       Next token is (27) integer
Next lexeme is: )         Next token is (23) right paren
Next lexeme is: finish    Next token is ( 1) program ending