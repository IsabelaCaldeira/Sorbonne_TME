#include <stdio.h>

int main(void) {
    int n;
    printf("Entrez n (0..128) : ");
    if (scanf("%d", &n) != 1 || n < 0 || n > 128) {
        fprintf(stderr, "Valeur invalide. Entrez un entier entre 0 et 128.\n");
        return 1;
    }

    float u = 1.0f; /* u0 */
    for (int i = 0; i <= n; ++i) {
        printf("u[%d] = %f\n", i, u);
        u = 2.0f * u + 1.0f;
    }

    return 0;
}
