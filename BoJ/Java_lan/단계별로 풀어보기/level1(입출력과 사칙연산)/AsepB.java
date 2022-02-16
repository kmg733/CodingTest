import java.io.*;

public class AsepB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        String[] splits = input.split(" ");
        bw.write(Double.parseDouble(splits[0]) / Double.parseDouble(splits[1]) + "\n");
        bw.flush();
        bw.close();
    }
}
