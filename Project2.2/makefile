CXX = g++
OPTIONS = -Wall
PROGRAM = project2.out

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM) testbinary.bin

$(PROGRAM): project2.cpp Controller.cpp Model.cpp View.cpp
	$(CXX) $(OPTIONS) project2.cpp Controller.cpp Model.cpp View.cpp -o $(PROGRAM) 

clean:
	rm -f $(PROGRAM)