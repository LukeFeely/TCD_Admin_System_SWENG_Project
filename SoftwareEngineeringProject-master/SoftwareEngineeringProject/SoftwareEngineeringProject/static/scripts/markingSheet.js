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
 
        kendo.drawing.pdf.toBlob(group, function(blob){
        
            filename = studentNumber+"__marks.pdf"
            var form = new FormData();
            const file = new File([blob],filename, {type: "application/pdf"})
            form.append("pdfFile", file);
           

           

            $.ajax(

                options = {
                    contentType : false,
                    processData:false,
                    url : "blob/", // the endpoint
                    type : "POST", // http method
                    data:form,
                    dataType: 'text',
                    
                    // handle a successful response
                    success : function(data,status,xhr) {
                     
                  
                  
                    },
            
                    // handle a non-successful response
                    error : function(xhr,errmsg,err) {
                        Swal.fire({
                            type: 'error',
                            title: 'Oops...',
                            text: 'An error was returned. Data not written to database!',
                           
                          })
                          console.log(errmsg)
                          console.log(err)

                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    }
                }
            );
            
        });



    });
    }





			$(document).ready(function() {
                $("#loadingScreen").css("display", "none");
                $('#submitButton').click(function() { // catch the form's submit event
                $("#loadingScreen").css("display", "inline");
					 let csrftoken = getCookie('csrftoken')
					 $.ajaxSetup(
						 {
                     		beforeSend: function(xhr, settings) 
							 {
                            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        	 }
                		 });
					var frm = $('#markingForm')
					$.ajax(
						{ // create an AJAX call...
					
							data: frm.serialize(), // get the form data
							type: 'POST', // GET or POST
							url: '/marking/checkFormValidity', // the file to call
							success: function(response) 
							{ // on success..
								if(response == "success")
								{
                                   console.log("form is valid..")
                                    var id = document.getElementById("studentid").innerHTML
                                    ExportPdf(id)
									var frm = $('#markingForm')
									$.ajax(
										{ // create an AJAX call...
									
										data: frm.serialize(), // get the form data
										type: 'POST', // GET or POST
										url: '/marking/submit', // the file to call
										success: function(response) 
											{ // on success..
                                                
                                                
												Swal.fire({
                                                    title: "Thank You!",
                                                    text:"Your marks have been recorded",
                                                    type: 'success',
                                                    confirmButtonColor: '#3085d6',
                                                    confirmButtonText: 'Cool'
                                                  }).then((result) => {
                                                    if (result.value) {
                                                        var host = "http://"+ window.location.hostname+":8000/"
                                
                                                        var page = "marking/uncorrected/"
                                                        $(location).attr('href', host+page)
                                                    }
                                                  })

                                                  $("#loadingScreen").css("display", "none");
                                                   
												
											},
											error:function(data)
											{
												
												Swal.fire({
                                                    type: 'error',
                                                    title: 'Oops...',
                                                    text: "Error Writing To Database",
                                                    footer: 'Check your internet connection'
                                                    })
                                                    $("#loadingScreen").css("display", "none");
											}
										})
							
								}
								else
								{
									Swal.fire({
									type: 'error',
									title: 'Oops...',
									text: "Your Missing data from your form",
									footer: 'Make sure your weighting adds up to 100%!'
                                    })
                                    $("#loadingScreen").css("display", "none");
                                    
								}
							},
						
					});
					return false;
                });
                

                $('#draftButton').click(function() { 
                    $("#loadingScreen").css("display", "inline");
                    let csrftoken = getCookie('csrftoken')
					 $.ajaxSetup(
						 {
                     		beforeSend: function(xhr, settings) 
							 {
                            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        	 }
                		 });
					var frm = $('#markingForm')
					$.ajax(
						{ // create an AJAX call...
					
							data: frm.serialize(), // get the form data
							type: 'POST', // GET or POST
							url: '/marking/draft', // the file to call
							success: function(response) 
							{ // on success..
								
							
								Swal.fire({
                                    title: "Draft Submitted!",
                             
                                    type: 'success',
                                    confirmButtonColor: '#3085d6',
                                    confirmButtonText: 'Cool'
                                  })
                                  $("#loadingScreen").css("display", "none");
								
                            },
                            error:function(response)
                            {
                                Swal.fire({
                                    type: 'error',
                                    title: 'Oops...',
                                    text: "Couldn't save your draft",
                                    footer: 'Check your internet connection'
                                    })
                                    $("#loadingScreen").css("display", "none");
                            }
						
					});
					return false;
                })
			});