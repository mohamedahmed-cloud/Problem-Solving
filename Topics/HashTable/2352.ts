function equalPairs(grid: number[][]): number {
    let ans = 0, n = grid.length
    let map:{[key: string]: number} = {}

    for (let i = 0; i < n; i++) {
        let tmp = []
        for (let j = 0; j < n; j++) tmp.push(grid[j][i])
        const key = tmp.join(",")
        map[key] =(map[key] || 0 )+  1
    }
    // console.log(map)
    for (let i of grid) {
        const key = i.join(",")
        ans += (map[key] || 0)
    }
    return ans
};

let grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
console.log(equalPairs(grid))