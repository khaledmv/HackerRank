// Given an array of integers, calculate the ratios of its elements that are
// positive, negative, and zero. Print the decimal value of each fraction on a
// new line with  places after the decimal.


function plusMinus(arr) {
    // Write your code here
    
    let positive = 0;
    let negative = 0
    let zero = 0;
    
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === 0){
            zero++;
        }else if(arr[i] >0 ){
            positive++;
        }else{
            negative++;
        }
    }
    
    console.log((positive/arr.length).toFixed(6))
    console.log((negative/arr.length).toFixed(6))
    console.log((zero/arr.length).toFixed(6))
}


plusMinus(1,1, 0, -1,-1)