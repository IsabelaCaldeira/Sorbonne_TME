.data
.text
    lui $3 0xAABB	#on charge la partie haute
    ori $3, $3, 0xCCDD	#on charge la partie basse
    ori $2, $zero, 34
    add $4, $3, $zero
    syscall

    ori $2, $zero, 10
    syscall