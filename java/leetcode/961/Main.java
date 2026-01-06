import java.util.HashMap;

public class Main {

    public class Solution {

        public int repeatedNTimes(int[] nums) {
            HashMap<Integer, Integer> map = new HashMap<>();

            for (int num : nums) {
                map.merge(num, 1, Integer::sum);
            }

            int[] count = { 0 },
                res = { -1 };
            map.forEach((k, v) -> {
                if (v > count[0]) {
                    count[0] = v;
                    res[0] = k;
                }
            });
            return res[0];
        }
    }

    public void main() {
        Solution sol = new Solution();
        int[] nums = { 1, 2, 3, 3 };
        IO.println("Solution : " + sol.repeatedNTimes(nums));
    }
}
