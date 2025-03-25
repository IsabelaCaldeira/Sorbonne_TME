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

int main() {
   {
    int tab1[20];
int tab2[]={2,0,4,1,0,3,1,2,0,1,4,0,-1};
decompress_tab(tab1,tab2);
affiche_tab(tab1);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[20];
int tab2[20]={6,0,-1};
decompress_tab(tab1,tab2);
affiche_tab(tab1);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[20];
int tab2[20]={8,1,-1};
decompress_tab(tab1,tab2);
affiche_tab(tab1);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[20];
int tab2[]={0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,-1};
decompress_tab(tab1,tab2);
affiche_tab(tab1);;
   }
    printf("%s\n", SEPARATOR);   {
    int tab1[25];
int tab2[]={1,3,0,4,1,0,3,1,3,0,1,4,0,1,-1};
decompress_tab(tab1,tab2);
affiche_tab(tab1);;
   }
        return 0;
}

void decompress_tab(int tab_brut[], int tab_compress[]) {
	int j = 0;
	for (int i = 0; tab_compress[i] != -1; i++){
		if (tab_compress[i] != 1 && tab_compress[i] != 0){
			while (tab_compress[i] != 0){
				tab_brut[j++] = tab_compress[i + 1];
				tab_compress[i]--;
				}
			i++;
		}else tab_brut[j++] = tab_compress[i];
	}
	tab_brut[j++] = -1;
}