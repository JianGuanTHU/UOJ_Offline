#ifndef NEW_SHAPE_H
#define NEW_SHAPE_H

class NewShape {
public:
    virtual double area() = 0;
    virtual double perimeter() = 0;
    virtual void drawShape() = 0;
    virtual std::string description() = 0;
    virtual ~NewShape() {}
};

#endif
