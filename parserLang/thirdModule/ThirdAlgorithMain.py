from ThirdAlgorithmLexer import ThirdAlgorithmLexer
from ThirdAlgorithmParser import *
from AlgorithmWithActions import AlgorithmWithActions
import sys

def main():
    print(':: STUPIDSCRIPT :: version 1.0.0 🚀!!!')
    visitor = AlgorithmWithActions()  # Cria uma única instância
    input_stream = FileStream(sys.argv[1])
    lexer = ThirdAlgorithmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ThirdAlgorithmParser(token_stream)
    tree = parser.root()
    visitor.visit(tree)

if __name__ == "__main__":
    main()