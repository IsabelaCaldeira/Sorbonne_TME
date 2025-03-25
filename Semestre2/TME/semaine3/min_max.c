#include <stdio.h>

void min_max(int a, int *min, int *max) {
    if(a < *min) *min = a;
    if(a > *max) *max = a;
}

void stats (int a, int b, int c, int d, int *min, int *max, float *moy) {
    if (a <= 0) *min = *max = *moy = -1;
    else if ((a > 0) && (b > 0) && (c <= 0)){
        *min = *max = a;
        min_max(a, min, max);
        min_max(b, min, max);
        *moy = (a + b) / 2.0;
    }
    else{
        *min = *max = a;
        min_max(a, min, max);
        min_max(b, min, max);
        min_max(c, min, max);
        min_max(d, min, max);
        *moy = (a + b + c + d) / 4.0;
    }

}

void afficher_resultat(float moyenne, int min, int max) {
  printf("max = %d, min = %d, moy = %.2f\n", max, min, moyenne);
}

int main() {
   int min = 3, max = 8; 
   int a, b, c, d;
   float moy;
  
   printf("min = %d, max = %d. Saisissez une valeur entiere :\n", min, max);  
   scanf("%d", &a);  
   min_max(a, &min, &max);
   printf("La plus grande des 3 valeurs est %d, la plus petite %d.\n", max, min);  
   
   printf("Saisissez trois autres valeurs entieres :\n");  
   scanf("%d", &b);  
   scanf("%d", &c);  
   scanf("%d", &d);  
   
   stats(a, b, c, d, &min, &max, &moy);
   afficher_resultat(moy, min, max);
   return 0;
}