import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_project(dut):

    # Start clock
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Initial values
    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0

    # Reset
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1

    # -----------------------------
    # VALID PACKET TEST
    # -----------------------------
    dut.ui_in.value = 0x5A

    await RisingEdge(dut.clk)

    auth_ok = int(dut.uo_out.value) & 0x01
    alert   = (int(dut.uo_out.value) >> 1) & 0x01

    assert auth_ok == 1
    assert alert == 0

    # -----------------------------
    # INVALID PACKET TEST
    # -----------------------------
    dut.ui_in.value = 0x12

    await RisingEdge(dut.clk)

    auth_ok = int(dut.uo_out.value) & 0x01
    alert   = (int(dut.uo_out.value) >> 1) & 0x01

    assert auth_ok == 0
    assert alert == 1
