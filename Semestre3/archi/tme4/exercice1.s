.data
    var1: .word 0xFF         # rÃ©serve un mot (4 octets) contenant la valeur 0x000000FF Ã  lâ€™adresse 0x10010000
    .align 2                 # aligne sur 4 octets (nÃ©cessaire pour les mots)
    .space 4                 # rÃ©serve 4 octets vides (adresse suivante : 0x10010004)
    var2: .word 0x0          # rÃ©serve un mot (4 octets) Ã  0x10010008 (pour exemple)

.text
    lui $8, 0x1001           # charge 0x10010000 dans la partie haute de $8 â†’ $8 = 0x10010000
    ori $8, $8, 0x0000
    lw $9, 0($8)             # charge le mot stockÃ© Ã  lâ€™adresse 0x10010000 dans $9 â†’ $9 = 0x000000FF
    addiu $9, $9, 5          # $9 = $9 + 5 = 0x000000FF + 0x5 = 0x00000104
 
    sw $9, 4($8)             # stocke la valeur de $9 (0x00000104) Ã  lâ€™adresse 0x10010004
    ori $2, $0, 10           # code du syscall 10 (fin du programme)
    syscall                  # termine le programme

.data
 tab:.word 1, 2, 34, 256,-1 # 0x10010000-> 20 octets
 chaine: .asciiz "toto"
 .text
lui $8, 0x1001
ori $8, $8, 0x0000
lw $4, 12($8)
ori $2, $0, 1
syscall
 
lb $4, 16($8)
ori $2, $0, 1 
syscall
ori $2, $0, 10
syscall

 # alinea 2
 lui $8, 0x1001
 ori $8, $8, 0x0011
 ori $4, $8, 0
 ori $5, $0, 32
 ori $2, $0, 8
 syscall

 ori $4, $8, 0
 ori $2, $0, 4
 syscall
 ori $2, $0, 10
 syscall
