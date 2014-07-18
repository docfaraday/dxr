#include "subclass.h"

DerivedClass::DerivedClass() :
  BaseClass(42) {
}

DerivedClass::~DerivedClass() {}

int DerivedClass::virtual_member_function() {
#ifdef FAKE_IMPL
  return _val;
#else
  return member_function() * member_function();
#endif
}


