CC=gcc
CC_FLAGS = -O3
SRC=cd.c rot.c my_cat.c headers.c
BIN_DIR=bin


define print_first_arg
	echo $1 
endef

define compile_file
	@echo "comliling file:"$(BIN_DIR)/$(basename $1)
	@$(CC) $(CC_FLAGS) $1 -o $(BIN_DIR)/$(basename $1) 
endef 


all: $(basename $(SRC))

cd: cd.c
	@$(call compile_file,$^)

rot: rot.c
	@$(call compile_file,$^)

my_cat: my_cat.c
	@$(call compile_file,$^)

headers: headers.c
	@$(call compile_file,$^)

clean:
	@echo $(addprefix $(BIN_DIR)/,$(basename $(SRC)))
	@rm -rf $(addprefix $(BIN_DIR)/,$(basename $(SRC)))
