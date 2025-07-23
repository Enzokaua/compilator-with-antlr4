from AlgorithmParser import AlgorithmParser
from AlgorithmVisitor import AlgorithmVisitor

class SubSumMulDivAlgorithm(AlgorithmVisitor):
    def visitRoot(self, ctx):
        return self.visit(ctx.expr())

    def visitMultiplicacao(self, ctx: AlgorithmParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MULT():
            return left * right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitSoma(self, ctx: AlgorithmParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MAIS():
            return left + right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitSubtracao(self, ctx: AlgorithmParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MENOS():
            return left - right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitDivisao(self, ctx: AlgorithmParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.DIVISAO():
            return left / right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitPotencia(self, ctx: AlgorithmParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.POT():
            count = right
            result = left
            while count > 1:
                result = result * left
                count -= 1
            return result
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitValorUnico(self, ctx: AlgorithmParser.ExprContext):
        return int(ctx.NUMEROS().getText())