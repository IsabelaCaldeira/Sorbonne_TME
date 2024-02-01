#include <stdio.h>
#include <math.h> 

int discriminant(int a, int b, int c){
    int d = (b*b) -(4*a*c);
    return d;
}

int afficheRacines(int a, int b, int c){
    int d = discriminant(a,b,c);
    if (d < 0){
        printf("Il n'a pas de racine réelle");
    } else {
        if (d == 0){
            printf( "Il y a une racine double égale");
        } else {
            printf("Il y a deux racines");
        }
    }
    return 0;
}

int main(){
    printf("%c \n", afficheRacines(1,2,-4));
    return 0;
}