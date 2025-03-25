#include <stdio.h>

#define NB_VALEURS 6

void pos_neg_zero(int val, int *nb_negative, int *nb_positive, int *nb_zero){
    if (val < 0) (*nb_negative)++;
    else if(val > 0) (*nb_positive)++;
    else (*nb_zero)++;
}


int main(){
   int i, val, nb_negative = 0, nb_positive = 0, nb_zero = 0;
   
   printf("Saisissez une suite de %d valeurs\n", NB_VALEURS);
   for (i = 0; i < NB_VALEURS; i++) {
      scanf("%d", &val);
      pos_neg_zero(val, &nb_negative, &nb_positive, &nb_zero);
   }
  
   printf("%d valeurs negatives, %d valeurs positives, %d valeurs nulles.\n", nb_negative, nb_positive, nb_zero);  
   return 0;
}