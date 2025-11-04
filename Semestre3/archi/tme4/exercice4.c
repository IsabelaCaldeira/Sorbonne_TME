int tab[] = {4, 23, 12, 3, 8, 1};

int s, p;

void main(){
    s = tab[3];
    p = tab[4];

    tab[0] = s + 1;
    tab[1] = p + 1;
    tab[2] = tab[5];

    exit();
}