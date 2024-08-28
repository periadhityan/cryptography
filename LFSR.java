public class LFSR{

    public static void main(String[] args){

        int start_state = 0b1001110000101101;
        int output = start_state;
        int bit;
        int period = 0;

        do{
            bit = ((output>>0)^(output>>2)^(output>>3)^(output>>5)) & 1;
            output = (output>>1) | (bit<<15);
            System.out.println("Output  = " + intToBinary(output));
            period += 1;
        }while(output != start_state);

        System.out.println("Period = "  + period);
    }

    public static String intToBinary(int n)
    {
        String s = "";
        while (n > 0)
        {
            s =  ( (n % 2 ) == 0 ? "0" : "1") +s;
            n = n / 2;
        }
        return s;
    }
    

}