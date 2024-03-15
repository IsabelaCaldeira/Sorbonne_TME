#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

int est_deb(char *chaine1, char *chaine2){
    if(*chaine1 == '\0') return 1;
    if(*chaine2 == '\0') return 0;
    if(*chaine1 != *chaine2) return 0;

    return est_deb(chaine1 + 1, chaine2 + 1);
}

int est_incluse(char *chaine1, char *chaine2){
    if(*chaine1 == '\0') return 1;
    if(*chaine2 == '\0') return 0;
    if(*chaine1 != *chaine2) return est_incluse(chaine1, chaine2 + 1);

    return est_incluse(chaine1 + 1, chaine2 + 1);
}

int main() {
   {
    printf("%d\n",est_incluse("alpha","alphabet"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("%d\n",est_incluse("alpaga","alphabet"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("%d\n",est_incluse("abe","alphabet"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("%d\n",est_incluse("beta","alphabet"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("%d\n",est_incluse("","alphabet"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("%d\n",est_incluse("bet","alphabet"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("%d\n",est_incluse("ber","alphabet"));;
   }
        return 0;
}