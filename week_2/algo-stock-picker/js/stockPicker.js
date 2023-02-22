picker = function (prices) {

    let biggestProfit = 0
    let buyDay = 0
    let sellDay = 0
    for(i in prices) {
        for(j in prices) {
            let currentMath = prices[j] - prices[i]
            if(j>i) {
                if(currentMath > biggestProfit) {
                    biggestProfit = currentMath
                    buyDay = i
                    sellDay = j
                }
            }
        }
    }
    console.log("The biggest profit is $" + biggestProfit + " when you buy on Day " + buyDay + " and you sell on Day " + sellDay + ".")
    return [parseInt(buyDay), parseInt(sellDay)]

}

console.log(picker([17,3,6,9,15,8,6,1,10]))
console.log(picker([17,3,6,9,15,8,6,1,10]))
console.log(picker([3,17,6,9,18,15,6,1,10]))
console.log(picker([1,17,6,9,8,15,6,3,19]))
console.log(picker([19,17,6,9,8,15,6,3,1]))