// Liz Chandler and Christian Nelson

#include "Model.h"

/*Base Code*/
int Model::getRD(){
    return rd;
};

int Model::getRS(){
    return rs;
};

int Model::getRT(){
    return rt;
};

int Model::getAddress(){
    return address;
};

int Model::getNumCycles()
{
    return numOfCycles;
}

int Model::getNumPCUpdates()
{
    return numPCUpdates;
}

int Model::getNumRegisterUpdates()
{
    return numRegisterUpdates;
}

int Model::getNumMemoryUpdates()
{
    return numMemoryUpdates;
}

int Model::getNumALUArithOps()
{
    return numALUArithOps;
}

string Model::getOpcode(){
    return opcode;
};

string Model::getInstrOp(){
    return InstrOp;
};

string Model::getFuncField(){
    return funcField;
};

string Model::getDesiredALU(){
    return desiredALU;
};

vector<int> Model::getPC(){
    return PC;
};

map<string, int> Model::getRegisters(){
    return Registers;
};

map<string, int> Model::getMemory(){
    return Memory;
};

string Model::getBinInstruction(){
    return binInstruction;
};

void Model::updateRD(int x){
    rd = x;
};

void Model::updateRS(int x){
    rs = x;
};

void Model::updateRT(int x){
    rt = x;
};

void Model::updateAddress(int x){
    address = x;
};

void Model::updateBinInstruction(string instruction){
    binInstruction = instruction;
};

void Model::updateOpcode(string newOpcode){
    opcode = newOpcode;
};

void Model::updateInstrOp(string newInstrOp){
    InstrOp = newInstrOp;
};

void Model::updateFuncField(string newFuncFeild){
    funcField = newFuncFeild;
};

void Model::updateDesiredALU(string newDesiredALU){
    desiredALU = newDesiredALU;
};

void Model::updatePC(int newValue){
    PC.push_back(newValue);
};

void Model::updateRegisters(string key, int value){
    Registers[key] = value;
};

void Model::updateMemory(string key, int value){
    Memory.insert({key,value});
    
};

void Model::updateNumCycles()
{
    ++numOfCycles;
}

void Model::updateNumPCUpdates()
{
    ++numPCUpdates;
}

void Model::updateNumRegisterUpdates()
{
    ++numRegisterUpdates;
}

void Model::updateNumMemoryUpdates()
{
    ++numMemoryUpdates;
}

void Model::updateALUArithOps()
{
    ++numALUArithOps;
}

// Decode function
//void decode(Instruction binaryInstr){};


// Execute

// Write to memory 