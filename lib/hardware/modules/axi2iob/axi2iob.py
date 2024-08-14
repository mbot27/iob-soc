def setup(py_params_dict):
    attributes_dict = {
        "original_name": "axi2iob",
        "name": "axi2iob",
        "version": "0.1",
        "confs": [
            {
                "name": "DATA_WIDTH",
                "type": "P",
                "val": "32",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "ADDR_WIDTH",
                "type": "P",
                "val": "32",
                "min": "NA",
                "max": "NA",
                "descr": "ADDR value",
            },
            {
                "name": "STRB_WIDTH",
                "type": "P",
                "val": "(DATA_WIDTH / 8)",
                "min": "NA",
                "max": "NA",
                "descr": "STRB value",
            },
            {
                "name": "AXI_ID_WIDTH",
                "type": "P",
                "val": "8",
                "min": "NA",
                "max": "NA",
                "descr": "AXI_ID value",
            },
            {
                "name": "AXI_ID_WIDTH",
                "type": "P",
                "val": "8",
                "min": "NA",
                "max": "NA",
                "descr": "AXI_ID value",
            },
            {
                "name": "STATE_IDLE",
                "type": "F",
                "val": "2'd0",
                "min": "NA",
                "max": "NA",
                "descr": "STATE_IDLE value",
            },
            {
                "name": "STATE_DATA",
                "type": "F",
                "val": "2'd1",
                "min": "NA",
                "max": "NA",
                "descr": "STATE_DATA value",
            },
            {
                "name": "STATE_RESP",
                "type": "F",
                "val": "2'd2",
                "min": "NA",
                "max": "NA",
                "descr": "STATE_RESP value",
            },
        ],
        "ports": [
            {
                "name": "s_axi_awid_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awid",
                        "width": "AXI_ID_WIDTH",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awaddr_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awaddr",
                        "width": "ADDR_WIDTH",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awlen_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awlen",
                        "width": 8,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awsize_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awsize",
                        "width": 3,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awburst_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awburst",
                        "width": 2,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awlock_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awlock",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awcache_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awcache",
                        "width": 4,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awprot_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awprot",
                        "width": 3,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awvalid_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_awvalid",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_wdata_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_wdata",
                        "width": "DATA_WIDTH",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_wstrb_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_wstrb",
                        "width": "STRB_WIDTH",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_wlast_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_wlast",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_wvalid_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "s_axi_wvalid",
                        "width": 1,
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "s_axi_awready_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "s_axi_awready",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reg_re",
                "instance_name": "iob_reg_re_inst",
            },
        ],
    }

    return attributes_dict
