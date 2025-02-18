#include <stdio.h>

int tarif(int age, char situ){
    if (age < 18) return 0;
    else if((situ == 'e' && age < 25) || (situ == 'd') || (age >= 65)) return 8;
    else return 10;
}

int main() {
  int age;
  char situation;
  
  /* Les deux instructions suivantes permettent de saisir la valeur des variables
  age et situation. Vous ne devez pas les modifier. */
  scanf("%c",&situation);
  scanf("%d",&age);
  printf("age : %d, situation : %c\n",age,situation);
  int tar = tarif(age, situation);
  if (tar == 0) printf("Entree gratuite\n");
  if (tar == 1) printf("Tarif reduit : 8 euros\n");
  if (tar == 2) printf("Tarif normal : 12 euros\n");
  return 0;
}