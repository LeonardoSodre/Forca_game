import random

#METODO PARA DEFINIR ALEATORIAMENTE A PALAVRA 
#ARMAZENO NA VARIAVEL PALAVRA E RETORNO EM LETRAS MAIUSCULAS
def defina_palavra():
    lista_palavras = [' Rosa', 'Margarida', ' Orquidea', 'Cravo', 'Jasmim','Begonia']
    palavra = radom.choice(lista_palavras)
    return palavra.upper() 

def exibir_forca(tentativas):

    estagios = [  # CABEÇA, TRONCO, BRAÇOS E PERNAS: MORTE.
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                #CABEÇA, TRONCO, BRAÇOS E PERNAS
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                #CABEÇA, TRONCO E BRAÇOS
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                #CABEÇA, TRONCO E BRAÇOS
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                #CABEÇA E TRONCO
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                #CABEÇA
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                #VAZIO
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return estagios[tentativas]    


def jogar(palavra):
     palavra_conclusa = "_" * len(palavra)
     adivinhou = False
     adivinhou_letras = []
     adivinhou_palavras = []
     tentativas = 6
     print("JOGO DA FORCA! \n DICA: É UMA FLOR E TEM {} LETRAS".format(len(palavra)))     
     print(exibir_forca(palavra))
     print(palavra_conclusa)
     print("\n")

     while not adivinhou and tentativas >0:
        palpite = input('Arrisque uma letra: ').upper()
        if len(palpite) == 1 and palpite.isalpha():
           if palpite in adivinhou_letras:
              print('Voce ja tentou: '+ palpite)
              print(adivinhou_letras)
           elif palpite not in palavra:
               print(palavra + 'Não')
               tentativas -= 1 
               adivinhou_letras.append(palpite)
           else:
                 print(palpite, "Está na palavra!")
                 adivinhou_letras.append(palpite)
                 palavras_na_lista = list(palavra_conclusa)
                 indices = [i for i, carta in enumerate(palavra) if carta == palpite]
                 for x in indices:
                     palavras_na_lista[x]= palpite
                 palavra_conclusa = "".join(palavras_na_lista)
                 if "_"  not in palavra_conclusa:
                     adivinhou = True   
        elif len(palpite) == len(palavra) and palpite.isalpha():
             if palpite in adivinhou_palavras:
               print('Voce ja tentou a palavra: ', palpite)
             elif palpite != palavra:
               print(palpite, 'Não é palavra')
               tentativas -=1
               adivinhou_palavras.append(palpite)
             else:
                adivinhou = True
                palavra_conclusa = palavra
        else:
            print('Invalido')
            
        print(exibir_forca(tentativas))
        print(palavra_conclusa)
        print('\n')

     if adivinhou == True:
        print('Parabens, voce adinhou a palavra!')
     else:
        print('Voce Perdeu! A palavra era' , palavra, ".")   


def main():
   palavra = (defina_palavra)
   jogar(palavra)
   
   while input('Jogar de novo ? (S/N').upper() == 'S':
      palavra = defina_palavra()
      jogar(palavra)
      
if __name__ == "__main__":
   main()
