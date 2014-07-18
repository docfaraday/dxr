#ifndef NOT_LIKELY
#define NOT_LIKELY

#include <stdlib.h>

/* Some simple macros */
#define TRUE 1
#define FALSE 0

/* c linkage function decl */
extern "C" {
int c_linkage_function();
}

typedef size_t simple_typedef;

class BaseClass {
  public:
    BaseClass(simple_typedef val) : _val(val) {}

    virtual ~BaseClass() {}

    int member_function() {
      if (c_linkage_function()) {
        return FALSE;
      } else {
        return TRUE;
      }
    }

    virtual int virtual_member_function() = 0;

    simple_typedef _val;
};

#endif

