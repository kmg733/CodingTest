public class 조이스틱 {
    public static void main(String[] args) {
        System.out.println(solution("JEROEN"));
    }

    public static int solution(String name) {
        // 알파벳의 개수는 총 26개
        int answer = 0;

        // 좌우로 움직이는 횟수
        int moveLR = name.length() - 1;
        
        for(int i = 0; i < name.length(); i++) {
            // 조이스틱 상, 하 이동
            int num = name.charAt(i) - 'A';
            if(num > 13) {
                num = 26 - num;
            }
            answer += num;

            
            // 조이스틱 좌, 우 이동
            int nextIndex = i + 1;
            
            // 다음 A가 아닌 문자의 인덱스를 찾음
            while(nextIndex < name.length() && name.charAt(nextIndex) == 'A') {
                nextIndex++;
            }
            // BBBAAAAAABA 와 같이 중간까지 왔다 다시 왼쪽으로 돌아가는 것이 더 빠른 경우
            moveLR = Math.min(moveLR, i * 2 + name.length() - nextIndex);
            // BBBBAAAAAAAAB 와 같이 처음부터 뒤로가서 먼저 입력하는 경우
            moveLR = Math.min(moveLR, (name.length() - nextIndex) * 2 + i);
        }
        answer += moveLR;
        return answer;
    }
}
