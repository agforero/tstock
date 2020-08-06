#include <iostream>
#include <string>
using namespace std;

class Person {
private:
    string name = "";

public:
    Person(string n) {
        name = n;
    }
    string getName() {
        return name;
    }
};