def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_iob2wishbone",
        "name": "iob_iob2wishbone",
        "version": "0.1",
        "confs": [
            {
                "name": "DATA_W",
                "type": "P",
                "val": "32",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "ADDR_W",
                "type": "P",
                "val": "32",
                "min": "NA",
                "max": "NA",
                "descr": "ADDR value.",
            },
            {
                "name": "READ_BYTES",
                "type": "P",
                "val": "4",
                "min": "NA",
                "max": "NA",
                "descr": "READ_BYTES value.",
            },
            {
                "name": "RB_MASK",
                "type": "F",
                "val": "{1'b0, {READ_BYTES{1'b1}}}",
                "min": "NA",
                "max": "NA",
                "descr": "READ_BYTES value.",
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
                "name": "iob_valid_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "iob_valid",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "iob_addr_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "iob_addr",
                        "width": "ADDR_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "iob_wdata_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "iob_wdata",
                        "width": "DATA_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "iob_wstrb_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "iob_wstrb",
                        "width": "DATA_W/8",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "wb_ack_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "wb_ack",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "wb_data_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "wb_data",
                        "width": "DATA_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "iob_rvalid_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "iob_rvalid",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "iob_rdata_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "iob_rdata",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "iob_ready_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "iob_ready",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "wb_addr_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "wb_addr",
                        "width": "ADDR_W",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "wb_select_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "wb_select",
                        "width": "DATA_W/8",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "wb_we_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "wb_we",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "wb_cyc_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "wb_cyc",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "wb_stb_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "wb_stb",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "wb_data_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "wb_data",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "iob_valid_r",
                "descr": "iob_valid_r wire",
                "signals": [
                    {"name": "iob_valid_r", "width": 1},
                ],
            },
            {
                "name": "iob_address_r",
                "descr": "iob_address_r wire",
                "signals": [
                    {"name": "iob_address_r", "width": "ADDR_W"},
                ],
            },
            {
                "name": "iob_wdata_r",
                "descr": "iob_wdata_r wire",
                "signals": [
                    {"name": "iob_wdata_r", "width": "DATA_W"},
                ],
            },
            {
                "name": "wb_data_r",
                "descr": "wb_data_r wire",
                "signals": [
                    {"name": "wb_data_r", "width": "DATA_W"},
                ],
            },
            {
                "name": "wb_select",
                "descr": "wb_select wire",
                "signals": [
                    {"name": "wb_select_int", "width": "DATA_W/8"},
                ],
            },
            {
                "name": "wb_select_r",
                "descr": "wb_select_r wire",
                "signals": [
                    {"name": "wb_select_r", "width": "DATA_W/8"},
                ],
            },
            {
                "name": "wb_we",
                "descr": "wb_we wire",
                "signals": [
                    {"name": "wb_we_int", "width": 1},
                ],
            },
            {
                "name": "wb_we_r",
                "descr": "wb_we_r wire",
                "signals": [
                    {"name": "wb_we_r", "width": 1},
                ],
            },
            {
                "name": "wb_ack_r",
                "descr": "wb_ack_r wire",
                "signals": [
                    {"name": "wb_ack_r", "width": 1},
                ],
            },
            {
                "name": "iob2wishbone_int",
                "descr": "iob2wishbone wire",
                "signals": [
                    {"name": "wb_ack"},
                    {"name": "iob_valid"},
                ],
            },
            {
                "name": "iob2wishbone2_int",
                "descr": "iob2wishbone2 wire",
                "signals": [
                    {"name": "iob2wishbone2"},
                    {"name": "iob_valid"},
                ],
            },
            {
                "name": "iob2wishbone3_int",
                "descr": "iob2wishbone3 wire",
                "signals": [
                    {"name": "iob2wishbone2"},
                    {"name": "iob2wishbone3"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_valid",
                "parameters": {
                    "DATA_W": 1,
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone_int",
                    "data_i": "iob_valid_i",
                    "data_o": "iob_valid_r",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_addr",
                "parameters": {
                    "DATA_W": "ADDR_W",
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone2_int",
                    "data_i": "iob_addr_i",
                    "data_o": "iob_address_r",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_iob_data",
                "parameters": {
                    "DATA_W": "DATA_W",
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone2_int",
                    "data_i": "iob_wdata_i",
                    "data_o": "iob_wdata_r",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_we",
                "parameters": {
                    "DATA_W": 1,
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone2_int",
                    "data_i": "wb_we",
                    "data_o": "wb_we_r",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_strb",
                "parameters": {
                    "DATA_W": "DATA_W / 8",
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone2_int",
                    "data_i": "wb_select",
                    "data_o": "wb_select_r",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_wb_data",
                "parameters": {
                    "DATA_W": "DATA_W",
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone3_int",
                    "data_i": "wb_data_i",
                    "data_o": "wb_data_r",
                },
            },
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_wb_ack",
                "parameters": {
                    "DATA_W": 1,
                    "RST_VAL": 0,
                },
                "connect": {
                    "clk_en_rst": "clk_en_rst",
                    "en_rst": "iob2wishbone3_int",
                    "data_i": "wb_ack_i",
                    "data_o": "wb_ack_r",
                },
            },
        ],
        "snippets": [
            {
                "verilog_code": """
        assign iob2wishbone2=1'b0;
        assign iob2wishbone3=1'b1;
        assign wb_addr_o   = iob_valid_i ? iob_addr_i : iob_address_r;
        assign wb_data_o   = iob_valid_i ? iob_wdata_i : iob_wdata_r;
        assign wb_select_o = iob_valid_i ? wb_select_int : wb_select_r;
        assign wb_we_o     = iob_valid_i ? wb_we_int : wb_we_r;
        assign wb_cyc_o    = iob_valid_i ? iob_valid_i : iob_valid_r;
        assign wb_stb_o    = wb_cyc_o;
        assign wb_select_int   = wb_we_int ? iob_wstrb_i : (RB_MASK) << (iob_addr_i[1:0]);
        assign wb_we_int       = |iob_wstrb_i;
        assign iob_rvalid_o = wb_ack_r & (~wb_we_r);
        assign iob_rdata_o  = wb_ack_i ? wb_data_i : wb_data_r;
        assign iob_ready_o  = (~iob_valid_r) | wb_ack_r;
        
            """,
            },
        ],
    }

    return attributes_dict
