#include<stdlib.h>
#include<stdio.h>

int main(int argc, char const *argv[])
{
	int i, ret;

	if (argc < 2) {
		printf("Usage : mon_test <un_entier>\n");
		exit(-1);
	}

	printf("Il %s pair\n", atoi(argv[1]) % 2 ? "n'est pas" : "est");

	return 0;
}

