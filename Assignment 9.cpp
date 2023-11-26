#include<iostream>
#include<string>
using namespace std;

class stack
{
  public:
  char data;
  char a[100];
  int top=-1;
  
  void push(char d)
  {
    data=d;
    a[++top]=d;
  }
  bool isempty()
  {
    if(top==-1)return true;
    else return false;
  }
  void pop()
  {
    top--;
  }
  char topp()
  {
    return a[top];
  }
  void solve()
  {
    if(top==-1)cout<<"Valid Expression";
    else cout<<"Invalid expression";
  }
};

int main()
{
  stack s;
  string str;
  cout<<"Enter string =";
  cin>>str;
  for(int i=0;i<str.size();i++)
  {
    if(str[i]=='(' || str[i]=='[' || str[i]=='{')
    {
      s.push(str[i]);
    }
    else if((str[i]==')' && s.topp()=='(') || (str[i]==']' && s.topp()=='[') || (str[i]=='}' && s.topp()=='{'))
    {
      s.pop();
    }
  }
  s.solve();
  return 0;
}
