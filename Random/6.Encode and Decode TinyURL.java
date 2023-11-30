/*
    Author : Mohamed Yousef 
    Date   : 2022-12-17
*/
// package com.company;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Main {
    public static HashMap<String,String> mapping=new HashMap<>();
    public static int finalValue=0;
    public static void main(String[] args) {
        String longUrl="http://bomb.example.com/basket.htm";
        encode(longUrl);

    }
    static void encode(String longUrl) {
        String ans="";
        long count=0;
        String [] array=longUrl.split("/");
//        System.out.println(longUrl.substring(longUrl.length()-1).equals("/"));
        if (longUrl.substring(longUrl.length()-1).equals("/")){
//            System.out.println("hlklfj");
            finalValue=1;
        }
        for(String i : array){
            if(i==""){
                i="/";
            }
            ans+=String.valueOf(count);
            mapping.put(String.valueOf(count),i);
            count++;
        }
//        change this in leetcode by return ans
        decode(ans);
    }
    static String decode(String shortUrl){
        String [] url=shortUrl.split("");
        String out="";
        int add=0;
        for(String i :url){
            out+=mapping.get(i);
//            System.out.println(add);
            if(mapping.get(i)!="/" || add==(url.length-1)){
                out+="/";
            }
            add+=1;
        }
        String myAns=out.substring(0,out.length()-1+finalValue);
        finalValue=0;
        System.out.println(myAns);
        return myAns;
    }


}
