module tt_um_raksha (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire ena,
    input  wire clk,
    input  wire rst_n
);

    wire auth_ok;
    wire alert;

    assign auth_ok = ((ui_in ^ 8'hA5) == 8'hFF);
    assign alert   = ~auth_ok;

    assign uo_out[0] = auth_ok;
    assign uo_out[1] = alert;
    assign uo_out[7:2] = 6'b000000;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

endmodule
