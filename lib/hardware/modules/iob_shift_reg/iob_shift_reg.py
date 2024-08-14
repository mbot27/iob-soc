def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_shift_reg",
        "name": "iob_shift_reg",
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
                "name": "N",
                "type": "P",
                "val": "21",
                "min": "NA",
                "max": "NA",
                "descr": "",
            },
            {
                "name": "ADDR_W",
                "type": "P",
                "val": "$clog2(N)",
                "min": "NA",
                "max": "NA",
                "descr": "ADDR Width",
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
                "name": "en_rst",
                "descr": "Enable and Synchronous reset interface",
                "signals": [
                    {
                        "name": "en",
                        "direction": "input",
                        "width": 1,
                        "descr": "Enable input",
                    },
                    {
                        "name": "rst",
                        "direction": "input",
                        "width": 1,
                        "descr": "Synchronous reset input",
                    },
                ],
            },
            {
                "name": "data_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "data",
                        "width": "DATA_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "ext_mem_r_data_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "ext_mem_r_data",
                        "width": "DATA_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "data_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "data",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "ext_mem_clk_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "ext_mem_clk",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "ext_mem_w_en_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "ext_mem_w_en",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "ext_mem_w_addr_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "ext_mem_w_addr",
                        "width": "ADDR_W",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "ext_mem_w_data_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "ext_mem_w_data",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "ext_mem_r_en_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "ext_mem_r_en",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "ext_mem_r_addr_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "ext_mem_r_addr",
                        "width": "ADDR_W",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "addr_w",
                "descr": "addr_w wire",
                "signals": [
                    {"name": "addr_w", "width": "ADDR_W"},
                ],
            },
            {
                "name": "addr_r",
                "descr": "addr_r wire",
                "signals": [
                    {"name": "addr_r", "width": "ADDR_W"},
                ],
            },
            {
                "name": "addr_r",
                "descr": "addr_r wire",
                "signals": [
                    {"name": "addr_r", "width": "ADDR_W"},
                ],
            },
            {
                "name": "out_en",
                "descr": "out_en wire",
                "signals": [
                    {"name": "out_en", "width": 1},
                ],
            },
            {
                "name": "out_en_nxt",
                "descr": "out_en_nxt wire",
                "signals": [
                    {"name": "out_en_nxt", "width": 1},
                ],
            },
            {
                "name": "rst_int_w",
                "descr": "rst_int_w wire",
                "signals": [
                    {"name": "rst_int_w", "width": 1},
                ],
            },
            {
                "name": "rst_int_r",
                "descr": "rst_int_r wire",
                "signals": [
                    {"name": "rst_int_r", "width": 1},
                ],
            },
            {
                "name": "shift_reg_int",
                "descr": "shift_reg_int wire",
                "signals": [
                    {"name": "en"},
                    {"name": "rst_int_w"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_counter",
                "instance_name": "iob_counter_inst",
                "parameters": {
                    "DATA_W": "ADDR_W",
                    "RST_VAL": "{ADDR_W{1'd0}}",
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "shift_reg_int",
                    "data_o": "addr_w",
                },
            },
            {
                "core_name": "iob_reg",
                "instance_name": "out_enable",
                "parameters": {
                    "DATA_W": "1",
                    "RST_VAL": "0",
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "data_i": "out_en_nxt",
                    "data_o": "out_en",
                },
            },
            # For simulation
            {
                "core_name": "iob_ram_2p",
                "instantiate": False,
            },
        ],
        "combs": [
            {
                "verilog_code": """
             if (addr_w == (N - 1)) begin
                 addr_r = 0;
            end else begin
            addr_r = addr_w + 1'b1;
            end
            
            """,
            },
        ],
        "snippets": [
            {
                "verilog_code": """
            assign data_o = ext_mem_r_data_i & {DATA_W{out_en}};
            assign ext_mem_clk_o = clk_i;
            assign ext_mem_w_en_o = en_i;
            assign ext_mem_w_addr_o = addr_w;
            assign ext_mem_w_data_o = data_i;
            assign ext_mem_r_en_o = en_i;
            assign ext_mem_r_addr_o = addr_r;
            assign out_en_nxt = out_en | (addr_w == (N - 1));
            assign rst_int_w = rst_i | (addr_w == (N - 1));
            assign rst_int_r = rst_i | (addr_r == (N - 1));
            """,
            },
        ],
    }

    return attributes_dict
