def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_ram_sp_se",
        "name": "iob_ram_sp_se",
        "version": "0.1",
        "generate_hw": False,
        "confs": [
            {
                "name": "HEXFILE",
                "type": "P",
                "val": '"none"',
                "min": "NA",
                "max": "NA",
                "descr": "Name of file to load into RAM",
            },
            {
                "name": "ADDR_W",
                "type": "P",
                "val": "10",
                "min": "0",
                "max": "NA",
                "descr": "Address bus width",
            },
            {
                "name": "DATA_W",
                "type": "P",
                "val": "32",
                "min": "0",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "COL_W",
                "type": "P",
                "val": "8",
                "min": "0",
                "max": "NA",
                "descr": "",
            },
            {
                "name": "NUM_COL",
                "type": "P",
                "val": "DATA_W / COL_W",
                "min": "0",
                "max": "NA",
                "descr": "",
            },
        ],
        "ports": [
            {
                "name": "clk",
                "descr": "Clock",
                "signals": [
                    {"name": "clk", "width": 1, "direction": "input"},
                ],
            },
            {
                "name": "en_i",
                "descr": "Input",
                "signals": [
                    {"name": "en", "width": 1, "direction": "input"},
                ],
            },
            {
                "name": "we_i",
                "descr": "Input",
                "signals": [
                    {"name": "we", "width": "DATA_W/COL_W", "direction": "input"},
                ],
            },
            {
                "name": "addr_i",
                "descr": "Input",
                "signals": [
                    {"name": "addr", "width": "ADDR_W", "direction": "input"},
                ],
            },
            {
                "name": "d_i",
                "descr": "Input",
                "signals": [
                    {"name": "d", "width": "DATA_W", "direction": "input"},
                ],
            },
            {
                "name": "d_o",
                "descr": "Output",
                "signals": [
                    {"name": "d", "width": "DATA_W", "direction": "output"},
                ],
            },
        ],
        "wires": [
            {
                "name": "d_o_int",
                "descr": "d_o_int wire",
                "signals": [
                    {"name": "d_o_int", "width": "DATA_W"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_ram_sp",
                "instantiate": False,
            },
        ],
    }

    return attributes_dict
