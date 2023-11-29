#include<iostream>
using namespace std;
struct item
{
  int priority;
  int value;
};

void sort(item a[3])
{
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<2;j++)
        {
            if(a[j].priority>a[j+1].priority)
            {
                swap(a[j].priority,a[j+1].priority);
                swap(a[j].value,a[j+1].value);
            }
        }
    }
}
int main()
{
    item a[3];
    for(int i=0;i<3;i++)
    {
        cout<<"Enter priority=";cin>>a[i].priority;
        cout<<"Enter value=";cin>>a[i].value;
    }
    sort(a);
    cout<<"\nSolution="<<endl;
    for(int i=0;i<3;i++)
    {
        cout<<a[i].value<<endl;
    }
    
    return 0;
}
