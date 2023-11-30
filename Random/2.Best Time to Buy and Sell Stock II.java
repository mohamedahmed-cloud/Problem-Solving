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
        int [] wall={1,2,3,4,5};
        System.out.println(encode(wall));

    }
    static int encode(int[] wall) {
        int buy=-1;
        int profit=0;
        for(int i=0;i<wall.length-1;i++){
//            buy if next is larger than me and buy=-1
            if (buy==-1 && wall[i]<wall[i+1] ){
                buy=wall[i];
            }
//            sell if next is smaller than me.
            else if (buy!=-1 && wall[i]>wall[i+1]){
//                System.out.println(wall[i]);
                profit+=(wall[i]-buy);
                buy=-1;
            }
//            System.out.println(buy);
        }
        if (wall[wall.length-1]>buy && buy!=-1){
            profit+=(wall[wall.length-1]-buy);
        }
        return profit;
    }


}