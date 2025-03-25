#include <stdio.h>
#define TFAMILLE 57.8
#define TADULTE 22.7
#define TENFANT 10.75

float prixEntree(int nb_a, int nb_e){
	int adu = nb_a;
	int enf = nb_e;
	float total = 0;
	float totalSansFamille = 0;
	
	while (adu >= 2 && enf >= 3) {
		total += TFAMILLE;
		adu -= 2;
		enf -= 3;
	}
	
	totalSansFamille = adu * TADULTE + enf * TENFANT;
	if ((adu <= 2 && enf <= 3) && totalSansFamille < TFAMILLE) total += totalSansFamille;
	else {
		if ((adu <= 2 && enf <= 3) && totalSansFamille > TFAMILLE) total += TFAMILLE;
	}
	if (adu > 2 || enf > 3) total += totalSansFamille;
	
	return total;
}

int main(){
	int nb_a, nb_e;
	
	scanf("%d", &nb_a);
	scanf("%d", &nb_e);
	printf("(%d adultes, %d enfants) = %.2f livres\n", nb_a, nb_e, prixEntree(nb_a,nb_e));
	
	return 0;
}