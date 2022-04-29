function priceSplit(price) {
  let result = "";
  let count = 0;
  price = price.toString().split("").reverse().join("");
  for (let index = 0; index < price.length; index++) {
    if (count == 3) {
      result += ",";
      count = 0;
    }
    count++;
    result += price[index];
  }
  return result.split("").reverse().join("");
}

function phoneSplit(phone) {
  let result = "";
  phone = phone.toString().split("");
  for (let index = 0; index < phone.length; index++) {
    if (index == 4 || index == 7) {
      result += "-";
    }
    result += phone[index];
  }
  return result;
}
export default {
  priceSplit,phoneSplit
}