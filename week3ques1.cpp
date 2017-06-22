# include <iostream>  
# include <fstream>  
# include <vector>  
  
using namespace std;  
  
long sort(vector<int>&, int, int);  
int partition(vector<int>&, int, int);  
int median_of_3(vector<int>&, int, int, int);  
  
int main(int argc, char** argv) {  
  
    vector<int> num;  
  
    ifstream infile;  
    infile.open("QuickSort.txt", ios::in);  
    int tmp;  
    while (infile >> tmp)  
        num.push_back(tmp);  
    infile.close();  
  
    long cnt = sort(num, 0, num.size()-1);  
  
    for (int i = 0; i < num.size(); ++i)  
        cout << num[i] << endl;  
    cout << "# of comparisons: " << cnt << endl;  
  
    return 0;  
}  
  
long sort(vector<int>& num, int low, int high) {  
  
    if (high <= low)  
        return 0;  
    int pivot = partition(num, low, high);  
    long tmp1 = sort(num, low, pivot-1);  
    long tmp2 = sort(num, pivot+1, high);  
    return (tmp1+tmp2+(high-low));  
}  
  
int partition(vector<int>& num, int low, int high) {  
  
    int index = median_of_3(num, low, high, (low+high)/2);  
    int pivot = num[index];  
    swap(num[low], num[index]);  
    int i = low + 1;  
    int j;  
    for (j = low + 1; j <= high; ++j) {  
        if (num[j] < pivot) {  
            swap(num[i], num[j]);  
            ++i;  
        }  
    }  
    swap(num[i-1], num[low]);  
    return (i-1);  
}  
  
int median_of_3(vector<int>& num, int low, int high, int medium) {  
  
    if (num[low] > max(num[medium], num[high])) {  
        if (num[medium] > num[high])  
            return medium;  
        else  
            return high;  
    }  
    else if (num[low] < min(num[medium], num[high])) {  
        if (num[medium] > num[high])  
            return high;  
        else  
            return medium;  
    }  
    else  
        return low;   
}  