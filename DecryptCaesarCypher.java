import java.util.Scanner;

public class DecryptCaesarCypher
{
    private static Scanner input;

    public static void main(String[] args)
    {
        input = new Scanner(System.in);
        System.out.print("Enter the message that you wish to decrypt: ");
        String message = input.nextLine();

        System.out.println("The possible original message is: ");
        for(int shift=1;shift<26;shift++)
        {
            System.out.println(shift+". "+EncryptCaesarCypher.caesarcypher(message, shift));
        }

    }

}