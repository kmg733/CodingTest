public class 셀프_넘버 {
    public static void main(String[] args) {
        boolean[] check = new boolean[10001];

        for(int i=1; i < 10001; i++) {
            int n = genNum(i);

            if(n < 10001) {
                check[n] = true;
            }
        }

        StringBuilder sb = new StringBuilder();

        for(int i=1; i < 10001; i++) {
            if(check[i] == false) {
                sb.append(i+"\n");
            }
        }
        System.out.println(sb);
    }

    public static int genNum(int num)  {
        int sum = num;
        while(num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
