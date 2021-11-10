#include <iostream>
using namespace std;
struct node
{
    int data;
    node *next;
};
node *head, *temp, *newnode;
int insertatbegin()
{
    head = NULL;
    int n, x;
    cout << "Numbers of element: ";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        temp = new node();
        cout << "Enter num: ";
        cin >> temp->data;
        temp->next = head;
        head = temp;
    }
}
int insertatpos()
{
    head = NULL;
    int num, count = 0;
    cout << "Enter the no. of elements in list : ";
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        newnode = new node();
        cout << "Enter number: ";
        cin >> newnode->data;
        newnode->next = NULL;
        if (head == NULL)
        {
            head = temp = newnode;
        }
        else
        {
            temp->next = newnode;
            temp = newnode;
        }
    }
    cout << "At what position do we need to insert element:";
    int pos;
    cin >> pos;
    temp = head;
    count = 1;
    while (temp->next != NULL)
    {
        if (pos == count + 1)
        {
            newnode = new node();
            cout << "Enter number: ";
            cin >> newnode->data;
            newnode->next = temp->next;
            temp->next = newnode;
        }
        count++;
        temp = temp->next;
    }
}
int display()
{
    cout << "List is: ";
    temp = head;
    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
}
int main()
{
    cout << "Name: Tejas Jain, Roll: 2K20/CO/460 " << endl;
    int choice;
    do
    {
        cout<<"1. Insert at beginning "<<endl
            <<"2. Insert at particular position "<<endl
            <<"3. Display "<<endl
            <<"4. Exit" << endl;
        cin >> choice;
        switch (choice)
        {
        case 1:
            insertatbegin();
            cout << endl;
            break;
        case 2:
            insertatpos();
            cout << endl;
            break;
        case 3:
            display();
            cout << endl;
            break;
        case 4:
            exit(0);
            break;
        }
    } while (choice != 4);
    return 0;
}