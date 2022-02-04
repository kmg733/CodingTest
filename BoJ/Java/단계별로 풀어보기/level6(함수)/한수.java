import java.io.*;

public class 한수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int result = hansu(Integer.parseInt(br.readLine()));

        bw.write(Integer.toString(result));
        bw.flush();
        bw.close();
    }   

    public static int hansu(int num) {
        int count = 0;
        // 1 ~ 99 는 모두 등차 수열이기 때문에
        // 100보다 작은 수들은 그대로 출력하면 된다.
        if(num < 100) {
            return num;
        } else {
            count = 99;
            if(num == 1000) {
                num = 999;
            }

            for(int i = 100; i <= num; i++) {
                int hundred = i / 100;
                int ten = (i / 10) % 10;
                int one = i % 10;

                if((hundred - ten) == (ten - one)) {
                    count++;
                }
            }
        }

        return count;
    }
}
