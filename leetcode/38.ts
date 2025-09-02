// Leetcode: 38
// Count and Say
// https://leetcode.com/problems/count-and-say/
// #medium

function countAndSay(n: number): string {
  let s = "1";

  for (let i = 1; i < n; i++) {
    s = stringBuilder(s);
  }
  return s;
}

function stringBuilder(currString: string): string {
  let nextString = "";
  let count = 1;
  let prevChar = currString.at(0);
  for (let i = 0; i < currString.length; i++) {
    if (prevChar == currString.at(i + 1)) {
      count++;
    } else {
      nextString = nextString + count + prevChar;
      count = 1;
      prevChar = currString.at(i + 1);
    }
  }
  return nextString;
}

const res = countAndSay(4);
console.log("Answer", res);
