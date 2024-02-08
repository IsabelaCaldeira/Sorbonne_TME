#include <cini.h>

void carre(int len, int coord){
    int i;
    for (i = 0; i <= len; i++){
        CINI_draw_pixel(i + coord, coord, "blue"); 
        CINI_draw_pixel(i + coord,coord + len, "green"); 
        CINI_draw_pixel(coord, i + coord, "red"); 
        CINI_draw_pixel(len + coord , i + coord, "white"); 
    }
    i = 0;    
}

void carre_remontant(int len, int coord){   
    int i;
    for(i = 0; coord+i>=0; i-=20){
        carre(len, coord + i);
    }
}

int main(){

    CINI_open_window(500, 500, "Honey");
    carre_remontant(100, 200);
    CINI_loop();
    return 0;
}