### another question, c++ use python function
从statsmodels.tsa.stattools调用adfuller实现adf检验

### 实现过程
1. 编写my_adf.pyx, setup.py，实现需要的函数
2. 编写my_adf.h，把python函数转化成c++函数
3. 编写main.cpp, 调用my_adf函数

### 编译

在windows上编译运行，注意需要替换自己的python路径才能编译成功
```
// 编译出来pyd文件
python setup.py build_ext --inplace
// 编译main.cpp
g++ main.cpp -Ic:/anaconda3/include  -Lc:/anaconda3/libs -lpython311 -o main
// 运行main
./main
```
在macos上进行编译,需要根据自己的机器，修改具体的python路径
```
// 编译出来pyd文件
python setup.py build_ext --inplace
// 编译main.cpp
g++ main.cpp -I$(python3-config --includes) -L/Users/yunjinqi/opt/anaconda3/lib -lpython3.11 -o main --std=c++11 -Wl,-rpath,/Users/yunjinqi/opt/anaconda3/lib
// 运行main
./main
```

在ubuntu上进行编译
```
// 编译出来pyd文件
python setup.py build_ext --inplace
//设置 LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/yun/anaconda3/lib:$LD_LIBRARY_PATH
// 编译main.cpp
g++ main.cpp -I$(python3-config --includes) -L$(python3-config --prefix)/lib -lpython3.11 -o main
// 运行main
./main
```





### the answer of first question

When running the source code, an error occurs, 
and it doesn't run successfully. The Derived class has some errors when I run `Base *b = new Derived();`. 
When inheriting from Base, the public keyword needs to be used. 
After making this change, there are still some memory leak issues. 
When running on macOS, it outputs 'D' followed by random garbled 
characters, while on Windows, it outputs 'D'.

### the answer of second question 

```
#include <iostream>
#include <map>

int main() {
    // Define the input array
    int arr[] = {4, 6, 5, 3, 2, 7, 6, 5};
    // Create a map to store occurrences
    std::map<int, int> myMap;
    // Count the occurrences of each number
    for (int num : arr) {
        myMap[num]++;
    }
    for (auto p : myMap) {
        std::cout << p.first << " -> " << p.second << std::endl;
    }
    return 0;
}
```

### the answer of third question

```
#include <iostream>
#include <stack>
#include <string>

bool isValid(std::string s) {
    std::stack<char> stack;

    // Traverse through each character in the string
    for (char c : s) {
        // If it's an opening bracket, push to the stack
        if (c == '(' || c == '[') {
            stack.push(c);
        }
            // If it's a closing bracket, check if it matches the top of the stack
        else if (c == ')') {
            if (!stack.empty() && stack.top() == '(') {
                stack.pop();
            } else {
                return false;
            }
        } else if (c == ']') {
            if (!stack.empty() && stack.top() == '[') {
                stack.pop();
            } else {
                return false;
            }
        }
    }

    // If the stack is empty, all opening brackets have been matched
    return stack.empty();
}

int main() {
    std::string s = "([()])";  // Example input

    if (isValid(s)) {
        std::cout << "s is valid.\n";
    } else {
        std::cout << "s is not valid.\n";
    }
    std::string s1 = "([())";  // Example input

    if (isValid(s1)) {
        std::cout << "s1 is valid.\n";
    } else {
        std::cout << "s1 is not valid.\n";
    }

    std::string s2 = "test";  // Example input

    if (isValid(s2)) {
        std::cout << "s2 is valid.\n";
    } else {
        std::cout << "s2 is not valid.\n";
    }

    return 0;
}
```

### the answer of question four
```
#include <iostream>
#include <vector>
#include <limits>

void findTwoLargest(const std::vector<int>& arr, int& first_max, int& second_max) {
    // Initialize first_max and second_max with minimum possible values
    first_max = std::numeric_limits<int>::min();
    second_max = std::numeric_limits<int>::min();

    // Traverse the array to find the two largest numbers
    for (int num : arr) {
        if (num > first_max) {
            second_max = first_max;  // Update second_max before updating first_max
            first_max = num;
        } else if (num > second_max) {
            second_max = num;
        }
    }
}

int main() {
    // Example input
    std::vector<int> arr = {4, 6, 5, 3, 2, 7, 6, 5};

    int first_max, second_max;
    findTwoLargest(arr, first_max, second_max);

    std::cout << "First largest: " << first_max << std::endl;
    std::cout << "Second largest: " << second_max << std::endl;

    return 0;
}
```

