#include <stdio.h>

int compteDiv( int v1, int v2, int min){
    int res = 0;
    for(int i = min; i <= v1; i++){
        if(v1%i == 0 && v2%i == 0) res ++;
    }
    return res;
}

int main()
{
    int v1, v2, min;

    /* Les trois instructions suivantes permettent de saisir la valeur des variables v1, v2
    et min. Vous ne devez pas les modifier. */
    scanf("%d", &v1);
    scanf("%d", &v2);
    scanf("%d", &min);
    printf("v1 : %d, v2 : %d, min : %d\n", v1, v2, min);

    printf("%d\n", compteDiv(v1,v2,min));
    return 0;
}