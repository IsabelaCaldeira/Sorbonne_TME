#include <stdio.h>
#include <math.h>

int discriminant(int a, int b, int c) {
    return b * b - 4 * a * c;
}

int nb_racines_delta(int a, int b, int c) {
   int dis = discriminant(a,b,c);
   if (dis > 0) return 2;
   else if (dis == 0) return 1;
   else return 0;

}

int racines(int a, int b, int c, float *rac1, float *rac2){
   int nb_rac = nb_racines_delta(a,b,c); 
   int dis = discriminant(a,b,c);

   if (nb_rac == 2){
      *rac1 = (-b + sqrt(dis))/(2*a);
      *rac2 = (-b - sqrt(dis))/(2*a);
   } 

   if (nb_rac == 1) *rac1 = -b/(2.0*a);

   return nb_rac;
}

int main(){
   int a, b, c;
   int nb_rac; 
   float rac1, rac2;
  
   printf("Entrez les coefficients a (!= 0) b et c du polynome :\n");
   scanf("%d", &a);
   scanf("%d", &b);
   scanf("%d", &c);
  
   printf("valeur de delta : %d\n", discriminant(a,b,c));
   nb_rac = racines(a,b,c, &rac1, &rac2);
   if (nb_rac == 2){
      printf("Le polynome a 2 racines : %.3f et %.3f\n", rac1, rac2);
   }
   if (nb_rac == 1){
      printf("Le polynome a 1 racine double : %.3f\n", rac1);
   }
   if (nb_rac == 0){
      printf("Le polynome n'a pas de racine reelle.\n");
   }
   return 0;
}