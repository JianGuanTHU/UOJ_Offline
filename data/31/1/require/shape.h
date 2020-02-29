#ifndef SHAPE_H
#define SHAPE_H

class Shape {
public:
    virtual void draw() = 0;
    virtual void resize() = 0;
    virtual std::string description() = 0;
    virtual ~Shape() {}
};

#endif
