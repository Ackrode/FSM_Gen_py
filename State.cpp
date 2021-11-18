#include <iostream>
#include <map>
#include <iterator>
#include <vector>
#include <fstream>
#include "get_states.h"
using namespace std;
#include <bitset>
#include <math.h>


using std::cout; using std::endl;
using std::string; using std::bitset;
string toBinary(int n)
{
    string r;
    while (n != 0){
        r += ( n % 2 == 0 ? "0" : "1" );
        n /= 2;
    }
    return r;
}
float resultado;
int main ()
{
/*iterate into states map*/
    array <map <string, vector <string>>, 2> States;

     States = get_states("state_table.txt");

  vector <vector <string>> States1;
    for(auto it1 = States[0].begin(); it1 != States[0].end(); it1++)
    {
        vector <string> StatesColumns;
            StatesColumns.push_back(it1 -> first);          
            for (auto it2 = it1 -> second.begin(); it2 != it1 -> second.end(); ++it2)
            {
                StatesColumns.push_back(*it2);
            }
        States1.push_back(StatesColumns);
    }


 
/*first map to inputs*/

map<string, vector<string> >inputs;
vector <string> input_values = {"[0:0]"};
inputs.insert({"FSM", input_values});
input_values ={"[0:0]"};
inputs.insert({"clk", input_values});
input_values ={"[0:0]"};
inputs.insert({"reset", input_values});
input_values ={"[0:0]"};
inputs.insert({"x", input_values});

/* second map to outputs*/

map<string, vector<string> >outputs;
vector <string> output_values = {"[0:0]"};
outputs.insert({"outp", output_values});
output_values ={"[0:0]"};


/*iterate into inputs map*/

vector <vector <string>> FSO4;
for (auto it1 = inputs.begin(); it1 != inputs.end(); ++it1)
        {
            vector <string> COL;  
           COL.push_back(it1 -> first);          
            for (auto it2 = it1 -> second.begin(); it2 != it1 -> second.end(); ++it2)
            {
                COL.push_back(*it2);
            }
            FSO4.push_back(COL);
        }
    
/*iterate into outputs map*/

vector <vector <string>> FSO5;
for (auto it3 = outputs.begin(); it3 != outputs.end(); ++it3)
        {
            vector <string> COL;  
           COL.push_back(it3 -> first);          
            for (auto it4 = it3 -> second.begin(); it4 != it3 -> second.end(); ++it4)
            {
                COL.push_back(*it4);
            }
            FSO5.push_back(COL);
        }
    

fstream OL;
/* define the module*/
OL.open("design1.sv", ios::app);
OL << "module" <<" "<< FSO4[0][0] <<"("<< FSO4[2][0] <<", "<< FSO4[1][0] <<", "<< FSO4[3][0] <<  ", "<< FSO5[0][0] <<  ")"<<";"<<endl;
OL << "\t" <<"input" <<" "<< FSO4[0][1]<<" "<< FSO4[2][0]<<", "<< FSO4[1][0]<<", "<<FSO4[3][0]<<";"<<endl;
OL << "\t" <<"output reg" <<" "<<FSO5[0][1]<<" "<< FSO5[0][0]<<";"<<endl;

/* State and next state*/
float x, y; int reg1;    
x = States1.size() ; reg1 = 0;
y = log(x)/log(2);
reg1 = ceil(y);
resultado = reg1 - 1;
OL << "\n" <<endl;
OL << "\t" << "reg ["<<resultado<<":0] state;" << endl;
OL << "\t" << "reg ["<<resultado<< ":0] next_state;" << endl;

/*State codification*/

OL << "\n" <<endl;

for (int i=0; i< States1.size() ; i++)
{
    
    OL <<"\t"<<"parameter"<<" "<< States1[i][0]<<" "<<"="<<i <<";"<<endl;
}


/* intial begin*/
OL << "\n" <<endl;
bitset<3> bs2(toBinary(0)); 
OL << "\t" << "initial begin" << endl;
OL << "\t\t" << "state = "<<States1[0][0] <<";" << endl;
OL << "\t" << "end" << endl;

/*State register*/
OL << "\n" <<endl;
OL << "\t" << "always @("<<"posedge"<<" "<< FSO4[1][0]<<", "<<"posedge"<<" "<<FSO4[2][0]<<")"<<endl;
OL << "\t\t" << "begin" << endl;
OL << "\t\t\t" << "if("<<FSO4[2][0]<<")" << endl;
OL << "\t\t\t\t" << "state <= A;" << endl;
OL << "\t\t\t" << "else" << endl;
OL << "\t\t\t\t" << "state <= next_state;" << endl;
OL << "\t\t" << "end" << endl;

OL.close();

return 0;
}