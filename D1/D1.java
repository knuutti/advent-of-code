import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;

class D1 {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("D1_data.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        Integer count = 0;
        Integer[] top_elves = {0, 0, 0};

        try {
            while ((st = br.readLine()) != null) {

                if (st.length() == 0) {
                    if (count > top_elves[2]) {
                        top_elves[2] = count;
                        Arrays.sort(top_elves, Collections.reverseOrder());
                    }
                    count = 0;
                    continue;
                }
                else {
                    count += Integer.parseInt(st);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        Integer sum = top_elves[0] + top_elves[1] + top_elves[2];

        System.out.println(top_elves[0]);
        System.out.println(sum);

    }
}