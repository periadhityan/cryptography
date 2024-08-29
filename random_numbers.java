import java.util.Random;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.security.SecureRandom;

public class random_numbers{

    public static void main(String args[]){

        double myRandom_double = Math.random();
        int myRandom_integer = (int)(10*Math.random());
        int myRandom_interval = (int)((30-20)*Math.random() + 20); 


        System.out.println("Random double number = " + myRandom_double);
        System.out.println("Random integer number = " + myRandom_integer);
        System.out.println("Random integer value between an interval = " + myRandom_interval);
        System.out.println();

        Random randomObj = new Random();

        System.out.println("Random integer using Random object = " + randomObj.nextInt(0, 200));
        System.out.println("Random float using Random object = " + randomObj.nextFloat(0, 200));
        System.out.println("Random double using Random object = " + randomObj.nextDouble(0, 200));
        System.out.println("Random boolean using Random object = " + randomObj.nextBoolean());
        System.out.println();

        byte[] randomBytes = new byte[20];
        randomObj.nextBytes(randomBytes);

        System.out.println("Random bytes using Random object = ");
        System.out.println(Arrays.toString(randomBytes));
        System.out.println();

        Random randomObj2 = new Random();
        randomObj2.setSeed(10);

        System.out.println("Random integers generated after setting seed value: ");
        for(int i=0;i<5;i++){
            System.out.println((i+1) + ". " + randomObj2.nextInt());
        }
        System.out.println();

        randomObj2.setSeed(10);
        System.out.println("Setting seed will generate the same pseudo random sequence: ");
        for(int i=0;i<5;i++){
            System.out.println((i+1) + ". " + randomObj2.nextInt());
        }
        System.out.println();

        List<Integer> randomList = new ArrayList<Integer>();

        for(int i=0;i<10;i++){
            randomList.add(randomObj.nextInt(20));
        }

        System.out.println("List generated using Random object and a for loop: ");
        System.out.println(randomList);
        System.out.println();

        List<Integer> randomStream = new ArrayList<Integer>();

        randomStream = randomObj.ints(10, 0, 10).boxed().collect(Collectors.toList());


        System.out.println("List generated using Random object and a stream: ");
        System.out.println(randomStream);
        System.out.println();

        SecureRandom secureRandom = new SecureRandom();
        System.out.println("Random integer generated using Secure Random object: " + secureRandom.nextInt());


    }
 }