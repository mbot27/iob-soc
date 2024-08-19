def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_regfile_2p",
        "name": "iob_regfile_2p",
        "version": "0.1",
        "confs": [
            {
                "name": "DATA_W",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "N",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "N width",
            },
            {
                "name": "W",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "W width",
            },
            {
                "name": "WDATA_W",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "WDATA_W width",
            },
            {
                "name": "WADDR_W",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "WADDR_W width",
            },
            {
                "name": "RDATA_W",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "RDATA_W width",
            },
            {
                "name": "RADDR_W",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "RADDR_W width",
            },
            {
                "name": "WSTRB_W",
                "type": "P",
                "val": "WDATA_W / 8 ",
                "min": "NA",
                "max": "NA",
                "descr": "WSTRB_W width",
            },
            {
                "name": "WADDR_INT_W",
                "type": "F",
                "val": "(WADDR_W > ($clog2(DATA_W / 8) + 1)) ? WADDR_W : ($clog2(DATA_W / 8) + 1)",
                "min": "NA",
                "max": "NA",
                "descr": "WADDR_INT width",
            },
            {
                "name": "LAST_I",
                "type": "F",
                "val": "(N / WSTRB_W) * WSTRB_W",
                "min": "NA",
                "max": "NA",
                "descr": "LAST_I width",
            },
            {
                "name": "REM_I",
                "type": "F",
                "val": "(N - LAST_I) + 1",
                "min": "NA",
                "max": "NA",
                "descr": "REM_I width",
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
                "name": "wen_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "wen",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "req_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "req_i",
                        "width": "((RADDR_W+WADDR_W)+(WSTRB_W+WDATA_W))",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "resp_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "resp",
                        "width": "RDATA_W",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "regfile",
                "descr": "regfile wire",
                "signals": [
                    {"name": "regfile", "width": "(N*W)"},
                ],
            },
            {
                "name": "wen_int",
                "descr": "wen_int wire",
                "signals": [
                    {"name": "wen_int", "width": "N"},
                ],
            },
            {
                "name": "wstrb",
                "descr": "wstrb wire",
                "signals": [
                    {"name": "wstrb", "width": "WSTRB_W"},
                ],
            },
            {
                "name": "waddr",
                "descr": "waddr wire",
                "signals": [
                    {"name": "waddr", "width": "WADDR_W"},
                ],
            },
            {
                "name": "waddr_incr",
                "descr": "waddr_incr wire",
                "signals": [
                    {"name": "waddr_incr", "width": "($clog2(DATA_W/8)+1)"},
                ],
            },
            {
                "name": "waddr_int",
                "descr": "waddr_int wire",
                "signals": [
                    {"name": "waddr_int", "width": "WADDR_INT_W"},
                ],
            },
            {
                "name": "wdata_int",
                "descr": "wdata_int wire",
                "signals": [
                    {"name": "wdata_int", "width": "WDATA_W"},
                ],
            },
            {
                "name": "row_sel",
                "descr": "row_sel wire",
                "signals": [
                    {"name": "row_sel", "width": 1},
                ],
            },
            {
                "name": "col_sel",
                "descr": "col_sel wire",
                "signals": [
                    {"name": "col_sel", "width": 1},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_ctls",
                "instance_name": "iob_ctls_txinst",
                "parameters": {
                    "W": "DATA_W/8",
                    "MODE": "0",
                    "SYMBOL": "0",
                },
                "connect": {
                    "data_i": "wstrb",
                    "count_o": "waddr_incr",
                },
            },
            {
                "core_name": "iob_reg_e",
                "instantiate": False,
            },
        ],
        "snippets": [
            {
                "verilog_code": """
    assign wstrb = req_i[WDATA_W+:WSTRB_W];
    assign waddr = req_i[WSTRB_W+WDATA_W+:WADDR_W];
    assign waddr_int = waddr + waddr_incr;
    assign  wdata_int = req_i[WDATA_W-1:0];
     genvar row_sel;
     genvar col_sel;
    generate
    for (row_sel = 0; row_sel < N; row_sel = row_sel + WSTRB_W) begin : g_rows
      for (
          col_sel = 0; col_sel < ((row_sel == LAST_I) ? REM_I : WSTRB_W); col_sel = col_sel + 1
      ) begin : g_columns
        if ((row_sel + col_sel) < N) begin : g_if
          assign wen_int[row_sel+col_sel] = wen_i & (waddr_int == (row_sel + col_sel)) & wstrb[col_sel];
          iob_reg_e #(
              .DATA_W (W),
              .RST_VAL({W{1'b0}})
          ) iob_reg_inst (
              `include "iob_regfile_2p_clk_en_rst_s_s_portmap.vs"
              .en_i  (wen[row_sel+col_sel]),
              .data_i(wdata_int[(col_sel*8)+:W]),
              .data_o(regfile[(row_sel+col_sel)*W+:W])
          );
        end
      end
    end
  endgenerate

  //read register file
  generate
    if (RADDR_W > 0) begin : g_read
      wire [RADDR_W-1:0] raddr = req_i[(WSTRB_W+WDATA_W)+WADDR_W+:RADDR_W];
      assign resp_o = regfile[RDATA_W*raddr+:RDATA_W];
    end else begin : g_read
      assign resp_o = regfile;
    end
  endgenerate
    
         """,
            },
        ],
    }

    return attributes_dict
