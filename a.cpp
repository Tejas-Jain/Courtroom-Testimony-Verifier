#include<bits/stdc++.h>
using namespace std;
void printing(vector<string> &s){
    for(string t: s){
        cout<<t <<'\n';
    }
}
int main()
{
    system("cls");
    cout<<"Name: Tejas Jain, Roll No.: 2K20/CO/460 \n";
    cout<<"Enter Statement in String 1";
    vector<string> st1,st2;
    string temp, temp2;
    while(getline(cin, temp, '.')){
        st1.push_back(temp);
        printing(st1);
    }
        
    while(getline(cin, temp2, '.'))
        st2.push_back(temp2);
    printing(st1);
    printing(st2);
    return 0;
}