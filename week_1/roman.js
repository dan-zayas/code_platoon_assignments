function to_roman(num) {
  // empty string
  let output = ""
  // important to create a dict with the highest values and downward
  let map = {
    "M" : 1000,
    "CM" : 900,
    "D" : 500,
    "CD" : 400,
    "C" : 100,
    "XC" : 90,
    "L" : 50,
    "XL" : 40,
    "X" : 10,
    "IX" : 9,
    "V" : 5,
    "IV" : 4,
    "I" : 1
  }

  while (num > 0) {
    for (let i in map) {
      //loop through the dict looking for the highest number and append that highest number roman while also decrementing num by that same amount.
      if (num >= map[i]) {
        output += `${i}`
        num -= map[i]
      }
    }
  }

  return output
}

console.log(to_roman(944))
