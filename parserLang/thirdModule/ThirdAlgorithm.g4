grammar ThirdAlgorithm;
root: action+ EOF;
action: IF '(' expr ')' action (ELSE action)? #Condicoes
      | NOME ATRIBUICAO expr ';' #Atribuicao
      | 'logger('  expr ')' ';' #Log
      ;

expr: <assoc=right> expr POT expr #Potencia
    | expr MULT expr #Multiplicacao
    | expr DIVISAO expr #Divisao
    | expr MENOS expr #Subtracao
    | expr MAIS expr #Soma
    | expr OP_COMPARACAO expr #Comparacao
    | NOME #Variavel
    | BOOL #Booleano
    | NUMEROS #ValorUnico
    ;

MAIS : '+' ;
MENOS: '-';
DIVISAO: '/';
MULT: '*';
POT: '^';
IF: 'case';
ELSE: 'when';
NOME: [a-zA-Z]+;
ATRIBUICAO: '===';
OP_COMPARACAO: '==' | '!=' | '>' | '<' | '>=' | '<=';
BOOL: 'true' | 'false';
NUMEROS: [0-9]+ ;
WS : [\n\t\r]+ -> skip;