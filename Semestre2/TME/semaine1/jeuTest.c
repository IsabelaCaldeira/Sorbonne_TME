#include <stdio.h>

int alternative(int n1, int n2, int n3){
    int res;

    if (n1 > 8) {
        res = 3;
    } else {
        if (n3 == 20){
            res = 2;
        } else {
            if ((n2 >= 10) && (n3 >= 10)) {
                res = 1;
            } else {
                res = 0;
            }
        }
    }

    return res;
}

int main() {

    // n1 > 8
    printf("%d \n", alternative(9,1,1));
    // n3 == 20
    printf("%d \n",alternative(8,1,20));
    // (n2 >= 10) && (n3 >= 10)
    printf("%d \n",alternative(7,10,10));
    // != (n2 >= 10) && (n3 >= 10)
    printf("%d \n",alternative(7,10,9));

    return 0; 
    
}