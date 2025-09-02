// Regular Expression Matching

/**
 * Recursive Bottom-up Apporach
 * @param s text
 * @param p pattern
 * @returns wether the string matches the pattern or not
 */
function isMatch1(s: string, p: string): boolean {
  function isMatchRec(t: string, p: string, n: number, m: number): boolean {
    // if pattern is empty, string must be also empty
    if (m === 0) {
      return n === 0;
    }

    // if text is empty, then pattern can have character followed by *s
    if (n === 0) {
      return (m >= 2 && p[m - 1]) === "*" && isMatchRec(t, p, n, m - 2);
    }

    // if last characters of both string and pattern match, or pattern has '.
    if (t[n - 1] === p[m - 1] || p[m - 1] === ".") {
      return isMatchRec(t, p, n - 1, m - 1);
    }

    // handle "*" in the pattern
    if (p[m - 1] === "*" && m > 1) {
      const zero = isMatchRec(t, p, n, m - 2);
      const oneOrMore =
        (p[m - 2] === t[n - 1] || p[m - 2] === ".") &&
        isMatchRec(t, p, n - 1, m);

      return zero || oneOrMore;
    }

    // no match
    return false;
  }

  return isMatchRec(s, p, s.length, p.length);
}

/**
 * Recursive Top-Down Apporach with Memoization
 * @param s text
 * @param p pattern
 * @returns wether the string matches the pattern or not
 */

function isMatch2(s: string, p: string): boolean {
  const cache = new Map();

  // depth first search
  function dfs(i: number, j: number): boolean {
    if (cache.get([i, j]) !== undefined) return cache.get([i, j]);

    if (i >= s.length && j >= p.length) {
      return true;
    }

    if (j >= s.length) {
      return false;
    }

    const match = i < s.length && (s[i] === p[j] || p[j] === ".");

    if (j + 1 < p.length && p[j + 1] == "*") {
      cache.set([i, j], dfs(i, j + 2) || (match && dfs(i + 1, j)));
      return cache.get([i, j]);
    }

    if (match) {
      cache.set([i, j], dfs(i + 1, j + 1));
      return cache.get([i, j]);
    }

    cache.set([i, j], false);
    // no match
    return cache.get([i, j]);
  }

  console.log(cache);

  return dfs(0, 0);
}

console.log(isMatch2("a", "a*"));
