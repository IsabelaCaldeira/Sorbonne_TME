#include <stdio.h>

int valeur() {
  int n;
  scanf("%d",&n);
  return n;
}

int compteVal(int ref, int nb) {
    int val, compteur = 0;
    for (int i = 0; i < nb; i ++){
        val = valeur();
        if (val == ref) compteur ++;
    }

    return compteur;

}

int main(){
    int ref, nb;
    
    /* Les deux instructions suivantes permettent de saisir la valeur des variables ref et nb.
    Vous ne devez pas les modifier. */
    scanf("%d",&ref);
    scanf("%d",&nb);
    printf("Reference : %d, nb valeurs : %d\n",ref,nb);
    
    
	printf("la valeur %d apparait %d fois\n", ref, compteVal(ref, nb));
	
	return 0;
}
