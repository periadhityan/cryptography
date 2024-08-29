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

        Random randomObj2 = new Random();
        randomObj2.setSeed(10);

        System.out.println("Random integers generated after setting seed value: ");
        for(int i=0;i<5;i++){
            System.out.println((i+1) + ". " + randomObj2.nextInt());
        }
        
        randomObj2.setSeed(10);
        System.out.println("Setting seed will generate the same pseudo random sequence: ");
        for(int i=0;i<5;i++){
            System.out.println((i+1) + ". " + randomObj2.nextInt());
        }

    }
 }