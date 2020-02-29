#include <iostream>
#include "drawing.h"
#include "rectangle.h"
#include "circle.h"
#include "triangle.h"
#include "rhombus.h"

int main(int argc, char const *argv[])
{
    std::cout << "Creating drawing of shapes..." << std::endl;
    Drawing drawing;
    Rectangle* rectangle = new Rectangle();
    Circle* circle = new Circle();
    Triangle* triangle = new Triangle();
    Rhombus* rhombus = new Rhombus();
    drawing.addShape(rectangle);
    drawing.addShape(circle);
    drawing.addShape(triangle);
    drawing.addShape(rhombus);
    std::cout << "Drawing..." << std::endl;
    drawing.draw();
    std::cout << "Resizing..." << std::endl;
    drawing.resize();
    delete rectangle;
    delete circle;
    delete triangle;
    delete rhombus;
    return 0;
}