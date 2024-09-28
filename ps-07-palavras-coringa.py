"""
Lucas Martins Primo
12021EBI022
"""

def main():
 
  l = int(input()) # Lê o número de linhas que o texto tera
  texto = ""   
  for i in range(l):
    texto+=input() + " " #Pega o texto linha por linha do usuário e adiciona a variável texto o (" ") adiciona uma linha entre as frases

  n = int(input()) # recebe o número de palavras
  palavras = ""

  for i in range(n):
    palavras += input() + " " # adiciona as palavras na variavel palavras

  tratamento(texto, palavras)

def tratamento(texto, palavras):

  nao_pode = ".,:;!?"
  
  #tratamento do texto
  texto = texto.lower()#coluca tudo em diminuitivo
  for j in nao_pode:
    texto = texto.replace(j,"") #retira a pontuacao definida em nao_pode
  texto = texto.split() #Separando as palavras do texto

  #Tratamento das palavras buscadas

  palavrasAux = palavras
  palavrasAux = palavrasAux.split()

  for i in nao_pode:
    palavras = palavras.replace(i,"") #retira a pontuacao definida em nao_pode

  palavras = palavras.lower()
    

  palavras = palavras.split() # separando as palavras para fazer buscas independentes
  
  busca(texto, palavras, palavrasAux)
     
def busca(texto, palavras, palavrasAux):

  for i in range(len(palavras)):
    parecidas = 0
    iguais = 0
    for j in range(len(texto)):
      #verifica se tem * na palavra
      if "*" in palavras[i] and len(texto[j]) >= len(palavras[i]):
         
          palavra_teste = palavras[i]
          texto_teste = texto[j]
          
          auxiliar_palavras = list(palavra_teste)
          auxiliar_texto = list(texto_teste)

          for k in range(len(palavras[i])):
            # se tivero '*' deleta ele da palavra, e se tiver no texto tira também
            if auxiliar_palavras[k] == '*':
              auxiliar_palavras[k] =  ''
              auxiliar_texto[k] = ''
          #voltar a ser strings
          palavra_teste = "".join(auxiliar_palavras)
          texto_teste = "".join(auxiliar_texto)
          #Contador para palavras com "*"
          if palavra_teste == texto_teste:
            iguais+=1
          elif texto_teste.count(palavra_teste) != 0:
            parecidas+=1
      #Contador para palavras sem "*'
      elif palavras[i] == texto[j]:
        iguais+=1
      elif texto[j].count(palavras[i]) != 0:
        parecidas+=1
         
    print1(palavras, iguais, parecidas, i, palavrasAux) 

    
def print1(palavras, iguais, parecidas, i, palavrasAux):
  print("Palavra buscada:",palavrasAux[i])
  print("Ocorrencia:",iguais)
  print("Palavras similares:",parecidas)
  
main()
  
