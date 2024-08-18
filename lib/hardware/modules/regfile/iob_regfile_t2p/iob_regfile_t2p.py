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
                "name": "r_data_int",
                "descr": "r_data_int wire",
                "signals": [
                    {"name": "r_data_int", "width": "DATA_W"},
                ],
            },
            {
                "name": "sync_int",
                "descr": "sync wire",
                "signals": [
                    {"name": "r_clk"},
                    {"name": "r_arst"},
                ],
            },
            {
                "name": "reg_int",
                "descr": "reg wire",
                "signals": [
                    {"name": "r_clk"},
                    {"name": "r_cke"},
                    {"name": "r_arst"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_sync",
                "instance_name": "iob_sync_regfile_synced",
                "parameters": {
                    "DATA_W": "(2 ** ADDR_W) * DATA_W",
                    "RST_VAL": "{((2 ** ADDR_W) * DATA_W) {1'b0}}",
                },
                "connect": {
                    "clk_rst": "sync_int",
                    "signal_i": "regfile_in",
                    "signal_o": "regfile_synced",
                },
            },
            {
                "core_name": "iob_reg_e",
                "instantiate": False,
            },
            {
                "core_name": "iob_reg",
                "instance_name": "rdata",
                "parameters": {
                    "DATA_W": "DATA_W",
                    "RST_VAL": "{DATA_W{1'd0}}",
                },
                "connect": {
                    "clk_en_rst": "reg_int",
                    "data_i": "r_data_int",
                    "data_o": "r_data_o",
                },
            },
        ],
        "snippets": [
            {
                "verilog_code": """
        assign r_data = regfile_synced[r_addr_i*DATA_W+:DATA_W];
         genvar addr;
   generate
      for (addr = 0; addr < (2 ** ADDR_W); addr = addr + 1) begin : gen_register_file
         assign regfile_en[addr] = (w_addr_i == addr);
         iob_reg_e #(
            .DATA_W (DATA_W),
            .RST_VAL({DATA_W{1'd0}})
         ) rdata (
            .clk_i (w_clk_i),
            .cke_i (w_cke_i),
            .arst_i(w_arst_i),
            .en_i  (regfile_en[addr]),
            .data_i(w_data_i),
            .data_o(regfile_in[addr*DATA_W+:DATA_W])
         );
      end
   endgenerate
            """,
            },
        ],
    }

    return attributes_dict
