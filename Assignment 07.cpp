#include <iostream>
using namespace std;
class node
{
  public:
  char data;
  node*next;
  node*prev;
  node(char d)
  {
    data=d;
    node* next=NULL;
    node*prev=NULL;
  }
};

void print(node*a[10])
{
  for(int i=0;i<10;i++)
  {
    node*temp=a[i];
    while(temp!=NULL)
    {
      cout<<temp->data<<"  ";
      temp=temp->next;
    }
    cout<<endl;
  }
  cout<<"\n\n\n\n";
}

void bookseat(node*a[10],int row,int col)
{
  node*h=a[row-1];
  node*head=h;
  for(int i=0;i<col-1;i++)
  {
    head=head->next;
  }
  if(head->data=='B') cout<<"Seat already booked"<<endl;
  else head->data='B';
}

void cancel(node*a[10],int row,int col)
{
  node*h=a[row-1];
  node*head=h;
  for(int i=0;i<col-1;i++)
  {
    head=head->next;
  }
  if(head->data=='A') cout<<"Seat was not already booked"<<endl;
  else head->data='A';
}

int main() 
{
    node * a[10];
    for(int i=0;i<10;i++)
    {
      a[i]=new node('A');
    }
    for(int i=0;i<10;i++)
    {
      node* head=a[i];
      for(int j=0;j<6;j++)
      {
        node*t=new node('A');
        head->next=t;
        t->prev=head;
        head=t;
      }
    }
    
    int row,col;
    cout<<"Enter row="; cin>>row;
    cout<<"Enter column="; cin>>col;
    cout<<endl;
    bookseat(a,2,3);
    bookseat(a,3,2);
    
    print(a);
    cancel(a,row,col);
    print(a);
    return 0;
}
