// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function ExportPdf(studentNumber){ 
    kendo.drawing
    .drawDOM("#myCanvas", 
    { 
    paperSize: "A4",
    margin: { top: "1cm", bottom: "1cm",right:"1.5cm",left:"1.5cm" },
    scale: 0.5,
    height: 500,
    width:1024
    })
    .then(function(group){

        let csrftoken = getCookie('csrftoken');      
        console.log(csrftoken)
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                
            }
        });
        console.log("sending")
        kendo.drawing.pdf.toBlob(group, function(blob){
        
            filename = studentNumber+"__marks.pdf"
            var form = new FormData();
            const file = new File([blob],filename, {type: "application/pdf"})
            download(file, file.name, file.type);
            console.log(file)
            form.append("pdfFile", file);
           

           

            $.ajax(

                options = {
                    contentType : false,
                    processData:false,
                    url : "blob/", // the endpoint
                    type : "POST", // http method
                    data:form,
                    dataType: 'json',
                    
                    // handle a successful response
                    success : function(xhr,code) {
                     
                        console.log("success"); // another sanity check
                        Swal.fire("Litmas")
                    },
            
                    // handle a non-successful response
                    error : function(xhr,errmsg,err) {
                        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    }
                }
            );
            
        });



    });
    }


    


$(document).ready(function(){
  
    $("#submitButton").click(function(){
        var id = document.getElementById("studentid").innerHTML

       ExportPdf(id)
   })
})