public class TestVillageois {
    public static void main(String[] args) {
        Villageois prem= new Villageois("Chris");
        Villageois sec= new Villageois("Victor");
        Villageois trois= new Villageois("Clara");
        Villageois quatr= new Villageois("Lara");
        System.out.println((prem.toString()));
        System.out.println((sec.toString()));
        System.out.println((trois.toString()));
        System.out.println((quatr.toString()));
        System.out.println(prem.getNom());
        System.out.println(prem.getPoids());
        System.out.println(prem.getMalade());
        double pTot=prem.poidsSouleve()+sec.poidsSouleve()+trois.poidsSouleve()+quatr.poidsSouleve();
        if (pTot>150.00){
        	System.out.println("Les 4 villageois ont pu soulever le rocher");
        }
        else {
        	System.out.println("Les 4 villageois n'ont pas pu soulever le rocher");
        }
    }
}

