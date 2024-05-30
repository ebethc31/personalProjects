// Liz Chandler and Christian Nelson

#include "View.h"
#include "Model.h"
#include "Controller.h"
#include <iostream>
#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
#include <fstream>
#include <stdlib.h>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[])
{
    fstream inFile(argv[1]);
    string binaryLine;
    Model m;
    View v;
    Controller c(m,v);

    while(getline(inFile, binaryLine))
    {
        c.decode(binaryLine);
        c.execute();
        binaryLine.clear();
    }

    inFile.close();
    
    return 0;
}
