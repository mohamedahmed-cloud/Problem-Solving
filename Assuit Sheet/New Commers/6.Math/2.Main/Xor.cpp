// Time Limit In Test 4
#include <iostream>
using namespace std;

int main(){
    long long A,B,Q,ans;
    cin>>A>>B>>Q;
    if (Q==1){
        cout<<A;
    }
    else if (Q==2){
        cout<<B;
    }else if  (Q>2){
        ans=0;
        for(int i=3; i<=Q;i++){
            ans+=A^B;
            A=B;
            B=ans;
        }
        cout<<ans;
    }
}