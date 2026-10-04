#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double PI = 3.14159;
    double radius;
    cin >> radius;
    double area = PI * radius * radius;
    cout << fixed << setprecision(4) << "A=" << area << endl;
    return 0;
}