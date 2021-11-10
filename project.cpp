#include<iostream>
using namespace std;
int main()
{
    system("cls");
    // int n=3;
    cout<<"Enter Statements: ";
    // cin>>n;
    string s[3];
    for(int i=0; i<3; i++){
        getline(cin, s[i], '.' );
        if(i==1)
            cout<<"Buffer clean"<<endl;
    }
    for(int i=0; i<3; i++){
        cout<<s[i]<<endl;
    }
    return 0;
}