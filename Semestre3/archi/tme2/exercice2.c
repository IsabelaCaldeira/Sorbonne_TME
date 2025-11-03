#include <stdio.h>

int main (){
    float a=10.0;
    int *ca;
    ca = (int * )&a;
    printf("codage du flottant = %x \n", *ca);
}