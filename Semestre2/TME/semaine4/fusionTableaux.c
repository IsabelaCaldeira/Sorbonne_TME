#include <stdio.h>
#include <stdlib.h>

int* fusion(int tab1[], int taille1, int tab2[], int taille2){
    int* new_tab = (int*)malloc((taille1 + taille2)* sizeof(int));
    int i1, i2 = 0, i = 0;

    while(i1 < taille1 && taille2 > i2){
        if(tab1[i1] <= tab2[i2]){
            new_tab[i] = tab1[i1];
            i1++;
        }else{
            new_tab[i] = tab2[i2];
            i2++;
        }
        i++;
    }

    while(i1 < taille1){
        new_tab[i] = tab1[i1];
        i++;
        i1++;
    }

    while(i2 < taille2){
        new_tab[i] = tab2[i2];
        i++;
        i2++;
    }

    return new_tab;
}

int main()
{
    int tab1[20];
    int tab2[20];
    int i;
    int nb1, nb2;
    int* tab;

    scanf("%d", &nb1);
    scanf("%d", &nb2);
    for (i = 0; i < nb1; i++)
    {
        scanf("%d", tab1 + i);
    }
    for (i = 0; i < nb2; i++)
    {
        scanf("%d", tab2 + i);
    }

    tab = fusion(tab1, nb1, tab2, nb2);
    for (i = 0; i < nb1 + nb2; i++)
    {
        printf("%d  ", tab[i]);
    }
    printf("\n");
    free(tab);
    return 0;
}