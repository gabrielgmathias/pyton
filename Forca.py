def jogar():
    print("*********************")
    print('***BEM VINDO AO JOGO DA FORCA!***')
    print("*********************")
    
    palavra_secreta ="maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] 
    letras_acertadas2 =[]
    
    for letra in (palavra_secreta):
        letras_acertadas2.append("_")
        
        enforcou = False
        acertou = False
        erros = 0
        
        print(letras_acertadas)
        
        while (not enforcou and not acertou):
            
            chute = input("qual letra? ")
            chute = chute.strip().upper()
