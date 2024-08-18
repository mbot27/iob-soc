def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_ctls",
        "name": "iob_ctls",
        "version": "0.1",
        "confs": [
            {
                "name": "W",
                "type": "P",
                "val": "21",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "MODE",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "",
            },
            {
                "name": "SYMBOL",
                "type": "P",
                "val": "0",
                "min": "NA",
                "max": "NA",
                "descr": "",
            },
        ],
        "ports": [
            {
                "name": "data_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "data",
                        "width": "W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "count_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "count",
                        "width": "$clog2(W)+1",
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "data_int1",
                "descr": "data wire",
                "signals": [
                    {"name": "data_int1", "width": "W"},
                ],
            },
            {
                "name": "data_int2",
                "descr": "data wire",
                "signals": [
                    {"name": "data_int2", "width": "W"},
                ],
            },
            {
                "name": "data_int3",
                "descr": "data wire",
                "signals": [
                    {"name": "data_int3", "width": "W"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_reverse",
                "instantiate": False,
            },
            {
                "core_name": "iob_prio_enc",
                "instance_name": "prio_encoder0",
                "parameters": {
                    "W": "W+1",
                    "MODE": '"LOW"',
                },
                "connect": {
                    "unencoded_i": "data_int3",
                    "encoded_o": "count_o",
                },
            },
        ],
        "snippets": [
            {
                "verilog_code": """
    assign data_int3={1'b1, data_int2};
    generate
      if (SYMBOL == 0) begin : g_zeros
         assign data_int1 = data_i;
      end else begin : g_ones
         assign data_int1 = ~data_i;
      end
   endgenerate

    generate
      if (MODE == 1) begin : g_reverse
         iob_reverse #(W) reverse0 (
            .data_i(data_int1),
            .data_o(data_int2)
         );
      end else begin : g_noreverse
         assign data_int2 = data_int1;
      end
   endgenerate
         """,
            },
        ],
    }

    return attributes_dict
