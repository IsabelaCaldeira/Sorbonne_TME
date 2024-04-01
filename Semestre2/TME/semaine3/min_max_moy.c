#include <stdio.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define VAL1 -2
#define VAL2 7
#define VAL3 5
#define VAL4 9

void min_max(int val, int *min, int *max)
{
  if (val < *min)
  {
    *min = val;
  }
  if (val > *max)
  {
    *max = val;
  }
}

void afficher_min_max(int min, int max)
{
  printf("La plus grande des 3 valeurs est %d, la plus petite %d.\n", max, min);
}

void stats(int v1, int v2, int v3, int v4, int *min, int *max, float *moy)
{
  float count = 0.0;
  float somme = 0.0;

  if (v1 <= 0)
  {
    *min = *max = *moy = -1;
    return;
  }

  *min = *max = v1;
  somme += v1;
  count++;

  if (v2 > 0)
  {
    min_max(v2, min, max);
    somme += v2;
    count++;
  }
  else
  {
    *moy = somme / count;
    return;
  }

  if (v3 > 0)
  {
    min_max(v3, min, max);
    somme += v3;
    count++;
  }
  else
  {
    *moy = somme / count;
    return;
  }

  if (v4 > 0)
  {
    min_max(v4, min, max);
    somme += v4;
    count++;
  }

  *moy = somme / count;
}

void afficher_resultat(float moyenne, int min, int max)
{
  printf("max = %d, min = %d, moy = %.2f\n", max, min, moyenne);
}

int main()
{
  int min = 3, max = 8;
  int a, b, c, d;
  float moy;

  printf("min = 3, max  = 8. ");
  printf("Saisissez une valeur entiere :\n");
  scanf("%d", &a);

  min_max(a, &min, &max);
  afficher_min_max(min, max);

  printf("Saisissez trois autres valeurs entieres :\n");
  scanf("%d", &b);
  scanf("%d", &c);
  scanf("%d", &d);

  stats(a, b, c, d, &min, &max, &moy);
  afficher_resultat(moy, min, max);
  return 0;
}