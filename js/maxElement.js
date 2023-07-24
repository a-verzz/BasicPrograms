// Function to find the maximum element in an array
function findMaxElement(arr) {
  if (!Array.isArray(arr) || arr.length === 0) {
    return "Input is not a valid non-empty array.";
  }

  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }

  return max;
}

// Example usage:
const numbers = [5, 10, 3, 22, 7, 15];
const maxNumber = findMaxElement(numbers);
console.log("Maximum element in the array:", maxNumber);
