#include<iostream>
#include<sstream>
#include<vector>
using namespace std;
class witness{
        string stat, temp; 
        vector<string> line, wordTemp;
        vector<vector<string>> word;
    public: 
        witness(){
            cout<<"Enter the statements: "<<endl;
            fflush(stdin);
            getline(cin, stat);
            stringstream ss(stat),st;
            for(int i=0;i<3;i++){
                getline(ss, temp, '.');
                line.push_back(temp);
                st<<temp;
                for(int j=0;j<6;j++){
                    st>>temp;
                    wordTemp.push_back(temp);
                }
                word.push_back(wordTemp);
            }
            cout<<word[1][2];
        }
        void display(){
            cout<<"The lines are:- "<<endl;
            for(int i=0; i<3; i++)
                cout<<line[i]<<endl;
            cout<<"The Words of: ";
            for(int i=0;i<3;i++){
                cout<<"Line "<<i<<" :-"<<endl;
                for(int j=0;j<6;j++)
                    cout<<word[i][j]<<endl;
            }
        }
};
int main()
{
    system("cls");
    int n=1;
    cout<<"Enter the number of Withnesses: ";
    // cin>>n;
    witness w[n];
    w[0].display();
    // for(int i=0;  ; i++)
    return 0;
}