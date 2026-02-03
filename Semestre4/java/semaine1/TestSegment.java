public class TestSegment {
    public static void main(String[] args) {
        Segment s= new Segment(6,8);
        Segment p= new Segment(12,5);
        int ls=s.longueur();
        int lp=p.longueur();

        if (ls>lp){
            System.out.println("Le premier "+s.toString()+ " est le plus long");
        }
        else {
             System.out.println("Le deuxieme "+p.toString()+ " est le plus long");
        }


    }
}

