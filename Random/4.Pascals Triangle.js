let solve = function (numsRows) {
  x = [[1], [1, 1]];

  if (numsRows === 1) return[x[0]];
  else if (numsRows === 2) return x;
  else {
    for (let i = 0; i < numsRows - 2; i++) {
      f = x.at(-1);
      newx = [1];
      for (let j = 1; j < f.length; j++) {
        newx.push(f[j - 1] + f[j]);
      }
      newx.push(1);
      x.push(newx);
    }
  }
  return x;
};
console.log(solve(5));
