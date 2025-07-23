grammar Algorithm;
root: expr EOF;
expr: <assoc=right> expr POT expr #Potencia
    | expr MULT expr #Multiplicacao
    | expr DIVISAO expr #Divisao
    | expr MENOS expr #Subtracao
    | expr MULT expr #Multiplicacao
    | expr MAIS expr #Soma
    |	NUMEROS #ValorUnico
    ;
MAIS : '+' ;
MENOS: '-';
DIVISAO: '/';
MULT: '*';
POT: '^';
NUMEROS: [0-9]+ ;
WS : [ \n\t\r]+ -> skip;