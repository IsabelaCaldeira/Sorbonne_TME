#include <stdio.h>

void Affiche_rec(float tab[], int n){
    if (n>0){
        Affiche_rec(tab+1, n-1);
        printf("%f ", tab[0]);
    }
}

int main(){
    float t[5]={1, 2, 3, 4, 5};
    Affiche_rec(t, 5);
    printf("\n");
      return 0;
}