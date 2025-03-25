#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

//Question 1 
int jours(int contaminees, int population, float pourcentage){
    int jours = 1;
    int compte_population = 1 + contaminees;

    while (compte_population < ((population*pourcentage)/100)) {
        compte_population = compte_population + contaminees * compte_population;
        jours = jours + 1;
    }
    return jours;
}

//Question 2
float pourcentage(int personnes_contaminees_jours, int population_totale, int jours){
    int personnes_contaminees = 1;
    float total_contaminees = 1 + personnes_contaminees; 

    for(int i = 0; i < jours; i++){
        total_contaminees += personnes_contaminees_jours * total_contaminees;
    }

    float pourcentage_contaminees = ((total_contaminees / population_totale) * 100/2);

    if (pourcentage_contaminees > 100){
        pourcentage_contaminees = 100;
    }

    return pourcentage_contaminees;

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