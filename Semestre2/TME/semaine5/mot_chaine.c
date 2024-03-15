#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

int compte_mots(char *s){
    int i;
    char temp = ' ';
    int compt = 0;
    for (i = 0; s[i] != '\0'; i++){
        if (s[i] != ' ' && temp == ' ') compt ++;
        temp = s[i];
    }
    return compt;
}


int main() {
   {
    printf("nombre de mots : %d\n",compte_mots("mot1 mot2 mot3"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("mot1  mot2    mot3"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("   mot1 mot2 mot3 mot4"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("mot1 mot2 mot3 mot4 mot5  "));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("   mot1     mot3     "));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("mot1mot2mot3"));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("   mot1mot2mot3   "));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots(""));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("    "));;
   }
    printf("%s\n", SEPARATOR);   {
    printf("nombre de mots : %d\n",compte_mots("mot motpluslong  motcourt  motencorepluslong   "));;
   }
        return 0;
}