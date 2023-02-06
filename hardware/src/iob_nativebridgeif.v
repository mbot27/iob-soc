`timescale 1ns/1ps
`include "iob_lib.vh"
`include "iob_nativebridgeif_conf.vh"
`include "iob_nativebridgeif_swreg_def.vh"

module iob_nativebridgeif # (
     `include "iob_nativebridgeif_params.vh"
   ) (
     `include "iob_nativebridgeif_io.vh"
   );

    // Connect interfaces
    assign iob_avalid_o = iob_avalid_i;
    assign iob_addr_o = iob_addr_i;
    assign iob_wdata_o = iob_wdata_i;
    assign iob_wstrb_o = iob_wstrb_i;
    assign iob_rdata_o = iob_rdata_i;
    assign iob_ready_o = iob_ready_i;

endmodule
    
