#include <iostream>
#include <vector>
#include "shape.h"

class Drawing {
    std::vector<Shape*> shapes;
public:
    void addShape(Shape* shape) {
        shapes.push_back(shape);
    }
    void draw() {
        if (shapes.empty())
            std::cout << "Nothing to draw!" << std::endl;
        for (auto shape : shapes) {
            shape->draw();
        }
    }
    void resize() {
        if (shapes.empty())
            std::cout << "Nothing to resize!" << std::endl;
        for (auto shape : shapes) {
            shape->resize();
        }
    }
};
