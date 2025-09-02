class Node {
  key: number;
  left: Node | null;
  right: Node | null;

  constructor(key: number) {
    this.key = key;
    this.left = null;
    this.right = null;
  }
}

function insert(root: Node | null, key: number) {
  if (root == null) {
    return new Node(key);
  }

  if (root.key == key) return root;

  if (key < root.key) {
    root.left = insert(root.left, key);
  } else if (key > root.key) {
    root.right = insert(root.right, key);
  }

  return root;
}

function deleteNode(root: Node | null, key: number) {
  // 3 Cases
  // 1. Deleting the leaf Node
  // 2. Node with 1 Leaf Node
  // 3. Node with 2 Leaf Nodes, [i] Replace with Inorder Predecessor [ii] Replace with Inorder Successor
}

function searchNode(root: Node | null, key: number) {
  if (root == null || root.key == key) {
    return root;
  }

  if (root.key < key) {
    return searchNode(root.right, key);
  }
  return searchNode(root.left, key);
}

function inOrder(root: Node | null) {
  if (root != null) {
    inOrder(root.left);
    console.log(root.key + " ");
    inOrder(root.right);
  }
}
function postOrder(root: Node | null) {
  if (root != null) {
    postOrder(root.right);
    console.log(root.key + " ");
    postOrder(root.left);
  }
}

const root = new Node(4);
insert(root, 2);
insert(root, 7);
insert(root, 1);
insert(root, 6);
insert(root, 3);
insert(root, 5);

const subTree = searchNode(root, 2);

console.log("In Order");
inOrder(root);

console.log("Post Order");
postOrder(root);

console.log("Search Sub Tree");
inOrder(subTree);
