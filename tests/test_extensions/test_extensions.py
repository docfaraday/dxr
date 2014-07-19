from dxr.testing import DxrInstanceTestCase


class FileExtensionsTests(DxrInstanceTestCase):
    """Tests searching for files by extension"""

    def test_extensions(self):
        """Try search by filename extension."""
        self.found_files_eq('ext:c', ['main.c', 'dot_c.c'])
        self.found_files_eq('ext:cpp', ['hello-world.cpp'])
        self.found_files_eq('ext:inc', ['hello-world.inc'])

    def test_extensions_formatting(self):
        """Extensions can be preceeded by a dot"""
        self.found_files_eq('ext:.c', ['main.c', 'dot_c.c'])

    def test_incremental(self):
        for file in ['code/main.c','code/hello-world.cpp','code/hello-world.inc','code/dot_c.c']:
            self.touch_and_rebuild(file)
            self.test_extensions()
            self.test_extensions_formatting()

