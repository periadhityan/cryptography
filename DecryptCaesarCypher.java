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
            System.out.println(shift+". "+caesarcypher(message, shift));
        }

    }

    public static String caesarcypher(String message, int shift)
    {
        String new_message = "";

        char[] message_array = message.toCharArray();
        
        for(int i=0;i<message_array.length;i++)
        {
            char c = message_array[i];

            c = (char)((c - 'a' + shift + 26) % 26 + 'a');
            new_message += c;
        }

        return new_message;
    }
}