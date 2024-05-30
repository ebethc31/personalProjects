CXX = g++
OPTIONS = -Wall
PROGRAM = project.out

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM) testbinary.bin

$(PROGRAM): project.cpp Controller.cpp Model.cpp View.cpp
	$(CXX) $(OPTIONS) project.cpp Controller.cpp Model.cpp View.cpp -o $(PROGRAM) 

clean:
	rm -f $(PROGRAM)
