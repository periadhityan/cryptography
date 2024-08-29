public class random_numbers{

    public static void main(String args[]){

        double myRandom_double = Math.random();
        int myRandom_integer = (int)(10*Math.random());
        int myRandom_interval = (int)((30-20)*Math.random() + 20); 


        System.out.println("Random double number = " + myRandom_double);
        System.out.println("Random integer number = " + myRandom_integer);
        System.out.println("Random integer value between an interval = " + myRandom_interval);

    }
 }