import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String cmd = "";

        System.out.println("Labirinto Infinito");
        while (!cmd.equals("S"))
        {
            System.out.println("Bem-vindo ao Labirinto");
            System.out.println("1 > Direita");
            System.out.println("2 > Esquerda");
            System.out.println("3 > Frente");
            cmd = scan.next();

            if (cmd.equals("1"))
            {
                System.out.println("Seguiste o caminho a direita");
                System.out.println("Caiste num buraco, estas preso para sempre.");
                break;
            }
            else if (cmd.equals("2"))
            {
                System.out.println("Seguiste o caminho a esquerda");
                System.out.println("Estas livre para prosseguir");
                System.out.println("1 > Direita");
                System.out.println("2 > Esquerda");
                cmd = scan.next();

                if (cmd.equals("1"))
                {
                    System.out.println("Parabens! Encontraste a saida");
                    break;
                }

                if (cmd.equals("2"))
                {
                    System.out.println("Perdeste");
                    break;
                }
            }
            else if (cmd.equals("3"))
            {
                System.out.println("Foste devorado pelo o Lorax.");
                System.out.println("Perdeste!");
                break;
            }


        }

        }
}
