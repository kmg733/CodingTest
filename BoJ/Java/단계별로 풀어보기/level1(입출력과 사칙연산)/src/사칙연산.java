import java.io.*;

public class 사칙연산 {
    public static void main(String[] args) throws IOException {
        사칙연산 cal = new 사칙연산();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        String[] splits = input.split(" ");
        int a = Integer.parseInt(splits[0]);
        int b = Integer.parseInt(splits[1]);

        cal.plus(a, b);
        cal.minus(a, b);
        cal.mul(a, b);
        cal.sep(a, b);
        cal.rmd(a, b);
        bw.flush();
        bw.close();
    }

    public void plus(int a, int b) {
        System.out.println(a + b);
    }

    public void minus(int a, int b) {
        System.out.println(a - b);
    }

    public void mul(int a, int b) {
        System.out.println(a * b);
    }

    public void sep(int a, int b) {
        System.out.println(a / b);
    }

    public void rmd(int a, int b) {
        System.out.println(a % b);
    }
}

