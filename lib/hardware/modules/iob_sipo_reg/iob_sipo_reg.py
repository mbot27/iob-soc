def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_sipo_reg",
        "name": "iob_sipo_reg",
        "version": "0.1",
        "confs": [
            {
                "name": "DATA_W",
                "type": "P",
                "val": "21",
                "min": "1",
                "max": "NA",
                "descr": "",
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
                "name": "s_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "p_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "p",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "data_int",
                "descr": "data_int wire",
                "signals": [
                    {"name": "data_int", "width": "DATA_W"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reg",
                "instance_name": "iob_reg_inst",
                "parameters": {
                    "DATA_W": "DATA_W",
                    "RST_VAL": "0",
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "data_i": "data_int",
                    "data_o": "p_o",
                },
            },
        ],
        "snippets": [
            {
                "verilog_code": """
             assign data_int = {p_o[DATA_W-2:0], s_i};
            """,
            },
        ],
    }

    return attributes_dict
