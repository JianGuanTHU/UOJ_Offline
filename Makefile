INCLUDE_PATH = include
CXXFLAGS = -I./include -O2

EXE_CHECKER = \
	builtin/checker/bcmp \
	builtin/checker/acmp \
	builtin/checker/caseicmp \
	builtin/checker/casencmp \
	builtin/checker/casewcmp \
	builtin/checker/dcmp \
	builtin/checker/fcmp \
	builtin/checker/hcmp \
	builtin/checker/icmp \
	builtin/checker/lcmp \
	builtin/checker/ncmp \
	builtin/checker/rcmp \
	builtin/checker/rcmp4 \
	builtin/checker/rcmp6 \
	builtin/checker/rcmp9 \
	builtin/checker/rncmp \
	builtin/checker/uncmp \
	builtin/checker/wcmp \
	builtin/checker/yesno

EXE = $(EXE_CHECKER)

all: $(EXE)

% : %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

$(EXE_CHECKER): include/testlib.h

clean:
	rm -f $(EXE)
