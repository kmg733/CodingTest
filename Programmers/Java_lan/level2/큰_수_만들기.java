public class 큰_수_만들기 {
    public static void main(String[] args) {
        System.out.println(solution("4177252841", 4));
    }
    public static String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        int index = 0;
        int max = 0;
        // 정답 문자열의 길이는 매개변수로 들어온 number의 길이에서 k만큼 빼준 길이가 됨.
        // 따라서 k를 빼준값만큼 for문 반복
        for(int i = 0; i < number.length() - k; i++) {
            max = 0;
            // 두번째 for문의 범위는 탐색해야하는 문자의 시작 인덱스 부터
            // 뒤에 남는 인덱스까지 탐색해야 한다
            for(int j = index; j <= k + i; j++) {
                if(max < number.charAt(j) - '0') {
                    max = number.charAt(j) - '0';
                    index = j + 1;
                }
            }
            sb.append(max);
        }
        return sb.toString();
    }
}
