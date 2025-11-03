.data
.text
    ori $9, $0, 84
    ori $10, $0, 10
    div $9, $10

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
    mult $11, $12
    mflo $13
    addu $13, $13, $12

    #affichage 
    ori $2, $0, 1
    addu $4, $13 $zero
    syscall

    #appel systeme pour exit
    ori $2, $zero, 10	
    syscall
