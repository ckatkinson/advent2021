#include <iostream>
#include <fstream>
#include <string>

using std::cout;
using std::string;

struct Sub
{
    int position, depth;
};

enum string_code
{
    cForward,
    cDown,
    cUp
};

string_code encode(string inString)
{
    if (inString == "forward")
        return cForward;
    if (inString == "down")
        return cDown;
    if (inString == "up")
        return cUp;
}

int main()
{
    std::ifstream infile("../inputs/two.txt");
    struct Sub sub;
    sub.position = 0;
    sub.depth = 0;
    string direction;
    int amount;
    while (infile >> direction >> amount)
    {
        switch (encode(direction))
        {
        case cForward:
            sub.position += amount;
            break;
        case cDown:
            sub.depth += amount;
            break;
        case cUp:
            sub.depth -= amount;
            break;
        default:
            break;
        }
    };
    cout << "Part 1 " << (sub.depth * sub.position) << std::endl;
    return 0;
    /* Skipping part 2 for now. This is a learning exercise for me and I won't learn any more C++ by doing part 2. Just add aim to sub and adjust movement */
};
