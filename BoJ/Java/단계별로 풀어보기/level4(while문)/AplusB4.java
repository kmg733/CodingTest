import java.io.*;

public class AplusB4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input;
        while((input = br.readLine()) != null && input.length() != 0) {
            String[] ary = input.split(" ");
            int a = Integer.parseInt(ary[0]);
            int b = Integer.parseInt(ary[1]);
            
            bw.write(a + b + "\n");
       }
       bw.flush();
       bw.close(); 

    }
}
