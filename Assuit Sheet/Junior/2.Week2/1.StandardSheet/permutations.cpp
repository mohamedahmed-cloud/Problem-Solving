#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    int n,q;
    string s;
    cin>>n;
    cin>>q;
    // cout<<n<<q;
    cin>>s;

    for(int i=0;i<q;i++){
        string next_prev;
        int b;
        cin>>next_prev>>b;
        if (next_prev=="next_permutation"){
            while(b--){
                next_permutation(s.begin(),s.end());
            }
        }
        else {
            while(b--){
                prev_permutation(s.begin(),s.end());
            }
        }
            cout<<s<<endl;


    }
}