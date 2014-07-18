#ifndef SUBCLASS
#define SUBCLASS

#include "common_utility_file_included_everywhere.h"

class DerivedClass : public BaseClass {
  public:
    DerivedClass();
    virtual ~DerivedClass();
    virtual int virtual_member_function();
};

#endif

