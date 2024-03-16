#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

float pourcentage(int personnes_contaminees_par_jour, int population_totale, int jours) {
    int personnes_contaminees = 1; 
    float total_contamines = 1 + personnes_contaminees;
    
    for (int i = 0; i < jours; i++) {
        total_contamines += personnes_contaminees_par_jour * total_contamines;
    }
    
    float pourcentage_contamines =( (total_contamines / population_totale) * 100/2);
    
    if (pourcentage_contamines > 100) {
        pourcentage_contamines = 100;
    }
    
    return pourcentage_contamines;
}

int main()
{
    {
        int pop = 10000;
        int x = 5;
        int jours = 2;
        printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n", pop, x, jours, pourcentage(x, pop, jours));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        int jours = 3;
        printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n", pop, x, jours, pourcentage(x, pop, jours));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        int jours = 4;
        printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n", pop, x, jours, pourcentage(x, pop, jours));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        int jours = 5;
        printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n", pop, x, jours, pourcentage(x, pop, jours));
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        int pop = 10000;
        int x = 5;
        int jours = 6;
        printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n", pop, x, jours, pourcentage(x, pop, jours));
        ;
    }
    return 0;
}