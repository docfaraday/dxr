from dxr.testing import DxrInstanceTestCase


class IncrementalUpdateTests(DxrInstanceTestCase):
    """Tests incremental update"""

    def test_refresh_c_function_decl(self):
        """Search for C linkage function"""
        self.found_line_eq('function-decl:c_linkage_function', u'int <b>c_linkage_function</b>();', 12)
        # touch main.cpp
        open('code/main.cpp', 'a').close()
        # rebuild
        self.setup_class()
        # make sure this is still there
        self.found_line_eq('function-decl:c_linkage_function', u'int <b>c_linkage_function</b>();', 12)
