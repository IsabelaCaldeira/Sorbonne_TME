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
     printf("%d\n",est_deb("alpha","alphabet"));;
    }
     printf("%s\n", SEPARATOR);   {
     printf("%d\n",est_deb("alpaga","alphabet"));;
    }
     printf("%s\n", SEPARATOR);   {
     printf("%d\n",est_deb("aaaaaaaaa","aaaaaaaaa"));;
    }
     printf("%s\n", SEPARATOR);   {
     printf("%d\n",est_deb("aaaaaaaaa","aaaaaaaab"));;
    }
     printf("%s\n", SEPARATOR);   {
     printf("%d\n",est_deb("","aaaaaaaaa"));;
    }
         return 0;
 }
 