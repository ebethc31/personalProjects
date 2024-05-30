// Liz Chandler and Christian Nelson

#ifndef MODEL_H
#define MODEL_H

#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <map>
#include <vector>
using namespace std;

class Model{
    // Private Attributes
    private:
        int rd,rs,rt, address, numOfCycles = 0, 
        numPCUpdates = 0, numRegisterUpdates = 0, 
        numMemoryUpdates = 0,
        numALUArithOps = 0;
        std::string binInstruction;
        std::string opcode; // First 6 bits from instruction line
        std::string InstrOp; // Translated opcode to assembly instruction
        std::string funcField; // Last 6 bits from instruction line
        std::string desiredALU; // Translated funcField into assembly instruction

        // Storage parameters
        vector<int> PC;
        map<std::string, int> Registers;
        map<std::string, int> Memory; 
    // Public Functions
    public:
        Model(){
            PC.assign(1, 0x00000000);
            Registers.insert({"R0", 0});
            Registers.insert({"R1", 0}); 
            Registers.insert({"R2", 0}); 
            Registers.insert({"R3", 0}); 
            Registers.insert({"R4", 0}); 
            Registers.insert({"R5", 0}); 
            Registers.insert({"R6", 0});
            Registers.insert({"R7", 0});
            Memory.insert({"0", 0});
            Memory.insert({"1", 0});
            Memory.insert({"2", 5});
            Memory.insert({"3", 0});
            Memory.insert({"4", 6});
        }
        int getRD();
        int getRS();
        int getRT();
        int getAddress();
        int getNumCycles();
        int getNumPCUpdates();
        int getNumRegisterUpdates();
        int getNumMemoryUpdates();
        int getNumALUArithOps();
        std::string getBinInstruction();
        std::string getOpcode();
        std::string getInstrOp();
        std::string getFuncField();
        std::string getDesiredALU();
        vector<int> getPC();
        map<std::string, int> getRegisters();
        map<std::string, int> getMemory(); 
        void updateRD(int);
        void updateRS(int);
        void updateRT(int);
        void updateAddress(int);
        void updateBinInstruction(string);
        void updateOpcode(string);
        void updateInstrOp(string);
        void updateFuncField(string);
        void updateDesiredALU(string);
        void updatePC(int);
        void updateRegisters(string, int);
        void updateMemory(string, int);
        void updateNumCycles();
        void updateNumPCUpdates();
        void updateNumRegisterUpdates();
        void updateNumMemoryUpdates();
        void updateALUArithOps();
};

#endif