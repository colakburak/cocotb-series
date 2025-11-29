import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ReadOnly


@cocotb.test()
async def test_dff(dut):
    cocotb.start_soon(Clock(dut.clk, 10, "ns").start())

    # === RESET ===
    dut.reset_n.value = 0
    dut.d.value = 0

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.reset_n.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()  # Somehow without this the value read is incorrect, we read too early?
    assert dut.q.value == 0, f"Q should be 0 after reset, got {dut.q.value}"

    # === TEST D=1 ===
    await FallingEdge(dut.clk)
    dut.d.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert dut.q.value == 1, f"Q should capture D=1, got {dut.q.value}"

    # === TEST D=0 ===
    await FallingEdge(dut.clk)
    dut.d.value = 0
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert dut.q.value == 0, f"Q should capture D=0, got {dut.q.value}"
