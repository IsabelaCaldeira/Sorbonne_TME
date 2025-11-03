.data
.text
    #Pour lire un entier au clavier
    ori $2, $0, 5
    syscall
    
    #Donne le valeur à $9
    ori $9, $2, $zero

    #Pour lire un entier au clavier
    ori $2, $0, 5
    syscall
    
    #Donne le valeur à $10
    ori $10, $2, $zero

    #division
    div $9,$10
    #on recuper les quotient et le reste  
    mflo $11
    mfhi $12

    #affiche le quotient 
    ori $2, $0, 1
    addu $4, $11 $zero
    syscall

    #affiche le reste
    ori $2, $0, 1
    addu $4, $12 $zero
    syscall

    #calculer l'inverse
    mult $11, $10
    mflo $13
    addu $13, $13, $12

    #affichage 
    ori $2, $0, 1
    addu $4, $13 $zero
    syscall

    #appel systeme pour exit
    ori $2, $zero, 10	
    syscall
