function isPalindrome(x) {
  let str = x.toString();
  let endpoint = Math.floor(str.length / 2);
  for (let i = 0; i < endpoint; i++) {
    let tail = str.length - 1 - i;
    if (str[i] != str[tail]) {
      console.log("false");
      return false;
    }
  }
  console.log("true");
  return true;
}

isPalindrome(121);
isPalindrome(1243431);
isPalindrome(1221);
isPalindrome(121121);
