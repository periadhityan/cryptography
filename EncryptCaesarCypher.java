import java.util.Scanner;

public class EncryptCaesarCypher
{
    private static Scanner input;

    public static void main(String[] args)
    {
        input = new Scanner(System.in);
        System.out.print("Enter the message that you wish to encrypt: ");
        String message = input.nextLine();

        System.out.println(caesarcypher(message, 3));
    }

    public static String caesarcypher(String message, int shift)
    {
        String new_message = "";
        message = message.toLowerCase();

        char[] message_array = message.toCharArray();
        
        for(int i=0;i<message_array.length;i++)
        {
            char c = message_array[i];

            if(Character.isLetter(c))
            {
                c = (char)((c - 'a' + shift + 26) % 26 + 'a');
            }

            

            new_message += c;
        }

        return new_message;
    }

    
}
