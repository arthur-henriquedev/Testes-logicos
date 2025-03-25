Algoritmo "MediaNotas"

Var
    nota1, nota2, nota3, media: Real  // Variáveis para as 3 notas e a média

Inicio
    escreva("Nota 1: ")
    leia(nota1)

    escreva("Nota 2: ")
    leia(nota2)

    escreva("Nota 3: ")
    leia(nota3)

    media <- (nota1 + nota2 + nota3) / 3 //Fórmula da média

 se media >= 7 ENTAO
  escreva("Você foi aprovado.")
 SENAO media <= 7 ENTAO
  escreva("Você foi reprovado.")
  fimse

Fimalgoritmo