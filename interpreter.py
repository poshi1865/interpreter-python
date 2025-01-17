#this class will interpret the tree
from nodes import *
from values import Number

 #we will pass the root node over the tree
 #the interpreter will process that tree 
 #and return a number
class Interpreter:
	def __init__(self):
		pass
		
	def visit(self, node):
		method_name = f'visit{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)

	def visit_NumberNode(self, node):
		return Number(node.value)

	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	def visit_SbtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

	def visit_DivideNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except:
			raise Exception("Runtime math error")

	def visit_PlusNode(self, node):
		return self.visit(node.node)

	def visit_MinusNode(self, node):
		return Number(-self.visit(node.node).value)