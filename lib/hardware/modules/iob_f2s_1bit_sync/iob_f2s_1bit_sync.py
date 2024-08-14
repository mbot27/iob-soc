def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_f2s_1bit_sync",
        "name": "iob_f2s_1bit_sync",
        "version": "0.1",
        "ports": [
            {
                "name": "clk_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "clk",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "cke_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "cke",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "value_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "value",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "value_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "value",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "sync",
                "descr": "sync wire",
                "signals": [
                    {"name": "sync", "width": 2},
                ],
            },
            {
                "name": "data_int",
                "descr": "data_int wire",
                "signals": [
                    {"name": "data_int", "width": 2},
                ],
            },
            {
                "name": "int",
                "descr": "int wire",
                "signals": [
                    {"name": "clk"},
                    {"name": "cke"},
                    {"name": "value"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reg",
                "instance_name": "reg0",
                "parameters": {
                    "DATA_W": "2",
                    "RST_VAL": "1",
                },
                "connect": {
                    "clk_en_rst": "int",
                    "data_i": "data_int",
                    "data_o": "sync",
                },
            },
        ],
        "snippets": [
            {
                "verilog_code": """
            assign data_int = {sync[0], 1'b0};
            assign value_o = sync[1];
            """,
            },
        ],
    }

    return attributes_dict
