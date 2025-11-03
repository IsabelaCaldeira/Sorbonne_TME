.data
.text
   ori $8, $0, 137
   addu $4, $8, $0       # $4 = $8 = 137 → valeur à afficher
   syscall               # affiche la valeur contenue dans $4

  ori $2, $0, 10        # $2 = 10 (exit)
  syscall               # quitte le programme
