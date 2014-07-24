#include "baseclass.h"

#include "subclass.h"

#include <stdio.h>

extern "C" {
int c_linkage_function() {
  unsigned int input;
  int res = scanf("%u", &input);
  if (!res) {
    return -1;
  } else {
    return res;
  }
}
}

int main() {
  DerivedClass subclass;
  return subclass.virtual_member_function();
}

