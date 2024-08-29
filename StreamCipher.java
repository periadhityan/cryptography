import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.Random;

public class StreamCipher{

    public static Scanner in = new Scanner(System.in);
    public static void main(String args[]){

        System.out.println("Write a sequence of 0's and 1's: ");
        String myString = in.nextLine();

        System.out.println("You have entered: " + myString);

        List<Integer> key = new ArrayList<Integer>();

        for(int i=0;i<myString.length();i++){
            key.add((int)myString.charAt(i)-48);
        }

        System.out.println("The key is: " + key);

        String password = "abcdefgh";

        int hash = HashCode(password);

        Random randomObj = new Random();
        randomObj.setSeed((long)hash);

        List<Integer> randomStream = new ArrayList<Integer>();
        randomStream = randomObj.ints(password.length(), 0, 2).boxed().collect(Collectors.toList());

        System.out.println(randomStream);

        List<Integer> ciphered = new ArrayList<Integer>();

        for(int i=0;i<key.size();i++){
            ciphered.add(key.get(i)^randomStream.get(i));
        }

        System.out.println("Cipher text for password = " + ciphered);

    }

    public static int HashCode(String password){

        int hash = password.hashCode();
        System.out.println("The hashed password is " + hash);
        return hash;
    }
}