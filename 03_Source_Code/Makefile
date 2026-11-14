# PHANToM GRID :: Makefile for QNX SDP 8.0 & Host Toolchain
CXX ?= g++
CXXFLAGS ?= -O3 -std=c++17 -Wall -Wextra -pthread

TARGET = qnx_motion_kernel
SRC = qnx_motion_kernel.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET) *.o

run: $(TARGET)
	./$(TARGET)
