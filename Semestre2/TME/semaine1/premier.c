#include <stdio.h>
#define MAX 5

int premier(int n){
    for (int i = 2; i < n;i++){
        if (n%i== 0){
            return 0;
        }
    }
    return 1;
}

int affiche(int n_max){
    for (int i =2; i <= n_max; i++){
        if(premier(i) == 1){
            printf("%d ", i);
        }
    }
    printf(" \n");
    return 0;
}

int main(){
    affiche(MAX);
    return 0;
}

