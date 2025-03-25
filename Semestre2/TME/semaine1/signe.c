#include <stdio.h>
#include <assert.h>

//Question 1 
int signeProduit(int m, int n){
    if ((m == 0) || (n == 0)){
        return 0;
    } else {
        if ((m < 0) && (n < 0)) return 1;
        if ((m < 0) || (n < 0)) return -1;
        return 1;
    }
}

//Question 2 
int main(){
    assert(signeProduit(3,-3) == -1);
    assert(signeProduit(-1,-2) == 1);
    assert(signeProduit(3,0) == 0);
    return 0;
}