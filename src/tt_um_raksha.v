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

    parameter SECRET_KEY = 8'hA5;

    reg auth_ok;
    reg alert;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            auth_ok <= 1'b0;
            alert <= 1'b0;
        end
        else begin

            // Packet Authentication Logic
            if ((ui_in ^ SECRET_KEY) == 8'hFF) begin
                auth_ok <= 1'b1;
                alert <= 1'b0;
            end
            else begin
                auth_ok <= 1'b0;
                alert <= 1'b1;
            end
        end
    end

    // Outputs
    assign uo_out[0] = auth_ok;
    assign uo_out[1] = alert;
    assign uo_out[7:2] = 6'b000000;

    // Unused bidirectional IO
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

endmodule
