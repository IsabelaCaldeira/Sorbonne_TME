#include <stdio.h>

int indiceInsert(int tab[], int el, int nb, int taille)
{
    if (nb >= taille || el == tab[nb - 1])
    {
        return -1;
    }
    int i;
    for (i = 0; i < nb; i++)
    {
        if (tab[i] == el)
        {
            return -1;
        }
        if (tab[i] > el)
        {
            return i;
        }
    }

    return nb;
}

int main()
{
    int tab1[5] = {3, 5, 7, 9};
    printf("%d\n", indiceInsert(tab1, 10, 4, 5));
    return 0;
}