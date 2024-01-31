#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int c;

    cin >> c;

    for(int i = 0 ; i < c ; i++)
    {
        int n;
        int sum = 0;
        int count = 0;
        double avg;
        double percentage;
        cin >> n;

        vector <int> students(n);
    

        for(int j = 0 ; j < n ; j++)
        {
            cin >> students[j];
            sum += students[j];
        }
        avg = sum / (double)n;

        for(int j = 0 ; j < n ; j++)
            if(students[j] > avg)
                count++;

        percentage = (double)count / students.size() * 100;
        printf("%.3f%\n", percentage);
    }

    return 0;
}