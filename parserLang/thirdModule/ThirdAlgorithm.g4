grammar ThirdAlgorithm;
root: action+ EOF;
action: NOME ATRIBUICAO expr ';' #Atribuicao
      | 'logger('  expr ');' #Log
      ;

expr: <assoc=right> expr POT expr #Potencia
    | expr MULT expr #Multiplicacao
    | expr DIVISAO expr #Divisao
    | expr MENOS expr #Subtracao
    | expr MAIS expr #Soma
    | NOME #Variavel
    | NUMEROS #ValorUnico
    ;
MAIS : '+' ;
MENOS: '-';
DIVISAO: '/';
MULT: '*';
POT: '^';
NOME: [a-zA-Z]+;
ATRIBUICAO: '===';
NUMEROS: [0-9]+ ;
WS : [ \n\t\r]+ -> skip;