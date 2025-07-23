from AlgorithmLexer import AlgorithmLexer
from AlgorithmParser import *
from OperationalLogics import AlgorithmExecutor

input_stream = InputStream(input('Enter algorithm -> '))
visitor = AlgorithmExecutor()
print("Resulted:", visitor.visit(AlgorithmParser(CommonTokenStream(AlgorithmLexer(input_stream))).root()))
