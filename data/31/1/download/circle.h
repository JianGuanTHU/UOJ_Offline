#include "shape.h"
#include <iostream>

class Circle : public Shape {
public:
    void draw() {
        std::cout << "Drawing Circle" << std::endl;
    }
    void resize() {
        std::cout << "Resizing Circle" << std::endl;
    }
    std::string description() {
        return "Circle object";
    }
};
