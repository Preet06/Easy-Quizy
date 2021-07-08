










var fin = []
var marks=0
var chec = []
var e = document.getElementsByTagName("input");
var roll_no = document.getElementById("roll_no").value
document.getElementById("demo3").innerHTML = roll_no;
function sayHello() {
    alert("Hello World")
}
function myFunction()
{
    for (i = 0; i <= fin.length; i++) {
        if (fin[i] == chec[i])
        {
            marks = marks + 1
        }
    }
    roll_no = document.getElementById("roll_no").value

    $.ajax({
        type: 'GET',
        url: 'final',
        data: {'marks': marks-1, 'roll_no':roll_no ,  csrfmiddlewaretoken: '{{ csrf_token }}'},
        dataType: 'json',
    });

    location.replace('final')

}
    function getanswers()
    {

        for (i = 0; i <= e.length; i++)
        {
            if (e[i].type == "radio")
            {
                if (e[i].checked)
                {
                    chec.push(e[i].value)

                    document.getElementById("demo3").innerHTML += e[i].value;
                }

                if (e[i].id == "ans22")
                {

                    fin.push(e[i].value)
                    document.getElementById("Answers").innerHTML += e[i].value;
                }
            }
        }

    }


document.getElementById("open-popup-btn").addEventListener("click",function(){
  document.getElementsByClassName("popup")[0].classList.add("active");
});

document.getElementById("dismiss-popup-btn").addEventListener("click",function(){
  document.getElementsByClassName("popup")[0].classList.remove("active");
});


