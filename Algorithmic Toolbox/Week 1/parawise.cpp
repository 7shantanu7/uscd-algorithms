#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

long long maxparawise(const vector<int>& numbers){
    int n = numbers.size(); 
    int max1 = -1;
    for(int i = 0; i<n; ++i)
        if ((max1 == -1) || (numbers[i]>numbers[max1]))
        max1 = i;
    int max2 = -1;
    for (int j = 0; j<n; ++j)
        if ((j!=max1) && ((max2 == -1) || (numbers[j]>numbers[max2])))
        max2 = j;   
     
    return ((long long)(numbers[max1]))*numbers[max2];
}  

int main(){
    int n;
    cin>>n;
    vector<int> numbers(n);
    for(int i = 0;i<n;++i){
        cin>>numbers[i];
    }
    long long  result = maxparawise(numbers);
    cout<<result<<endl;
}