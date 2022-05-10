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
