import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class buffer {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   
        String input = br.readLine();

        StringTokenizer st = new StringTokenizer(input);
        while(st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }

        String splits[] = input.split(" ");
        for (int i=0; i<splits.length; i++) {
            System.out.println(splits);
        }
        bw.close();
        return;
    }
}
