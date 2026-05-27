import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):

    # Start clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize
    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0

    # Reset delay
    await Timer(20, units="ns")

    dut.rst_n.value = 1

    # -------------------------
    # VALID PACKET
    # -------------------------
    dut.ui_in.value = 0x5A

    await Timer(20, units="ns")

    output_val = int(dut.uo_out.value)

    assert (output_val & 0x01) == 1
    assert ((output_val >> 1) & 0x01) == 0

    # -------------------------
    # INVALID PACKET
    # -------------------------
    dut.ui_in.value = 0x12

    await Timer(20, units="ns")

    output_val = int(dut.uo_out.value)

    assert (output_val & 0x01) == 0
    assert ((output_val >> 1) & 0x01) == 1
