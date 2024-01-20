function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let len = flowerbed.length

    for(let i = 0; i < len; i++){
        if (i == 0  && flowerbed[i] == 0){
            if(i + 1 == len || flowerbed[i + 1] === 0) {
                flowerbed[i] = 1
                n -= 1;
            }
        }
        else if (i > 0 && i + 1 < len && flowerbed[i - 1] === 0 
            && flowerbed[i] === 0 && flowerbed[i + 1] === 0) {
            flowerbed[i] = 1
            n -= 1
        }
        else if (i > 0 && i + 1 == len && flowerbed[i - 1] === 0 && flowerbed[i] == 0) {
            flowerbed[i] == 1
            n -= 1
        }

    }

    return n <= 0;
};

let flowerbed = [0, 1, 0]
let n = 1
console.log(canPlaceFlowers(flowerbed, n));