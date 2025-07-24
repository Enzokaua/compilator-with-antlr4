from ThirdAlgorithmLexer import ThirdAlgorithmLexer
from ThirdAlgorithmParser import *
from AlgorithmWithActions import AlgorithmWithActions

def main():
    print(':: STUPIDSCRIPT :: version 1.0.0 | port 8080 | Enter your code 🚀!!!')
    visitor = AlgorithmWithActions()  # Cria uma única instância

    while True:
        try:
            input_stream = InputStream(input(':::'))
            lexer = ThirdAlgorithmLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = ThirdAlgorithmParser(token_stream)
            tree = parser.root()

            result = visitor.visit(tree)  # Usa a mesma instância

            if result is not None:
                print("Result:", result)

        except Exception as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()