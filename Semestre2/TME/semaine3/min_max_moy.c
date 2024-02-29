#include <stdio.h>

#define MIN(a,b) ((a)<(b) ? (a):(b))
#define MAX(a,b) ((a)>(b) ? (a):(b))
#define VAL1 -2
#define VAL2 7
#define VAL3 5
#define VAL4 9


void min_max(int val, int *min, int *max) {
    printf("Ici c'est le val max et min:%d, %d, %d\n", val, *min, *max);
    if(*min>val) *min = val;
    if(*max<val) *max = val;
}

void stats (int v1, int v2, int v3, int v4, int *min, int *max, float *moy){
  
  if(v1<=0) *max = *min = *moy = -1;
  else{
    float count = 0.0;
    float somme = 0.0;

    min_max(v1, min, max);
    somme += v1;
    count ++;
  
    if(v2>0){
      min_max(v2, min, max);
      somme += v2;
      count ++;  

      if(v3>0){
        min_max(v3,min, max);
        somme += v3;
        count ++;
      
        if(v4>0){
          min_max(v4, min, max);
          somme += v4;
          count ++;
        }
      }
    }   
    *moy = somme/count;
  }
}
/*
void afficher_resultat(float moyenne, int min, int max) {
  printf("max = %d, min = %d, moy = %.2f\n",max,min,moyenne);
}
*/
int main() {
  float moy;
  int min, max;

  /* vous devrez bien sur modifier les parametres d'appel de la fonction stats une fois cette derniere completee */
  //stats();
  printf("Entrez deux nombres:\n");
  scanf("%d", &min);
  scanf("%d", &max);
  scanf("%f", &moy);
  stats(VAL1,VAL2,VAL3,VAL4, &min, &max, &moy);
  printf("Ici c'est le max: %d\n", max);
  printf("Ici c'est le min: %d\n", min);
  printf("Ici c'est le moy: %.2f\n", moy);

  /* vous devrez bien sur modifier les parametres d'appel de la fonction afficher_resultat */
  //afficher_resultat(0.0,0,0);

  return 0;
}