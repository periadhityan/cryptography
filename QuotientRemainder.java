import java.util.Scanner;

public class QuotientRemainder {

    private static Scanner in;
    public static void main(String args[])
    {
        in = new Scanner(System.in);

        System.out.print("Enter divisor: ");
        double divisor = in.nextDouble();

        System.out.print("Enter dividend: ");
        double dividend = in.nextDouble();

        System.out.println("What would you like: ");
        System.out.println("1. Quotient");
        System.out.println("2. Remainder");
        System.out.print("Choice: ");
        int choice = in.nextInt();
        double result = 0;

        switch(choice)
        {
            case(1):
            result = Quotient(divisor, dividend);
            break;

            case(2):
            result = Remainder(divisor, dividend);
            break;

            default:
            System.out.println("Invalid input");
                
        }

        System.out.println("Result = " + result);
    }

    public static double Quotient(double divisor, double dividend)
    {
        double sign = Math.signum(dividend);
        double abs_dividend = Math.abs(dividend);
        double quotient = sign * Math.floor(divisor/abs_dividend);

        return quotient;
    }

    public static double Remainder(double divisor, double dividend)
    {
        double quotient = Quotient(divisor, dividend);
        double remainder = dividend - divisor*quotient;

        return remainder;
    }

    
}