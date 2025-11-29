# test_runner.py

import os
from pathlib import Path
from cocotb_tools.runner import get_runner


def run_dff_test():
    sim = os.getenv("SIM", "ghdl")
    proj_path = Path(__file__).resolve().parent

    runner = get_runner(sim)

    runner.build(sources=[proj_path / "dff.vhd"], hdl_toplevel="dff", always=True)

    runner.test(
        hdl_toplevel="dff",
        hdl_toplevel_lang="vhdl",
        test_module="test_dff_design",
        seed=1871423625,
        plusargs=["--wave=waveform.ghw"],
    )


if __name__ == "__main__":
    run_dff_test()

