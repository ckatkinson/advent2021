
#include <fstream>
#include <iostream>
#include <vector>

std::ifstream infile("../inputs/one.txt");

// Compute the number of increases in vector
int incs(std::vector<int> &lines)
{
    int numInc = 0;
    for (auto i = lines.begin(); i != lines.end() - 1; ++i)
    {
        if (*(i + 1) > *i)
        {
            numInc += 1;
        }
    }
    return numInc;
}

int main()
{
    int line;
    std::vector<int> lines;
    // Collect lines into a vector<int>
    while (infile >> line)
    {
        lines.push_back(line);
    }

    // Part 1:
    int numInc = incs(lines);
    std::cout << "Part 1: " << numInc << std::endl;

    // Part 2:
    std::vector<int> threeSums;
    for (auto i = lines.begin(); i != lines.end() - 2; i++)
    {
        threeSums.push_back( *i + *(i + 1) + *(i + 2) );
    }

    int threeIncs = incs(threeSums);
    std::cout << "Part 2: " << threeIncs << std::endl;

    return 0;
}