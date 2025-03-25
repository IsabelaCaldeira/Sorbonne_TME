#include <stdio.h>

struct planete
{
    char nom[10];
    float densite;
    float distance;
    int nbsat;
};

typedef struct planete planete;

/* Autre option
typedef struct{
   char nom[10];
   float densite;
   float distance;
   int nbsat;
}planete;
*/

void affichePlanete(planete p){
   printf("%s : densite = %.2f, distance soleil = %.1f, nb satellites = %d\n", p.nom, p.densite, p.distance, p.nbsat);
}

int main(){
   planete p;
   
   scanf("%s", p.nom);
   scanf("%f", &p.densite);
   scanf("%f", &p.distance);
   scanf("%d", &p.nbsat);
   affichePlanete(p);
   return 0;
}
