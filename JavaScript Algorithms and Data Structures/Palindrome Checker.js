function palindrome(str) {
    var character = /[^A-Za-z0-9]/g;
    var ordered_string = str.toLowerCase().replace(character, '');
    var ordered_string_reversed = ordered_string.split("").reverse().join("");
    return ordered_string === ordered_string_reversed;
  }
  
  palindrome("eye");