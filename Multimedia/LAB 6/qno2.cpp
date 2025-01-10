#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

// Node of Huffman Tree
struct HuffmanNode
{
    char ch;
    int freq;
    HuffmanNode *left, *right;

    HuffmanNode(char character, int frequency)
    {
        ch = character;
        freq = frequency;
        left = right = nullptr;
    }
};

// Comparison object to be used in priority queue
struct Compare
{
    bool operator()(HuffmanNode *left, HuffmanNode *right)
    {
        return left->freq > right->freq;
    }
};

// Recursive function to generate Huffman Codes
void generateCodes(HuffmanNode *root, string str, unordered_map<char, string> &huffmanCodes)
{
    if (!root)
        return;

    if (root->ch != '$')
        huffmanCodes[root->ch] = str;

    generateCodes(root->left, str + "0", huffmanCodes);
    generateCodes(root->right, str + "1", huffmanCodes);
}

// Build Huffman Tree and generate codes
void buildHuffmanTree(string text)
{
    unordered_map<char, int> freq;
    for (char ch : text)
    {
        freq[ch]++;
    }

    priority_queue<HuffmanNode *, vector<HuffmanNode *>, Compare> minHeap;
    for (auto pair : freq)
    {
        minHeap.push(new HuffmanNode(pair.first, pair.second));
    }

    while (minHeap.size() != 1)
    {
        HuffmanNode *left = minHeap.top();
        minHeap.pop();
        HuffmanNode *right = minHeap.top();
        minHeap.pop();

        HuffmanNode *top = new HuffmanNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;
        minHeap.push(top);
    }

    HuffmanNode *root = minHeap.top();
    unordered_map<char, string> huffmanCodes;
    generateCodes(root, "", huffmanCodes);

    cout << "Huffman Codes:\n";
    for (auto pair : huffmanCodes)
    {
        cout << pair.first << " " << pair.second << "\n";
    }

    cout << "\nOriginal string: " << text << "\n";

    string encodedStr = "";
    for (char ch : text)
    {
        encodedStr += huffmanCodes[ch];
    }

    cout << "\nEncoded string: " << encodedStr << "\n";
}

int main()
{
    string text;
    cout << "Enter the text to encode: ";
    getline(cin, text);

    buildHuffmanTree(text);

    return 0;
}
