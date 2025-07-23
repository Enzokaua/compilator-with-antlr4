from AlgorithmParser import AlgorithmParser
from AlgorithmVisitor import AlgorithmVisitor

class AlgorithmExecutor(AlgorithmVisitor):
    def visitRoot(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: AlgorithmParser.ExprContext):
        if ctx.NUMEROS():
            return int(ctx.NUMEROS().getText())
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MAIS():
            return left + right
        elif ctx.MENOS():
            return left - right
        else:
            raise RuntimeError("Operador não reconhecido")