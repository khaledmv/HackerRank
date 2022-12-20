


// find min-max num  = [1,3,5,7,9]  == max = 24 and min 16




function miniMaxSum(arr){
	 // 

	 const sortedArray = arr.sort();
	 let min_sum = 0
	 let max_sum = 0

	 for( let i = 0; i <arr.length; i++){
	 	if(i < arr.length - 1){
	 		min_sum += arr[i]
	 	}

	 	if(i > 0 ){
	 		max_sum+= arr[i]
	 	}
	 }
	 console.log(min_sum, max_sum);
}



miniMaxSum([1,3,5,7,9]);