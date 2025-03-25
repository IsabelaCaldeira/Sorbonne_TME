int indiceInsert(int tab[], int el, int nb, int taille){
    if (nb >= taille || tab[nb - 1] == el) return -1;

    for(int i = 0; i < nb; i++){
        if(tab[i] == el) return -1;
        else if(tab[i] > el) return i;
    }
    return nb;
}