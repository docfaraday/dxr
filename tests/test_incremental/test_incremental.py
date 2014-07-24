from dxr.testing import DxrInstanceTestCase
import os


class IncrementalUpdateTests(DxrInstanceTestCase):
    """Tests incremental update"""

    def test_refresh_c_function_decl(self):
        """Search for C linkage function"""
        self.found_line_eq('function-decl:c_linkage_function', u'int <b>c_linkage_function</b>();', 12)
        self.touch_and_rebuild('code/main.cpp')
        # make sure this is still there
        self.found_line_eq('function-decl:c_linkage_function', u'int <b>c_linkage_function</b>();', 12)

    def test_function_ref_when_def_updated(self):
        self.found_line_eq('function-ref:c_linkage_function', u'if (<b>c_linkage_function</b>()) {', 4)
        # touch main.cpp, which defines virtual_member_function. The ref above
        # is in baseclass.cpp, which is not recompiled when main.cpp is touched.
        # The ref should not be pruned when this happens.
        self.touch_and_rebuild('code/main.cpp')
        self.found_line_eq('function-ref:c_linkage_function', u'if (<b>c_linkage_function</b>()) {', 4)
