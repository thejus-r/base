//*
// Find Valid Parenthesis
//  */
//
function isValid(s: string): boolean {
  let stack: string[] = [];

  for (const p of s) {
    const last = stack.at(-1);
    if (last === "(" && p === ")") {
      stack.pop();
    } else if (last === "[" && p === "]") {
      stack.pop();
    } else if (last === "{" && p === "}") {
      stack.pop();
    } else {
      stack.push(p);
    }
  }
  return stack.length === 0;
}

let str = "()";
console.log("Example 1:", isValid(str)); // true

str = "()[]{}";
console.log("Example 2:", isValid(str)); // true

str = "(]";
console.log("Example 3:", isValid(str)); // false
