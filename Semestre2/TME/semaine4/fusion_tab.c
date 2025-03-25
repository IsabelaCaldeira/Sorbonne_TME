#include <stdio.h>
#include <stdlib.h>

int* fusion(int tab1[], int taille1, int tab2[], int taille2){
    int taille = taille1 + taille2;
    int tab[taille];

    int i, j, k;
    if(taille1 <= taille2){
        for(i = 0; i < taille1; i++){
            for(j = 0; j < taille2; j++){
                for(k = 0; k < taille; k++){
                    if(tab1[i] < tab2[j]) tab[k] = tab1[i];
                    else tab[k] = tab2[i];
                }
            }
            if(j == taille2 && i != taille1 -1){
                
            }
        }
    }
    else{
        for(i = 0; i < taille2; i++){
            for(j = 0; j < taille1; j++){
                for(k = 0; k < taille; k++){
                    if(tab2[j] < tab1[i]) tab[k] = tab2[j];
                    else tab[k] = tab1[i];
                }
            }
        }
    }
    return tab; 
}

int main(){
    int tab1[20];
    int tab2[20];
    int i;
    int nb1, nb2;
    int* tab;

    scanf("%d", &nb1);
    scanf("%d", &nb2);
    for (i = 0; i < nb1; i++){
        scanf("%d", tab1 + i);
    }
    for (i = 0; i < nb2; i++){
        scanf("%d", tab2 + i);
    }

    tab = fusion(tab1, nb1, tab2, nb2);
    for (i = 0; i < nb1 + nb2; i++){
        printf("%d  ", tab[i]);
    }
    printf("\n");
    free(tab);
    return 0;
}