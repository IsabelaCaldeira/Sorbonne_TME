#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NB_VALEURS 50
#define VMIN -20
#define VMAX 20

int valeur_aleatoire(int min, int max)
{  
    return rand() % (max - min) + min;
}

int pos_neg_zero(int fois, int min, int max){
    int post = 0;
    int neg = 0;
    int zero = 0;

    int i;
    for(i=1;i<=fois;i++){
        int a = valeur_aleatoire(min, max);
        if (a>0) post++;
        if (a<0) neg ++;
        if (a==0) zero++;
        printf("Fois = %d, Positives = %d, Negative = %d, Zeros = %d\n",i,post,neg,zero);
    }

    return 0;
}

int main(){
  
    /* initialisation du générateur de nombres aléatoires */
    srand(time(NULL));
    
    pos_neg_zero(NB_VALEURS, VMIN, VMAX);
    
    return 0;
}