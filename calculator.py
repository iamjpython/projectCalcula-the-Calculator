import math
import operator
from pyparsing import *

stack = []

def push_stack(toks):
	stack.append(toks[0])

def push_negative(toks):
	for t in toks:
		if t == '-':
			stack.append("unary -")
		else:
			break

parsed = None

def Parsing():
	global parsed
	if not parsed:
		pi = CaselessKeyword("PI")
		fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
		ident = Word(alphas, alphanums + "_$")

		plus, minus, mult, div = map(Literal, "+-*/")
		lpar, rpar = map(Suppress, "()")
		add_operation = plus | minus
		mult_operation = mult | div
		exp_operation = Literal("^")

		expr = Forward()
		expr_list = delimitedList(Group(expr))

		def insert_fn_argcount_tuple(t):
			fn = t.pop(0)
			num_args = len(t[0])
			t.insert(0, (fn, num_args))

		fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(insert_fn_argcount_tuple)
		atom = (
			add_operation[...]
			+ (
				(fn_call | pi | fnumber | ident).setParseAction(push_stack)
				| Group(lpar + expr + rpar)
			)
		).setParseAction(push_negative)

		factor = Forward()
		factor <<= atom + (exp_operation + factor).setParseAction(push_stack)[...]
		term = factor + (mult_operation + factor).setParseAction(push_stack)[...]
		expr <<= term + (add_operation + term).setParseAction(push_stack)[...]
		parsed = expr

	return parsed

operations = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.truediv,
	"^": operator.pow,
}

functions = {
	"sin": math.sin, # sin(60)
	"cos": math.cos,
	"tan": math.tan,
	"arcsin": math.asin,
	"arccos": math.acos, 
	"arctan": math.atan,
	"sqrt": math.sqrt,
	"fact": math.factorial,
	"log": math.log10,
	"ln": math.log,
	}


def process(s):
	op, num_args = s.pop(), 0
	if isinstance(op, tuple):
		op, num_args = op
	if op == "unary -":
		return -process(s)
	if op in "+-*/^":
		try:
			operation_2 = process(s)
			operation_1 = process(s)
			return operations[op](operation_1, operation_2)
		except:
			return "MATH ERROR"
	elif op == "PI":
		return round(math.pi, 2)
	elif op in functions:
		try:
			args = reversed([process(s) for _ in range(num_args)])
			return functions[op](*args)
		except ValueError:
			return "MATH ERROR"
	elif op[0].isalpha():
		raise Exception("Invalid Identifier '%s'" % op)
	else:
		try:
			return int(op)
		except ValueError:
			return float(op)

def solve(s):
	
	try:
		stack[:] = []
		results = Parsing().parseString(s, parseAll = True)
		val = process(stack[:])
		return val
	except:
		return 'SYNTAX ERROR'