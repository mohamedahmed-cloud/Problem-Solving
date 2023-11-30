/*
    Author : Mohamed Yousef 
    Date   : 2022-12-16
*/
package com.company;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] nums = new int[]{2, 0, 2, 1, 1, 0};
        sortColors(nums);
    }
    static void sortColors(int[] nums) {
        int[] freq=new int[]{0,0,0};
        int length=nums.length;
//        Freq freq
        for(int i=0;i<length;i++){
            freq[nums[i]]+=1;
        }
        int count=0;
        for(int i=0;i<3;i++){
            while(freq[i]>0){
                nums[count]=i;
                count+=1;
                freq[i]-=1;
            }
        }

        System.out.println(Arrays.toString(nums));
    }

}