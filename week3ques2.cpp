# include <iostream>  
# include <fstream>  
# include <vector>  
  
using namespace std;  
  
long sort(vector<int>&, int, int);  
int partition(vector<int>&, int, int);  
  
int main(int argc, char** argv) {  
  
    vector<int> num;  
  
    ifstream infile;  
    infile.open("QuickSort.txt", ios::in);  
    int tmp;  
    while (infile >> tmp)  
        num.push_back(tmp);  
    infile.close();  
  
    long cnt;  
  
    cnt = sort(num, 0, num.size()-1);  
  
    for (int i = 0; i < num.size(); ++i)  
        cout << num[i] << endl;  
    cout << "# of comparisons: " << cnt << endl;  
  
    return 0;  
}  
  
long sort(vector<int>& num, int low, int high) {  
  
    if (high <= low)  
        return 0;  
    int pivot = partition(num, low, high);  
    int tmp1 = sort(num, low, pivot-1);  
    int tmp2 = sort(num, pivot+1, high);  
    return (tmp1 + tmp2 + (high - low));  
}  
  
int partition(vector<int>& num, int low, int high) {  
  
    int pivot = num[high];  
    swap(num[low], num[high]);  
    int i = low + 1;  
    int j;  
    for (j = low + 1; j <= high; ++j) {  
        if (num[j] < pivot) {  
            swap(num[i], num[j]);  
            ++i;  
        }  
    }  
    swap (num[i-1], num[low]);  
    return (i-1);  
}