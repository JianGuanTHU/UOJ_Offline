#include <cmath>
#include <iostream> 
#include "new_shape.h"

class Rhombus : public NewShape {
    double a;
    double b;
public:
    Rhombus() {
        a = 1.;
        b = 1.;
    }
    double area() {
        double s = a * b;
        return s;
    }
    double perimeter() {
        return 2 * (a + b);
    }
    void drawShape() {
        std::cout << "Drawing Rhombus with area: " << area() << " and perimeter: " << perimeter() << std::endl;
    }
    std::string description() {
        return "Rhombus object";
    }
};
