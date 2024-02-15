#include <stdio.h>

void echange(int *a, int *b){
    int c = *a;
    *a = *b;
    *b = c;
    printf("a = %d, b = %d\n", *a, *b);
}

void tri(int *a, int *b){
    if (*a > *b) echange(a, b);
}

void tri_3(int *a, int *b, int *c){
    tri(a, b);
    tri(a, c);
    tri(b, c);
    printf("a = %d, b = %d, c = %d\n", *a, *b, *c);
}

int main(){
    int a = 3;
    int b = 5;
    int c = 4;

    tri_3(&a, &b, &c);
    return 0;
}