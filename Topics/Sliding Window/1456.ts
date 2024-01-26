function maxVowels(s: string, k: number): number {
  let map = new Set(["a", "e", "i", "o", "u"]);
  let n = s.length;
  let curr = 0,
    ans = 0,
    p1 = 0;

  for (let i = 0; i < k; i++) {
    if (map.has(s[i])) {
      curr += 1;
    }
  }
  ans = curr;
  for (let i = k; i < n; i++) {
    if (map.has(s[i])) {
      curr += 1;
    }
    if (map.has(s[p1])) curr -= 1;

    p1++;
    if (curr > ans) ans = curr;
  }
  return ans;
}

let s = "abciiidef",
  kk = 3;
console.log(maxVowels(s, kk));
