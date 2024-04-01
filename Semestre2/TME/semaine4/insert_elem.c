int insertElt(int tab[], int el, int *nb, int taille)
{
    int indice = indiceInsert(tab, el, *nb, taille);

    if (indice == -1 || *nb == taille)
    {
        return 0;
    }

    for (int i = *nb; i > indice; i--)
    {
        tab[i] = tab[i - 1];
    }

    tab[indice] = el;
    (*nb)++;

    return 1;
}

void affiche_tab(int tab[], int taille)
{
    int i;
    for (i = 0; i < taille; i++)
    {
        printf("%d  ", tab[i]);
    }
    printf("\n");
}

int main()
{
    int tab[6];
    int i, inser_OK, nbEl, val;

    scanf("%d", &nbEl);
    for (i = 0; i < nbEl; i++)
    {
        scanf("%d", tab + i);
    }

    scanf("%d", &val);
    inser_OK = insertElt(tab, val, &nbEl, 6);
    printf("insertion OK ? %d\n", inser_OK);
    affiche_tab(tab, nbEl);
    return 0;
}