int Inclus(element_t *ens1, element_t *ens2) {
    element_t *ptr1 = ens1;
    element_t *ptr2 = ens2;

    while (ptr1 != NULL) {
        if (ptr2 == NULL || ptr1->valeur < ptr2->valeur) {
            return 0;
        } else if (ptr1->valeur == ptr2->valeur && ptr1->frequence > ptr2->frequence) {
            return 0;
        }

        ptr1 = ptr1->suivant;
        ptr2 = ptr2->suivant;
    }

    return 1;
}