export INCLUDE_PATH
CXXFLAGS = -I$(INCLUDE_PATH) -O2

all: judger

% : %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@
