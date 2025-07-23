from AlgorithmLexer import AlgorithmLexer
from AlgorithmParser import *
from MathOperations import AlgorithmExecutor

input_stream = InputStream(input('Enter algorithm -> '))
visitor = AlgorithmExecutor()
print("Resulted:", visitor.visit(AlgorithmParser(CommonTokenStream(AlgorithmLexer(input_stream))).root()))
