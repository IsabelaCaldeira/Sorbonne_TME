#include <stdio.h>
#include <stdlib.h>

/*Question 1*/
int *alloue_tableau(int n){
    return (int *) malloc(n*sizeof(int));

}

void desalloue_tableau(int *T){
    free(T);
}

void remplir_tableau(int *T, int n, int V){ 
    for(int i = 0; i<n; i++){
        T[i] = (int) rand % V;   
    };
}