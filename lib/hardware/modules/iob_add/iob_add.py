def setup(py_params_dict):
    attributes_dict = {
        "original_name": "iob_add",
        "name": "iob_add",
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
                "name": "N",
                "type": "P",
                "val": "21",
                "min": "NA",
                "max": "NA",
            },
        ],
        "ports": [
            {
                "name": "in1_i",
                "descr": "Input port",
                "signals": [
                    {
                        "name": "in1",
                        "width": "W",
                        "direction": "input",
                    },
                ],
            },
            {
                "name": "sum_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "sum",
                        "width": "W",
                        "direction": "output",
                    },
                ],
            },
            {
                "name": "carry_o",
                "descr": "Output port",
                "signals": [
                    {
                        "name": "carry",
                        "width": 1,
                        "direction": "output",
                    },
                ],
            },
        ],
        "wires": [
            {
                "name": "sum_int",
                "descr": "sum wire",
                "signals": [
                    {"name": "sum_int", "width": "(N-1)*W"},
                ],
            },
        ],
        "blocks": [
            {
                "core_name": "iob_add2",
                "instantiate": False,
            },
        ],
        "snippets": [
            {
                "verilog_code": f"""
        genvar i;

   generate
      //first adder 
      if (N==2) begin: g_N2
         iob_add2 #(.W(W)) 
         adder(
               .in1_i(in_i[0 +: W]),
               .in2_i(in_i[W +: W]),
               .sum_o(sum_o),
               .carry_o(carry_o)
               );
      end else begin: g_N
         iob_add2 #(.W(W)) 
         adder(
               .in1_i(in_i[0 +: W]),
               .in2_i(in_i[W +: (N-1)*W]),
               .sum_o(sum[0 +: (N-1)*W]),
               .carry_o()
               );
      end

      //intermediate adders
      if (N>3) begin: g_Ngt3
         for(i=1; i<(N-1); i=i+1) begin: adder
            iob_add2 #(.W(W)) 
            adder(
                  .in1_i(in_i[i*W +: W]),
                  .in2_i(sum[(i-1)*W +: W]),
                  .sum_o(sum[i*W +: W]),
                  .carry_o()
                  );
         end
      end

      //last adder
      if (N>2) begin: g_Ngt2
      iob_add2 #(.W(W)) 
      adder(
            .in1_i(in_i[(N-1)*W +: W]),
            .in2_i(sum[(N-2)*W +: W]),
            .sum_o(sum_o),
            .carry_o(carry_o)
            );
        end
   endgenerate
         """,
            },
        ],
    }

    return attributes_dict
