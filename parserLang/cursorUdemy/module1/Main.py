from AlgorithmLexer import AlgorithmLexer
from AlgorithmParser import *
from SubSumMulDivAlgorithm import SubSumMulDivAlgorithm

input_stream = InputStream(input('Enter algorithm -> '))
visitor = SubSumMulDivAlgorithm()
print("Resulted:", visitor.visit(AlgorithmParser(CommonTokenStream(AlgorithmLexer(input_stream))).root()))
