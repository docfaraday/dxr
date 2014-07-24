#ifndef SUBCLASS
#define SUBCLASS

#include "baseclass.h"

class DerivedClass : public BaseClass {
  public:
    DerivedClass();
    virtual ~DerivedClass();
    virtual int virtual_member_function();
};

#endif

