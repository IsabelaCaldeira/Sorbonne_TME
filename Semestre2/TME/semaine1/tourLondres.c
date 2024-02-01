#include <stdio.h>
#include <assert.h>

float prixEntree(int adl, int enf){
    float res;
    if((adl == 2) && (enf < 4)){
        printf("I am inside the if of prixentree\n");
        res = 57.80;
        printf("%f", res);
    } else {
        res =  adl * 22.7 + enf * 10.75;
    }
    printf("%f \n", res);
    return res;
}

int main(){
    printf("%f", prixEntree(2,3));
    return 0;
}