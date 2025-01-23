#include <stdio.h>
#include <math.h> 

/*Question 1*/
int discriminant(int a, int b, int c){
    return (b*b) -(4*a*c);
}

/*Question 2*/
int afficheRacines(int a, int b, int c){
    int d = discriminant(a,b,c);
    if (d < 0){
        printf("Il n'a pas de racine réelle");
    } else {
        if (d == 0){
            float x = (-b/(2.0*a));
            printf( "Il y a une racine double égale: %f", x);
        } else {
            float x1 = (-b - sqrt(d))/2*a;
            float x2 = (-b + sqrt(d))/2*a;
            printf("Il y a deux racines: %f et %f", x1, x2);
        }
    }
    return 0;
}

/*Question */
int main(){
    printf("%c \n", afficheRacines(1,2,-4));
    return 0;
}