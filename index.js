function flip(arr) {
  let ipos = 0;
  let jpos = 0;
  let count1s = 0;
  for (let i = 0; i < arr.length; i++) if (arr[i] == "1") count1s++;
  let curCount = count1s;
  let maxCount = count1s;
  let res = [];
  console.log(count1s);
  while (ipos <= jpos && jpos < arr.length) {
    if (arr[jpos] == "0") curCount++;
    else curCount--;

    if (curCount < count1s) {ipos = jpos + 1; curCount = count1s}
    else if (curCount > maxCount) {
      maxCount = curCount;
      res = [ipos + 1, jpos + 1];
    }

    jpos++;
  }

  return res;
}


function Nsort(A){
    A = A.sort((a,b)=>{ if(+a < +b) return -1; else return 1;});
    let start = 0;
    let end = A.length-1;
    console.log(A.length);
    for(let i = 0; i < A.length; i++){
        if(A[i] == A.length-i-1 && A[i] != 0)
        {
            console.log(A[i], A.length-i-1);
            return 1;

        }
        console.log(A[i]);
    }
