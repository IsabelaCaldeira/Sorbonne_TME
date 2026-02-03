public class Villageois {
    private String nom;
    private double poids;
    private boolean malade;
    public Villageois(String nomVillageois){
        nom=nomVillageois;
        poids=Math.random()*100+50;
        malade=Math.random() < 0.20;
    }
    public String toString(){
        String mal;
        if (malade){
            mal="oui";
        }
        else {
            mal="non";
        }
        return "villageois: "+nom+ " , "+ "poids: "+ String.format("%.2f kg",poids)+" , "+ "malade: " + mal + " peut soulever "+String.format("%.2f kg",poidsSouleve());
    }
    public String getNom(){
    	return nom;
    }
    public double getPoids(){
    	return  poids;
    }
    public boolean getMalade(){
    	return malade;
    }
    public double poidsSouleve(){
    	if (malade){
    		return poids/4;
    	}
    	else {
    		return poids/3;
    	}
    }
}

