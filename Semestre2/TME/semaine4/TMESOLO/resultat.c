#include <stdio.h>

int resultat(float note1, float note2){
    if ((note1 >= 10) && (note2 >= 10)) return 3;
    else{
        if(((note1 >= 8) && (note2 >= 8)) && (((note1 + note2)/2 )>= 10)) return 2;
        else if(((note1 + note2)/2)>= 10) return 1;
        else return 0;
    }
}
 
int main() {
    float note1, note2;
  
    /* Les deux instructions suivantes permettent de saisir la valeur de variables note1 et note/
    Vous ne devez pas les modifier */
    scanf("%f",&note1);
    scanf("%f",&note2);
    printf("notes : %.2f, %.2f\n",note1,note2);
 
  
    if (resultat(note1, note2) == 3)  printf("VALIDE\n");
    if (resultat(note1, note2) == 2)  printf("COMPENSE\n");
    if (resultat(note1, note2) == 1 )printf("RATTRAPAGE\n");
    if (resultat(note1, note2) == 0)  printf("AJOURNE\n");
    return 0;
}