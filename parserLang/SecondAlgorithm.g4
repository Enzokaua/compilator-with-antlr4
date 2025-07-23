grammar Algorithm;
root: expr EOF;
expr: expr MAIS expr
    | expr MENOS expr
    |	NUMEROS
    ;
MAIS : '+' ;
MENOS: '-';
NUMEROS: [0-9]+ ;
WS : [ \n\t\r]+ -> skip;