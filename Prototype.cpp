#include<bits/stdc++.h>
using namespace std;
class witness{
    public: 
        string statement, temp; 
        vector<string> line;
        float trust=100;
        witness(){
            fflush(stdin);
            getline(cin, statement);
            stringstream ss(statement);
            for(int i=0; getline(ss, temp, '.');i++)
                line.push_back(temp);
        }
        void display(){
            cout<<"The lines are:- "<<endl;
            for(string t: line)
                cout<<t<<endl;
        }
};
vector<string> crosscheck(witness& w, witness pol){
    vector<string> false_stat;
    for(string t: w.line){
        auto it = find(pol.line.begin(), pol.line.end(),t);
        if(it==(pol.line.end()))
            false_stat.push_back(t);
    }
    // cout<<false_stat.size()<<" "<<w.line.size()<<" "<<pol.line.size()<<endl;
    // for(string t: w.line)
    //     cout<<t<<endl;
    // for(string t: pol.line)
    //     cout<<t<<endl;
    w.trust = (1-(float)false_stat.size()/w.line.size())*100;
    if(!false_stat.empty())
        return false_stat;
    else
        return {"NOT FOUND!!!"};
}
int main()
{
    system("cls");
    cout<<"\nEnter the Victim Statement: "<<endl;
    witness victim;
    cout<<"\nEnter the Accused Statement: "<<endl;
    witness accused;
    int n;
    cout<<"\nEnter number of Witness: ";
    cin>>n;
    vector<witness> wt;
    for(int i=1;i<=n;i++){
        cout<<"\nEnter the Statement of Witness "<<i<<":\n";
        witness temp;
        wt.push_back(temp);
    }
    cout<<"\nEnter the Police Investigation: "<<endl;
    witness pol;
    system("cls");
    cout<<"For ACCUSED :"<<endl;
    vector<string> cs1 = crosscheck(accused, pol);
    cout<<"The Unmatched Statements: "<<endl;
    for(string t: cs1)
        cout<<'\t'<<t<<endl;
    cout<<"Trustfullness= "<<accused.trust<<"%";

    cout<<"\n\nFor VICTIM :"<<endl;
    vector<string> cs2 = crosscheck(victim, pol);
    cout<<"The Unmatched Statements: "<<endl;
    for(string t: cs2)
        cout<<'\t'<<t<<endl;
    cout<<"Trustfullness= "<<victim.trust<<"%";

    for(int i=0;i<n;i++){
        cout<<"\n\nFor WITNESS "<<i+1<<":"<<endl;
        vector<string> crossStatements = crosscheck(wt[i], pol);
        cout<<"The Unmatched Statements: "<<endl;
        for(string t: crossStatements)
            cout<<'\t'<<t<<endl;
        cout<<"Trustfullness= "<<wt[i].trust<<"%\n";
    }
    system("pause");
    return 0;
}

//Sample Statements:
//  The car was moving. The car driver was on phone. The biker was in right lane. The biker was wearing helmet.
//  The biker was not wearing helmet. The biker was in right lane. The car was not moving. The car driver was not using phone.
//  The biker was in wrong lane. The biker was not wearing helmet. The car was not moving. The car driver was not using phone.
//  The biker was wearing helmet. The biker was in right lane. The car was moving. The car driver was not on phone. 
 