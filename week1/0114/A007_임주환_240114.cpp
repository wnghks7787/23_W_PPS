#include <iostream>
#include <vector>

using namespace std;

#define MAX_SIZE 8

int main()
{
    vector <int> melody(MAX_SIZE);
    bool ascending = true;
    bool descending = true;
    
    for(int i = 0 ; i < MAX_SIZE ; i++)
    {
        cin >> melody[i];

        if(melody[i] != i + 1)
            ascending = false;
        if(melody[i] != 8 - i)
            descending = false;
        
        if(!(ascending || descending))
            break;
    }

    if(ascending)
        cout << "ascending" << endl;
    else if(descending)
        cout << "descending" << endl;
    else
        cout << "mixed" << endl;

    return 0;
}