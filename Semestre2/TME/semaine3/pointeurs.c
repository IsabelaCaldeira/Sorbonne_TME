#include <stdio.h>

void ma_fonction(int v1, int v2) {
    int a;
    int *b = &a;

    a = v1;
    *b = a + v2;
    a = 2 * (*b);
    printf("Des valeurs: a=%d et b=%d\n",a,*b);
    printf("Des adresses: &a=%p et &b=%p\n",&a, &b);

}

int main() {
    ma_fonction(10,20);
}