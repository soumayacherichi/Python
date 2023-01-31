// algorithme reverse par moi puis le deuxième corrigé *
var arr = ["h","e","l","l","o"]
function reversestring(arr)
{
    for (var i=0; i<arr.length/2; i++)
    {
        var j=arr.length-1-i;
        temp=arr[i]
        arr[i] = arr[j]
        arr[j]=temp
        console.log("i == ", i, "j == ", j, temp);
    }
    console.log(arr.join(""))
}

reversestring(arr)


str1="hello"
function revervecorriged(string)
{
    var reversed=""
    for(i=string.length-1;i>=0;i--)
    {
        reversed+= string[i]
    }
    console.log(string,reversed)
    return reversed
}
revervecorriged(str1)

