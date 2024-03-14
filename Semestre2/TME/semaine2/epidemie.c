#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

int jours(int contaminees, int population, float pourcentage){
    int jours = 1;
    int compte_pop = 1 + contaminees;
    
    while (compte_pop < ((population*pourcentage)/100)) {
        compte_pop = compte_pop + contaminees * compte_pop;
        jours = jours + 1;
        }
    return jours;
}

int main()
{
    {
        int pop = 10000;
        int x = 5;
        float pourcentage = 100.00;
        printf("pop=%d, vitesse=%d, pourcentage=%.2f, nbjours=%d\n", pop, x, pourcentage, jours(x, pop, pourcentage));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        float pourcentage = 50.00;
        printf("pop=%d, vitesse=%d, pourcentage=%.2f, nbjours=%d\n", pop, x, pourcentage, jours(x, pop, pourcentage));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        float pourcentage = 25.00;
        printf("pop=%d, vitesse=%d, pourcentage=%.2f, nbjours=%d\n", pop, x, pourcentage, jours(x, pop, pourcentage));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        float pourcentage = 10.00;
        printf("pop=%d, vitesse=%d, pourcentage=%.2f, nbjours=%d\n", pop, x, pourcentage, jours(x, pop, pourcentage));
        ;
    }
    return 0;
}