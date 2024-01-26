class RecentCounter {
    counter: number;
    queue: number[];
    p1: number;
    p2: number;
    constructor() {
        this.counter = 0
        this.queue = []
        this.p1 = 0
        this.p2 = 0
    }

    ping(t: number): number {
        while(this.queue.length > this.p1 && t - this.queue[this.p1] > 3000) {
            this.p1 += 1
        }
        this.queue.push(t)
        this.p2 += 1
        return this.p2 - this.p1
    }
}



var obj = new RecentCounter()
console.log(obj.ping(1))
console.log(obj.ping(2))
console.log(obj.ping(3000))
console.log(obj.ping(3002))
