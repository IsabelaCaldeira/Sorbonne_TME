#include <cini.h>

void diagonale(int x){
    CINI_open_window(300, 300, "Shine");
    
    int i;
    for (i = 0; i <= x; i++){
        CINI_draw_pixel(i, i, "purple"); 
    }
    CINI_loop();
}

int main(){
    diagonale(500);
    return 0;
}