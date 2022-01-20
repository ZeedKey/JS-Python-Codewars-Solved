/**
	- Instruction! -

	Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

**/

function inArray(a1,a2){
  let arr = [];
  let new_arr = [];
  for (let i=0; i<a1.length;i++){
    for (let j=0; j<a2.length;j++){
      if (a2[j].includes(a1[i])){
        arr.push(a1[i])
      }
    }
  }
  
  arr.map(el => {
    if (!new_arr.includes(el)) new_arr.push(el)
  })
  return new_arr.sort()
}