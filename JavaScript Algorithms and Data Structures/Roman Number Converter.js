function convertToRoman(num) {
    var mappa = {
      M:1000,
      CM:900,
      D:500,
      CD:400,
      C:100,
      XC:90,
      L:50,
      XL:40,
      X:10,
      IX:9,
      V:5,
      IV:4,
      I:1},
      romano = '', i;
      for ( i in mappa ) {
        while ( num >= mappa[i] ) {
          romano += i;
          num -= mappa[i];
        }
      }
      return romano;
    }
    
    convertToRoman(36);