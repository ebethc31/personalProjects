Liz Chandler and Christian Nelson

We designed this project using MVC. Using the model as a database to house the pc, registers, and memory values. For the PC we decided to use a vector so that we could dynamically add new values after each cycle. Registers and Memory were implemented as ordered maps. This was done so we could easily access the values using a key and also add key values dynamically.
We used the controller to decode the binary read in from the binary file. This was done by using an instance of model in the controller function decode.
The decode function broke down the instruction and ALU type as well as registers and immediate values.
Then the execute function used the same instance of the model class to later take those translated instructions and manipulate the PC, registers, and memory.
View is called by Controller in order to display the most recent set of stats.
The stats that the View displays are logic block stats (number of cycles, number of PC updates, number of register updates, number of memory updates, and number of ALU arithmetic operations), PC information, Register information (7 registers), and Memory information.
Controller passses in an instance of Model for each statistic being printed, so that View can use Model getter functions to print accurate information about what's supposed to be printed.
