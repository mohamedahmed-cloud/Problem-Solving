#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i =0 ; i<n ; i++){
        // fib number
        int c ;
        cin>>c;
        long long a1,a2,a3,count;
        a1=0,a2=1,a3=1,count=0;
        for(int j =2 ; j<c ; j++){
            a3=a1+a2;
            a1=a2;
            a2=a3;
        }
        // prime
        if (a3==1 || a3==0){
                count=1;
            cout<<"not prime"<<endl;
        }
        else{
            for(int j=2 ; j*j<=a3 ; j++){
                if(a3%j==0){
                    count=1;
                    cout<<"not prime"<<endl;
                    break;
                }
            }}
        if (count==0){
            cout<<"prime"<<endl;
        }
    }
}