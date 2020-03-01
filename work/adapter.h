#include <iostream>
#include "new_shape.h"
#include "shape.h"

class Adapter : public Shape {
    NewShape* adaptee;
public:
    Adapter(NewShape* adaptee) {
        this->adaptee = adaptee;
    }
    void draw() {
        adaptee->drawShape();
    }
    void resize() {
        std::cout << description() << " can't be resized. Please create new one with required values." << std::endl;
    }
    std::string description() {
        return adaptee->description();
    }
};
