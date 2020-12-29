// 1
import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++)
        {
        	if (map.containsKey(target - nums[i]))
        	{
        		return new int[] {map.get(target - nums[i]), i};
        	}
        	map.put(nums[i], i);
        }
        return null;
    }
}

class Solution {
	public int[] twoSum(int[] nums, int target){
		int len = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
        	final Integer value = map.get(nums[i]);
        	if (value != null) {
        		return new int[] {value, i};
        	}
        	map.put(target - nums[i], i);
        }
        return null;
    }
}
    


// 2
class Solution{
	public int[] twoSum(int[] nums, int target){
		for (int i = 0; i < nums.length; i++)
		{
			for (int j = i + 1; j < nums.length; i++)
			{
				if (nums[i] + nums[j] == target)
				{
					return new int[] {i, j};
				}
			}
		}
		return null;
	}
}