#include <cini.h>

void carre(int len, int coord){
    
    CINI_open_window(500, 500, "Honey");

    int i;
    for (i = 0; i <= len; i++){
        CINI_draw_pixel(i + coord, coord, "blue"); 
        CINI_draw_pixel(i + coord,coord + len, "green"); 
        CINI_draw_pixel(coord, i + coord, "red"); 
        CINI_draw_pixel(len + coord , i + coord, "white"); 
    }
    i = 0;    
    CINI_loop();
}

int main(){
    carre(100, 200);
    return 0;
}