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
