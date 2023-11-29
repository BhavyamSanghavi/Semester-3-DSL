#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>

using namespace std;

int precedence(char op) {
    if (op == '+' || op == '-')
        return 1;
    else if (op == '*' || op == '/')
        return 2;
    return 0;
}

string infixToPostfix(const string& infix) {
    stack<char> operators;
    string postfix;
    unordered_map<char, int> prec;

    prec['+'] = prec['-'] = 1;
    prec['*'] = prec['/'] = 2;

    for (char c : infix) {
        if (c == ' ' || c == '\t') continue;

        if (isdigit(c) || isalpha(c)) {
            postfix += c;
        } else if (c == '(') {
            operators.push(c);
        } else if (c == ')') {
            while (!operators.empty() && operators.top() != '(') {
                postfix += operators.top();
                operators.pop();
            }
            operators.pop(); // Discard the '('
        } else { // It's an operator
            while (!operators.empty() && precedence(c) <= precedence(operators.top())) {
                postfix += operators.top();
                operators.pop();
            }
            operators.push(c);
        }
    }

    while (!operators.empty()) {
        postfix += operators.top();
        operators.pop();
    }

    return postfix;
}

int main() {
    string infix_expression = "a + b * (c - d) / e";
    string postfix_expression = infixToPostfix(infix_expression);
    cout << "Infix: " << infix_expression << endl;
    cout << "Postfix: " << postfix_expression << endl;

    return 0;
}
