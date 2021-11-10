#include<iostream>
#include<vector>
using namespace std;
int main()
{
    system("cls");
    int n;
    cout<<"Enter the number of Withnesses: ";
    cin>>n;
    vector<vector<string>> witness;
    string temp;
    for(int a=0;a<n;a++){
        cout<<"Enter the Statements of "<<a+1<<"th Witness.:-"<<endl;
        for(int i=0; getline(cin,witness[a][i],'.'); i++);
    }
    for(int i=0; cout<<witness[0]<<endl ; i++)
    return 0;
}