from ThirdAlgorithmParser import ThirdAlgorithmParser
from ThirdAlgorithmVisitor import ThirdAlgorithmVisitor

class AlgorithmWithActions(ThirdAlgorithmVisitor):

    def __init__(self):
        self.myvars = {}

    def visitRoot(self, ctx):
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                print(result)

    def visitMultiplicacao(self, ctx: ThirdAlgorithmParser.MultiplicacaoContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MULT():
            return left * right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitSoma(self, ctx: ThirdAlgorithmParser.SomaContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MAIS():
            if isinstance(left, int) and isinstance(right, int):
                return left + right
            if isinstance(left, str) and isinstance(right, str):
                return str(left) + str(right)
            return None
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitSubtracao(self, ctx: ThirdAlgorithmParser.SubtracaoContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MENOS():
            return left - right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitDivisao(self, ctx: ThirdAlgorithmParser.DivisaoContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.DIVISAO():
            return left / right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitPotencia(self, ctx: ThirdAlgorithmParser.PotenciaContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.POT():
            return left ** right
        else:
            raise RuntimeError("Operador não reconhecido")

    def visitValorUnico(self, ctx: ThirdAlgorithmParser.ValorUnicoContext):
        return int(ctx.NUMEROS().getText())

    def visitVariavel(self, ctx: ThirdAlgorithmParser.VariavelContext):
        var_name = ctx.NOME().getText()
        if var_name in self.myvars:
            return self.myvars[var_name]
        else:
            return ctx.NOME().getText()

    def visitAtribuicao(self, ctx: ThirdAlgorithmParser.AtribuicaoContext):
        var = ctx.NOME().getText()
        value = self.visit(ctx.expr())
        self.myvars[var] = value
        if isinstance(value, int):
            return int(value)
        else:
            return value

    def visitLog(self, ctx: ThirdAlgorithmParser.LogContext):
        value = self.visit(ctx.expr())
        return value

    def visitComparacao(self, ctx: ThirdAlgorithmParser.ComparacaoContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.OP_COMPARACAO().getText()

        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right

    def visitBooleano(self, ctx: ThirdAlgorithmParser.BooleanoContext):
        return ctx.BOOL().getText() == 'true'

    def visitCondicoes(self, ctx:ThirdAlgorithmParser.CondicoesContext):
        condition = self.visit(ctx.expr())
        if condition:
            return self.visit(ctx.action(0))
        elif ctx.ELSE():
            return self.visit(ctx.action(1))
        return None