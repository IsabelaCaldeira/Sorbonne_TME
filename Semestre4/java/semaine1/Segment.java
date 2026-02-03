public class Segment {
    private int x,y;
    public Segment(int extX,int extY){
        x=extX;
        y=extY;
    }
    public int longueur(){
        if (x<y){
            return y-x;
        }
        return x-y;
    }
    public String toString(){
        return "Segment ["+x+","+y+"]";
    }
}

