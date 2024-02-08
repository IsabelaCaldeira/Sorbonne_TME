#include <cini.h>
 
int main() {
 
  CINI_open_window(400, 300, "test");
  
  CINI_draw_pixel(199, 200, "white");   /* affiche pt coord x=199, y=200*/
  CINI_draw_pixel(200, 200, "white");   /* affiche pt coord x=200, y=200*/
  CINI_draw_pixel(201, 200, "white");   /* affiche pt coord x=201, y=200*/

  CINI_loop();
  return 0;
}