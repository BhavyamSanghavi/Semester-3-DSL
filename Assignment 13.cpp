#include <iostream>
using namespace std;

class queue
{
  public:
  int a[100];
  int front=50,rear=50;
 
  void print(int front,int rear)
  {
    for(int i=front;i<rear;i++)cout<<a[i]<<"  ";
    cout<<endl;
  }
  bool isEmpty()
  {
    if(front==rear)return true;
    else return false;
  }
  void pushback(int data)
  {
    a[rear++]=data;
    print(front,rear);
  }
  void pushfront(int data)
  {
    a[--front]=data;
    print(front,rear);
  }
  void popfront()
  {
    if(isEmpty())cout<<"Queue is empty"<<endl;
    else
    {
      cout<<"Element delete="<<a[front]<<endl;
      front++;
      print(front,rear);
    }
  }
  void popback()
  {
    if(isEmpty())cout<<"Queue is empty"<<endl;
    else
    {
      cout<<"Element delete="<<a[rear--];
      print(front,rear);
    }
  }
};

int main()
{
    queue q;
    int con=1;
    while(con)
    {
      int op;
      cout<<"Press 1 to Push and 2 to delete="<<endl;cin>>op;
      if(op==1)
      {
        int data;
        cout<<"Enter data=";cin>>data;
        q.pushback(data);  
      }
      else if(op==2)
      {
        q.popfront();
      }
      else if(op==3)
      {
       
      }
      cout<<"Press 0 to exit:";
      cin>>con;
    }
    return 0;
}
