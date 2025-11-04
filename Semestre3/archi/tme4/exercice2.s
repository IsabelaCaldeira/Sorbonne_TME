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
