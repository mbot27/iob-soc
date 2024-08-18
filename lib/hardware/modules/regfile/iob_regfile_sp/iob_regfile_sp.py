def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_regfile_sp",
        "name": "iob_regfile_sp",
        "version": "0.09",
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
                "val": "2",
                "min": "NA",
                "max": "NA",
                "descr": "ADDR value.",
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
                "name": "rst_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "rst",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "we_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "we",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "addr_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "addr",
                        "width": "ADDR_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "d_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "d",
                        "width": "DATA_W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "d_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "d",
                        "width": "DATA_W",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "data_in",
                "descr": "data_in wire",
                "signals": [
                    {"name": "data_in", "width": "DATA_W*(2**ADDR_W)"},
                ],
            },
            {
                "name": "data_out",
                "descr": "data_out wire",
                "signals": [
                    {"name": "data_out", "width": "DATA_W*(2**ADDR_W)"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reg_re",
                "instantiate": False,
            },
        ],
        "snippets": [
            {
                "verilog_code": """
        assign data_in=d_i << (addr_i * DATA_W);
        assign d_o = data_out >> (addr_i * DATA_W);

  genvar i;
  generate
    for (i = 0; i < 2 ** ADDR_W; i = i + 1) begin : g_regfile
      wire reg_en_i = we_i & (addr_i == i);
      iob_reg_re #(
          .DATA_W(DATA_W)
      ) regfile_sp_inst (
          `include "iob_regfile_sp_clk_en_rst_s_s_portmap.vs"
          .rst_i (rst_i),
          .en_i  (reg_en_i),
          .data_i(data_in[DATA_W*(i+1)-1:DATA_W*i]),
          .data_o(data_out[DATA_W*(i+1)-1:DATA_W*i])
      );
    end
  endgenerate
            """,
            },
        ],
    }

    return attributes_dict
