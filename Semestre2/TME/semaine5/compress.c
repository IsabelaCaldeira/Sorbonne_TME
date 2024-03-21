#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

void affiche_tab(int tab[]){
  int i=0;

  while (tab[i] != -1){
    printf("%d ",tab[i]);
    i++;
  }
  printf("\n");
}
void compress_tab(int tab_brut[], int tab_compress[]) {
	int compteur = 1;
	int i = 0, j = 0;
	
	while (tab_brut[i] != -1){
		if (tab_brut[i] == tab_brut[i + 1]) compteur++;
		else{
			if (compteur == 1) tab_compress[j++] = tab_brut[i];
			else{
				tab_compress[j++] = compteur;
				tab_compress[j++] = tab_brut[i];
				compteur = 1;
			}
		}
		i++;
	}
	tab_compress[j++] = -1;
}

int main() {
   {
    int tab1[]={0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,-1};
int tab2[20];
compress_tab(tab1,tab2);
affiche_tab(tab2);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[]={0,0,0,0,0,0,-1};
int tab2[20];
compress_tab(tab1,tab2);
affiche_tab(tab2);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[]={1,1,1,1,1,1,1,1,-1};
int tab2[20];
compress_tab(tab1,tab2);
affiche_tab(tab2);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[]={0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,-1};
int tab2[20];
compress_tab(tab1,tab2);
affiche_tab(tab2);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[]={1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,-1};
int tab2[20];
compress_tab(tab1,tab2);
affiche_tab(tab2);;
   }
        return 0;
}