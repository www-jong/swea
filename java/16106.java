import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();
        for (int i = 1; i <= T; i++) {
            ArrayList<Integer> station = new ArrayList<>();
            int K = sc.nextInt();
            int N = sc.nextInt();
            int M = sc.nextInt();
            sc.nextLine();
            for (int j = 0; j < M; j++) {
                station.add(sc.nextInt());
            }
            station.add(N);
            // sc.nextLine(); // 삭제해야 함
            int idx = 0;
            int res = 0;
            while (idx < N) {
                res++;
                int check = 0;
                for (int k = idx + 1; k <= idx + K; k++) {
                    if (station.indexOf(k) != -1) {
                        check = k;
                    }
                }
                if (check != 0) {
                    idx = check;
                } else {
                    res = 1;
                    break;
                }
            }
            // sc.nextLine(); // 삭제해야 함
            System.out.printf("#%d %d\n", i, res - 1);
        }
    }
}
