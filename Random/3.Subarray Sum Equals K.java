/*
    Author : Mohamed Yousef 
    Date   : 2023-01-05
*/
// package com.company;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static HashMap<String,String> mapping=new HashMap<>();
    public static int finalValue=0;
    public static void main(String[] args) {
        int [] wall={1};
        int k=0;
        System.out.println(encode(wall,k));

    }
    static int encode(int[] nums,int k) {
         HashMap<Integer,Integer> mapping=new HashMap<>();
         int ans=0;
         int sum=0;
         mapping.put(0,1);
         for(int i: nums){
             sum+=i;
             ans+=mapping.getOrDefault(sum-k,0);
             mapping.put(sum,mapping.getOrDefault(sum,0)+1);
         }
         return ans;

    }


}