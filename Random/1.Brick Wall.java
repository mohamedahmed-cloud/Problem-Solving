/*
    Author : Mohamed Yousef 
    Date   : 2022-12-20
*/
/* 
    Simple note this approach is true but I use in my Solution Array of Array not ArrayList 
    so i You run this solution in leetcode will give you RunTime Error 
    I used Array of array Because I Still don't know arraylist Very Well.
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
        int [][] wall={{1,2,2,1},{3,1,2},{1,3,2},{2,4},{3,1,2},{1,3,1,1}};
        encode(wall);

    }
    static void encode(int[][] wall) {
//        System.out.println(Arrays.deepToString(wall));
//       Create Dictionary
        Map<Long, Long> dictionary = new HashMap<Long, Long>();
        long n=wall.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<wall[i].length;j++){
                if (j!=0)
                    wall[i][j]+=wall[i][j-1];
                long key=wall[i][j];
                long x=0;
//                To Put initial value in Dict and or update its if it have.
                dictionary.put(key, dictionary.getOrDefault(key, x) + 1);
            }
        }
        long ans=0;
        int last=wall[0].length-1;
//        To Iterate on Dict By Key and Vaule
        for (Map.Entry<Long, Long> entry : dictionary.entrySet()) {
            long key = entry.getKey();
            long val = entry.getValue();
            if (key!=wall[0][last])
                ans=Math.max(ans,val);
        }
        System.out.println(n-ans);
    }


}