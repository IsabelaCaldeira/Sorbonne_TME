#include <stdio.h>

int main(void) {
    /* char */
    char ca = 0;
    char prev_ca = 0;
    do {
        prev_ca = ca;
        ca++;
    } while (ca > prev_ca);
    printf("char : min = %d, max = %d\n", (int)ca, (int)prev_ca);

    /* short */
    short sa = 0;
    short prev_sa = 0;
    do {
        prev_sa = sa;
        sa++;
    } while (sa > prev_sa);
    printf("short: min = %d, max = %d\n", (int)sa, (int)prev_sa);

    /* int */
    int ia = 0;
    int prev_ia = 0;
    do {
        prev_ia = ia;
        ia++;
    } while (ia > prev_ia);
    printf("int  : min = %d, max = %d\n", prev_ia, ia);

    /* unsigned char */
    unsigned char uca = 0;
    unsigned char prev_uca = 0;
    do {
        prev_uca = uca;
        uca++;
    } while (uca > prev_uca);
    printf("unsigned char: min = %u, max = %u\n", (unsigned int)0, (unsigned int)prev_uca);

    /* unsigned int */
    unsigned int ui = 0;
    unsigned int prev_ui = 0;
    do {
        prev_ui = ui;
        ui++;
    } while (ui > prev_ui);
    printf("unsigned int : min = %u, max = %u\n", 0u, prev_ui);

    return 0;
}