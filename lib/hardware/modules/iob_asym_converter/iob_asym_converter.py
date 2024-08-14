def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_asym_converter",
        "name": "iob_asym_converter",
        "version": "0.1",
        "confs": [
            {
                "name": "W_DATA_W",
                "type": "P",
                "val": "21",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "R_DATA_W",
                "type": "P",
                "val": "21",
                "min": "NA",
                "max": "NA",
                "descr": "R_DATA value.",
            },
            {
                "name": "ADDR_W",
                "type": "P",
                "val": "3",
                "min": "NA",
                "max": "NA",
                "descr": "ADDR value.",
            },
            {
                "name": "MAXDATA_W",
                "type": "P",
                "val": "`IOB_MAX(W_DATA_W, R_DATA_W)",
                "min": "NA",
                "max": "NA",
                "descr": "MAXDATA value.",
            },
            {
                "name": "MINDATA_W",
                "type": "P",
                "val": "`IOB_MIN(W_DATA_W, R_DATA_W)",
                "min": "NA",
                "max": "NA",
                "descr": "MINDATA value.",
            },
            {
                "name": "R",
                "type": "P",
                "val": "MAXDATA_W / MINDATA_W",
                "min": "NA",
                "max": "NA",
                "descr": "R value.",
            },
            {
                "name": "MINADDR_W",
                "type": "P",
                "val": "ADDR_W - $clog2(R)",
                "min": "NA",
                "max": "NA",
                "descr": "MINADDR value.",
            },
            {
                "name": "W_ADDR_W",
                "type": "P",
                "val": "(W_DATA_W == MAXDATA_W) ? MINADDR_W : ADDR_W",
                "min": "NA",
                "max": "NA",
                "descr": "W_ADDR value.",
            },
            {
                "name": "R_ADDR_W",
                "type": "P",
                "val": "(R_DATA_W == MAXDATA_W) ? MINADDR_W : ADDR_W",
                "min": "NA",
                "max": "NA",
                "descr": "R_ADDR value.",
            },
        ],
        "ports": [
            {
                "name": "clk_en_rst",
                "interface": {
                    "type": "clk_en_rst",
                    "subtype": "slave",
                },
                "descr": "Clock, clock enable and reset",
            },
            {
                "name": "rst",
                "descr": "Synchronous reset interface",
                "signals": [
                    {
                        "name": "rst",
                        "direction": "input",
                        "width": 1,
                        "descr": "Synchronous reset input",
                    },
                ],
            },
            {
                "name": "write",
                "descr": "Write interface",
                "signals": [
                    {
                        "name": "w_en",
                        "direction": "input",
                        "width": 1,
                        "descr": "Write enable",
                    },
                    {
                        "name": "w_addr",
                        "direction": "input",
                        "width": "W_ADDR_W",
                        "descr": "Write address",
                    },
                    {
                        "name": "w_data",
                        "direction": "input",
                        "width": "W_DATA_W",
                        "descr": "Write data",
                    },
                ],
            },
            {
                "name": "read",
                "descr": "Read interface",
                "signals": [
                    {
                        "name": "r_en",
                        "direction": "input",
                        "width": 1,
                        "descr": "Read enable",
                    },
                    {
                        "name": "r_addr",
                        "direction": "input",
                        "width": "R_ADDR_W",
                        "descr": "Read address",
                    },
                    {
                        "name": "r_data",
                        "direction": "output",
                        "width": "R_DATA_W",
                        "descr": "Read data",
                    },
                ],
            },
            {
                "name": "extmem",
                "descr": "External memory interface",
                "signals": [
                    #  Write port
                    {
                        "name": "ext_mem_w_en",
                        "direction": "output",
                        "width": "R",
                        "descr": "Memory write enable",
                    },
                    {
                        "name": "ext_mem_w_addr",
                        "direction": "output",
                        "width": "MINADDR_W",
                        "descr": "Memory write address",
                    },
                    {
                        "name": "ext_mem_w_data",
                        "direction": "output",
                        "width": "MAXDATA_W",
                        "descr": "Memory write data",
                    },
                    #  Read port
                    {
                        "name": "ext_mem_r_en",
                        "direction": "output",
                        "width": "R",
                        "descr": "Memory read enable",
                    },
                    {
                        "name": "ext_mem_r_addr",
                        "direction": "output",
                        "width": "MINADDR_W",
                        "descr": "Memory read address",
                    },
                    {
                        "name": "ext_mem_r_data",
                        "direction": "input",
                        "width": "MAXDATA_W",
                        "descr": "Memory read data",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "r_data_reg",
                "descr": "r_data_reg wire",
                "signals": [
                    {"name": "r_data_reg", "width": "MAXDATA_W"},
                ],
            },
            {
                "name": "r_data_int",
                "descr": "r_data_int wire",
                "signals": [
                    {"name": "r_data_int", "width": "MAXDATA_W"},
                ],
            },
            {
                "name": "r_addr_lsbs_reg",
                "descr": "r_addr_lsbs_reg wire",
                "signals": [
                    {"name": "r_addr_lsbs_reg", "width": "$clog2(R)"},
                ],
            },
            {
                "name": "r_data",
                "descr": "r_data wire",
                "signals": [
                    {"name": "r_data", "width": "W_DATA_W"},
                ],
            },
            {
                "name": "r_data_reg",
                "descr": "r_data_reg wire",
                "signals": [
                    {"name": "r_data_reg", "width": "MAXDATA_W"},
                ],
            },
            {
                "name": "r_en_int",
                "descr": "r_en_int wire",
                "signals": [
                    {"name": "r_en", "width": 1},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reg_r",
                "instance_name": "r_data_valid_reg_inst",
                "parameters": {
                    "DATA_W": 1,
                    "RST_VAL": "1'b0",
                },
                "connect": {
                    "rst": "rst",
                    "data_i": "r_en_int",
                    "data_o": "r_data_valid_reg",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "r_data_reg_inst",
                "parameters": {
                    "DATA_W": "MAXDATA_W",
                    "RST_VAL": "{MAXDATA_W{1'd0}}",
                },
                "connect": {
                    "rst": "rst",
                    "data_i": "r_en_int",
                    "data_o": "r_data_valid_reg",
                },
            },
            {
                "core_name": "iob_functions",
                "instance_name": "iob_functions_inst",
            },
        ],
    }

    return attributes_dict
