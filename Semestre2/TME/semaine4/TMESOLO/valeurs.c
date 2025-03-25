#include <stdio.h>

int valeur(void){
    int n;
    scanf("%d", &n);
    return n;
}

void ma_fonction(int n, int *min, int *max){
    int val = valeur();
    *min = val; 
    *max = val;
    for(int i = 1; i < n; i++){
        val = valeur();
        if (val < *min) *min = val;
        if (val > *max) *max = val;
    }
}

int main() {
  int nb;
  int min, max;

  
  /* Instructions pemettant de saisir la valeur de la variable nb */
  scanf("%d",&nb);
    min = max = nb;

  
  /* A COMPLETER, remplacez les pointilles */
  ma_fonction(nb, &min, &max);
  
  /* A COMPLETER, remplacez les pointilles */
  afficherResultat(min, max);


  return 0;
}