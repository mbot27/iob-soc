#
# TOP MAKEFILE
#
UART_DIR:=.
include core.mk

#
# SIMULATE
#

sim:
	make -C $(SIM_DIR) run

sim-waves: $(SIM_DIR)/waves.gtkw $(SIM_DIR)/uart.vcd
	gtkwave -a $^ &

$(SIM_DIR)/uart.vcd:
	make -C $(SIM_DIR) run VCD=1

sim-clean:
	make -C $(SIM_DIR) clean

#
# FPGA COMPILE
#

fpga-build:
	make -C $(FPGA_DIR) build

fpga-build-all:
	$(foreach s, $(FPGA_FAMILY_LIST), make fpga-build FPGA_FAMILY=$s;)

fpga-clean:
	make -C $(FPGA_DIR) clean

fpga-clean-all:
	$(foreach s, $(FPGA_FAMILY_LIST), make fpga-clean FPGA_FAMILY=$s;)


#
# DOCUMENT
#

doc-build: fpga-build-all
	make -C $(DOC_DIR) $(DOC_TYPE).pdf

doc-build-all:
	$(foreach s, $(DOC_LIST), make doc-build DOC_TYPE=$s;)


doc-clean:
	make -C $(DOC_DIR) clean

doc-clean-all:
	$(foreach s, $(DOC_LIST), make doc-clean DOC_TYPE=$s;)


#
# CLEAN ALL
# 

clean: sim-clean fpga-clean fpga-clean-all doc-clean doc-clean-all 

.PHONY: sim sim-waves fpga-build fpga-build-all fpga-clean doc-build doc-build-all doc-clean doc-clean-all clean

