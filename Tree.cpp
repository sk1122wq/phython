#include <iostream>
using namespace std;

// ===============================
// Tree Node Class
// ===============================
template <class T>
class TreeNode {
private:
    T info;
    TreeNode<T>* left;
    TreeNode<T>* right;

public:
    TreeNode(T val) {
        info = val;
        left = NULL;
        right = NULL;
    }

    T* getInfo() { return &info; }
    TreeNode<T>* getLeft() { return left; }
    TreeNode<T>* getRight() { return right; }

    void setLeft(TreeNode<T>* node) { left = node; }
    void setRight(TreeNode<T>* node) { right = node; }
};


// ===============================
// Insert into BST (no duplicates)
// ===============================
template <class T>
TreeNode<T>* insert(TreeNode<T>* root, T value)
{
    // If tree empty ? new node becomes root
    if (root == NULL) {
        root = new TreeNode<T>(value);
        return root;
    }

    // Duplicate found ? do NOT insert
    if (value == *(root->getInfo()))
        return root;

    // Insert left
    if (value < *(root->getInfo()))
        root->setLeft(insert(root->getLeft(), value));

    // Insert right
    else
        root->setRight(insert(root->getRight(), value));

    return root;
}


// ===============================
// Traversal Functions
// ===============================

// PREORDER: Root ? Left ? Right
void preorder(TreeNode<int>* treeNode)
{
    if (treeNode != NULL) {
        cout << *(treeNode->getInfo()) << " ";
        preorder(treeNode->getLeft());
        preorder(treeNode->getRight());
    }
}

// INORDER: Left ? Root ? Right
void inorder(TreeNode<int>* treeNode)
{
    if (treeNode != NULL) {
        inorder(treeNode->getLeft());
        cout << *(treeNode->getInfo()) << " ";
        inorder(treeNode->getRight());
    }
}

// POSTORDER: Left ? Right ? Root
void postorder(TreeNode<int>* treeNode)
{
    if (treeNode != NULL) {
        postorder(treeNode->getLeft());
        postorder(treeNode->getRight());
        cout << *(treeNode->getInfo()) << " ";
    }
}


// ===============================
// Main function
// ===============================
int main()
{
    TreeNode<int>* root = NULL;

    // Insert elements (duplicates ignored)
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);   // duplicate ? ignored

    cout << "Preorder: ";
    preorder(root);
    cout << endl;

    cout << "Inorder: ";
    inorder(root);
    cout << endl;

    cout << "Postorder: ";
    postorder(root);
    cout << endl;

    return 0;
}
