#include <stdio.h>
#include <assert.h>

int signeProduit(int m, int n){
    if ((m == 0) || (n == 0)){
        return 0;
    } else {
        if ((m < 0) && (n < 0)) return 1;
        if ((m < 0) || (n < 0)){
            return -1;
        } else {
            return 1;
        }
    }
}

int main(){
    assert(signeProduit(3,3) == 1);
    assert(signeProduit(-1,-2) == 1);
    assert(signeProduit(3,0) == 0);
    return 0;
}