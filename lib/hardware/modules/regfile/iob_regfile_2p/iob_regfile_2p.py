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
                "val": "(WADDR_W > ($clog2(DATA_W / 8) + 1)) ? WADDR_W : ($clog2(DATA_W / 8) + 1);",
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
                        "width":1,
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
                        "width":"((RADDR_W+WADDR_W)+(WSTRB_W+WDATA_W))",
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

        "blocks": [
            {
                "core_name": "iob_ctls",
                "instance_name": "iob_ctls_inst",
            },
        ],
    }

    return attributes_dict
