#include <stdio.h>
#include <math.h>

int discriminant(int a, int b, int c) {
    return b * b - 4 * a * c;
}

int nb_racines_delta(int a, int b, int c) {
    int delta = discriminant(a, b, c);
    if (delta > 0) {
        return 2;
    } else if (delta == 0) {
        return 1;
    } else {
        return 0;
    }
}

int racines(int a, int b, int c, float* rac1, float* rac2) {
    if (a == 0) {
        printf("Coefficient a cannot be 0.\n");
        return 0;
    }

    int delta = discriminant(a, b, c);
    int nb_racines = nb_racines_delta(a, b, c);
    if (nb_racines == 2) {
        *rac1 = (-b + sqrt(delta)) / (2 * a);
        *rac2 = (-b - sqrt(delta)) / (2 * a);
    } else if (nb_racines == 1) {
        *rac1 = *rac2 = -b / (2.0 * a);
    }
    return nb_racines;
}

int main() {
    int a, b, c;
    printf("Entrez les coefficients a (!= 0) b et c du polynome :\n");
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    int nb_rac;
    float rac1, rac2;

    printf("valeur de delta : %d\n", discriminant(a, b, c));
    nb_rac = racines(a, b, c, &rac1, &rac2);
    if (nb_rac == 2) {
        printf("Le polynome a 2 racines : %.3f et %.3f\n", rac1, rac2);
    } else if (nb_rac == 1) {
        printf("Le polynome a 1 racine double : %.3f\n", rac1);
    } else {
        printf("Le polynome n'a pas de racine reelle.\n");
    }
    return 0;
}
 