
#include <stdio.h> 

/* Ce programme affiche tous les nombres premiers inferieurs ou egaux a max */


void affichePremiers(int borne, int val) {
  int i, j, nbDiv;
  
  for (j=2; j <= borne; j++) { 
     nbDiv = 0;
     for (i=1; i <= j/2; i++) {
        if (j%i == 0){
           nbDiv = nbDiv + 1;
        } 
     }
     if (nbDiv == 1){ 
        printf("%d ",j);
     } 
  }
  printf("\n");

}

int main() {
    int max;
  
    /* L'instruction suivante est correcte, elle permet de saisir
    la valeur de max */
    scanf("%d",&max);  
   
    affichePremiers(max,3);
    return 0; 
}
