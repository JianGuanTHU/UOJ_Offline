#include "shape.h"
#include <iostream>

class Rectangle : public Shape {
public:
    void draw() {
        std::cout << "Drawing Rectangle" << std::endl;
    }
    void resize() {
        std::cout << "Resizing Rectangle" << std::endl;
    }
    std::string description() {
        return "Rectangle object";
    }
};
