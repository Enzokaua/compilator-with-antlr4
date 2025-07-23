# Compilador utilizando Antlr4

Este projeto visa o estudo de compiladores, inicialmente na camada de análise lexa, tokenização e análise sintática usando o Antlr4. O próximo passo, será usando o LLVM para realizar a interpretação (ou compilação) nativa para binário ou assemblyCode. 

---

## 🛠️ Tecnologias Utilizadas

- **Antlr4**: Versão 4.13.0
- **Python**: Versão 3.12.0
---

## 🚀 Funcionalidades

1. Soma de 2 números inteiros.
2. Subtração de 2 números inteiros.

---

## 📋 Como Executar
1- Clone este repositório:
```bash
git clone https://github.com/enzokaua/compilator-with-antlr4.git
```

2- Navegue até a pasta do projeto:
```bash
cd compilator-with-antlr4
```

3- Gere o parser e o visitor com o comando abaixo:
```bash
java -jar C:\antlr4\antlr-4.13.0-complete.jar -Dlanguage=Python3 -no-listener -visitor Algorithm2.g4
```

4- Rode o arquivo Main:
```bash
python FirstAlgorithMain.py
```

