#include <stdio.h>

#define NB_VALEURS 6

void pos_neg_zero(int val, int *nb_negatives, int *nb_positives, int *nb_zero)
{
    if (val < 0)
    {
        (*nb_negatives)++;
    }
    else if (val > 0)
    {
        (*nb_positives)++;
    }
    else
    {
        (*nb_zero)++;
    }
}

int main()
{
    int i, val;
    int nb_negatives = 0, nb_positives = 0, nb_zero = 0;

    printf("Saisissez une suite de %d valeurs\n", NB_VALEURS);
    for (i = 0; i < NB_VALEURS; i++)
    {
        scanf("%d", &val);
        pos_neg_zero(val, &nb_negatives, &nb_positives, &nb_zero);
    }

    printf("%d valeurs negatives, %d valeurs positives, %d valeurs nulles.\n", nb_negatives, nb_positives, nb_zero);
    return 0;
}