#include <iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    Node(int d)
    {
        data=d;
        next=NULL;
    }
};
void print(Node* head){
    Node*temp=head;
    while(temp){
        cout<<temp->data<<"->";
        temp=temp->next;
    }
}

Node* both(Node* head1,Node* head2){
    Node* ans=new Node(-1);
    Node* temp=ans;
    while(head1->next){
        Node* temp2=head2;
        while(temp2->next){
            if(head1->data==temp2->data){
                Node* newnode=new Node(head1->data);
                temp->next=newnode;
                temp=temp->next;
            }
            temp2=temp2->next;
        }
        head1=head1->next;
    }
    return ans->next;
}

Node* symdiff(Node* head1 , Node* head2 , Node* inter){
    Node* ans=new Node(-1);
    Node* temp=ans;
    while(head1->next)
    {
        bool flag=false;
        Node*temp2=inter;
        while(temp2)
        {
            if(head1->data==temp2->data){
                flag=true;
            }
            temp2=temp2->next;
        }
        if(flag==false)
        {
            Node* newnode=new Node(head1->data);
            temp->next=newnode;
            temp=temp->next;
        }
        head1=head1->next;
    }
    while(head2->next)
    {
        bool flag=false;
        Node*temp2=inter;
        while(temp2)
        {
            if(head2->data==temp2->data){
                flag=true;
            }
            temp2=temp2->next;
        }
        if(flag==false)
        {
            Node* newnode=new Node(head2->data);
            temp->next=newnode;
            temp=temp->next;
        }
        head2=head2->next;
    }
   
    return ans->next;
}

Node*unio(Node*diff,Node*inter)
{
    Node*head=diff;
    while(diff->next)
    {
        diff=diff->next;
    }
    diff->next=inter;
    return head;
}

Node* c(Node*head,Node*uni)
{
    Node* ans=new Node(-1);
    Node* temp=ans;
    while(head->next){
        Node* temp2=uni;
        bool flag=false;
        while(temp2){
            if(temp2->data==head->data)
            {
                flag=true;
                break;
            }
            temp2=temp2->next;
        }
        if(flag==false)
        {
            Node* newnode=new Node(head->data);
            temp->next=newnode;
            temp=temp->next;
        }
        head=head->next;
    }
    return ans->next;
}

int main() {
    Node* head=new Node(-1);
    Node* temp=head;
    int data=0;
    while(data!=-1)
    {
        cout<<"enter data=";
        cin>>data;
        Node* newnode=new Node(data);
        temp->next=newnode;
        temp=temp->next;
    }
    head=head->next;
   
   
    Node* head1=new Node(-1);
    temp=head1;
    data=0;
    while(data!=-1)
    {
        cout<<"enter data=";
        cin>>data;
        Node* newnode=new Node(data);
        temp->next=newnode;
        temp=temp->next;
    }
    head1=head1->next;
   
   cout<<endl<<endl;
    Node* head2=new Node(-1);
    temp=head2;
    data=0;
    while(data!=-1)
    {
        cout<<"enter data=";
        cin>>data;
        Node* newnode=new Node(data);
        temp->next=newnode;
        temp=temp->next;
    }
    head2=head2->next;
   
    Node* inter=both(head1,head2);
    cout<<"Intersection"<<endl;
     print(inter);
     cout<<endl<<endl;
     
     
     cout<<"Difference"<<endl;
    Node*diff=symdiff(head1,head2,inter);
    print(diff);
    cout<<endl<<endl;
   
   
    Node*uni=unio(diff,inter);
    Node*ans3=c(head,uni);
    cout<<"Answer 3"<<endl;
    print(ans3);
    return 0;
}
