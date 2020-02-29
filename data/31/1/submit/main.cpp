#include <iostream>
#include "drawing.h"
#include "rectangle.h"
#include "circle.h"
#include "triangle.h"
#include "rhombus.h"
#include "adapter.h"

int main(int argc, char const *argv[])
{
    std::cout << "Creating drawing of shapes..." << std::endl;
    Drawing drawing;
    drawing.addShape(new Rectangle());
    drawing.addShape(new Circle());
    drawing.addShape(new Adapter(new Triangle()));
    drawing.addShape(new Adapter(new Rhombus()));
    std::cout << "Drawing..." << std::endl;
    drawing.draw();
    std::cout << "Resizing..." << std::endl;
    drawing.resize();
    return 0;
}