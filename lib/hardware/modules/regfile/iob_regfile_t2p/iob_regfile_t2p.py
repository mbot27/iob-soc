def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_regfile_t2p",
        "name": "iob_regfile_t2p",
        "version": "0.1",
        "confs": [
            {
                "name": "DATA_W",
                "type": "P",
                "val": "21",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "ADDR_W",
                "type": "P",
                "val": "3",
                "min": "NA",
                "max": "NA",
                "descr": "ADDR value.",
            },
        ],
        "ports": [
            {
                "name": "w_clk_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "w_clk",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "w_cke_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "w_cke",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "w_arst_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "w_arst",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "w_addr_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "w_addr",
                        "width": "ADDR_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "w_data_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "w_data",
                        "width": "DATA_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "r_clk_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "r_clk",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "r_cke_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "r_cke",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "r_arst_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "r_arst",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "r_addr_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "r_addr",
                        "width": "ADDR_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "r_data_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "r_data",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "regfile_in",
                "descr": "regfile_in wire",
                "signals": [
                    {"name": "regfile_in", "width": "((2**ADDR_W)*DATA_W)"},
                ],
            },
            {
                "name": "regfile_synced",
                "descr": "regfile_synced wire",
                "signals": [
                    {"name": "regfile_synced", "width": "((2**ADDR_W)*DATA_W)"},
                ],
            },
            {
                "name": "regfile_en",
                "descr": "regfile_en wire",
                "signals": [
                    {"name": "regfile_en", "width": "(2**ADDR_W)"},
                ],
            },
            {
                "name": "r_data",
                "descr": "r_data wire",
                "signals": [
                    {"name": "r_data", "width": "DATA_W"},
                ],
            },

        ],
        "blocks": [
            {
                "core_name": "iob_sync",
                "instance_name": "iob_sync_inst",
                
            },
            {
                "core_name": "iob_reg_e",
                "instantiate": False,
            },
        ],
    }

    return attributes_dict
