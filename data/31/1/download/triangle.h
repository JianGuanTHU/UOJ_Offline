#include <cmath>
#include <iostream> 
#include "new_shape.h"

class Triangle : public NewShape {
    double a;
    double b;
    double c;
public:
    Triangle() {
        a = 1.;
        b = 1.;
        c = 1.;
    }
    double area() {
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
    double perimeter() {
        return a + b + c;
    }
    void drawShape() {
        std::cout << "Drawing Triangle with area: " << area() << " and perimeter: " << perimeter() << std::endl;
    }
    std::string description() {
        return "Triangle object";
    }
};
