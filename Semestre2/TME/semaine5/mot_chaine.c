#include <stdio.h>
#include <string.h>

int compt_mots(char *s){
    int i;
    char temp = ' ';
    int compt = 0;
    for (i = 0; s[i] != '\0'; i++){
        if (s[i] != ' ' && temp == ' ') compt ++;
        temp = s[i];
    }
    return compt;
}

int main(){

    char s[100];
    scanf("%99[^\n]", s);
    int resposta = compt_mots(s);
    printf(" %d \n", resposta);

    return 0;
}