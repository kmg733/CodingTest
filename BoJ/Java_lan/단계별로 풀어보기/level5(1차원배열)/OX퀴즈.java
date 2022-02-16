import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class OX퀴즈 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            char[] quiz = br.readLine().toCharArray();
            int count = 0, sum = 0;
            for(int j = 0; j < quiz.length; j++) {                
                if(quiz[j] == 'O') {                    
                    count += 1;                    
                    sum += count;
                }
                if(quiz[j] == 'X') {
                    count = 0;                   
                }
            } 
            bw.write(sum + "\n");
        }
        bw.flush();
        bw.close(); 
    }
}
