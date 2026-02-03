public class TestLettre{
	public static void main(String[] args){
		for (char i='a';i<='z';i++){
			Lettre c= new Lettre(i);
			System.out.println(c.getCodeAscii());
		}
		int cpt=0;
		for (char i='a';i<='z';i++){
			Lettre l= new Lettre(i);
			System.out.print(l.getCarac()+" ");
			cpt++;
			if (cpt%5==0){
				System.out.println();
			}
		}
	}
}
