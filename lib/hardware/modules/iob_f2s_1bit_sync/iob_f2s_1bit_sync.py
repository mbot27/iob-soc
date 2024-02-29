import os

from iob_module import iob_module

from iob_reg import iob_reg


class iob_f2s_1bit_sync(iob_module):
    def __init__(self):
        super().__init__()
        self.version = "V0.10"
        self.submodule_list = [
            iob_reg(),
        ]