# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

# use VERILOG_SOURCES for Verilog files
# use VHDL_SOURCES for VHDL files
VHDL_SOURCES += $(PWD)/*.vhd

# seed
RANDOM_SEED=1871423625

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = dff

# MODULE is the basename of the Python test file
# (multiple modules can be specified using a comma-separated list)
MODULE = test_dff_design

RUN_ARGS = --std=08
SIM_ARGS = --wave=waveform.ghw

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

