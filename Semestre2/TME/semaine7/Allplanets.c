#include <stdio.h>
#define NB_PLANETES 8

typedef struct 
{
    char nom[11];
    float densite;
    float distance;
    int nbsat;
} planete;


void affichePlanete(planete p){
   printf("%s : densite = %.2f, distance soleil = %.1f, nb satellites = %d\n", p.nom, p.densite, p.distance, p.nbsat);
}

void afficheToutesPlanetes(planete systeme[], int taille){
    for(int i = 0; i < taille; i++) affichePlanete(systeme[i]);
}

void modifieDensite(planete *p, float N_densite) {
    p -> densite = N_densite;
}

int main(){
    planete systemeSolaire[NB_PLANETES] ={{"Mercure", 5.42, 58, 0}, {"Venus", 5.25, 108.2, 0}, 
        {"Terre", 5.52, 149.6,1}, {"Mars", 3.94, 227.9, 2}, {"Jupiter", 1.314, 778.3, 16},
        {"Saturne", 0.69, 1427, 17}, {"Uranus", 1.19, 2869, 15}, {"Neptune", 1.6, 4496, 2}};
    int i;
    float d;
   
    afficheToutesPlanetes(systemeSolaire, NB_PLANETES);
    printf("\n");
    scanf("%d", &i);
    scanf("%f", &d);
    /* on affecte la densite d a la planete d'indice i du tableau systemeSolaire */
    modifieDensite(&systemeSolaire[i],d);
    affichePlanete(systemeSolaire[i]);
    printf("\n");
    return 0;
}