import java.util.Random;
import java.util.Arrays;

public class random_numbers{

    public static void main(String args[]){

        double myRandom_double = Math.random();
        int myRandom_integer = (int)(10*Math.random());
        int myRandom_interval = (int)((30-20)*Math.random() + 20); 


        System.out.println("Random double number = " + myRandom_double);
        System.out.println("Random integer number = " + myRandom_integer);
        System.out.println("Random integer value between an interval = " + myRandom_interval);

        Random randomObj = new Random();

        System.out.println("Random integer using Random object = " + randomObj.nextInt(0, 200));
        System.out.println("Random float using Random object = " + randomObj.nextFloat(0, 200));
        System.out.println("Random double using Random object = " + randomObj.nextDouble(0, 200));
        System.out.println("Random boolean using Random object = " + randomObj.nextBoolean());

        byte[] randomBytes = new byte[20];
        randomObj.nextBytes(randomBytes);

        System.out.println("Random bytes using Random object = " + Arrays.toString(randomBytes));
        

    }
 }