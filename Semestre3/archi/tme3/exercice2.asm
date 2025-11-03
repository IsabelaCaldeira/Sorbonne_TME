.data
.text
	ori $2, $0, 5
	syscall
	
	addi $3, $2, 10
	
	ori $2, $0, 1
	or $4, $0, $3
	syscall
	
	ori $2, $0, 10
	syscall