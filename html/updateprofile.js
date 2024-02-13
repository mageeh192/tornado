"use strict";

console.log(document.location.pathname);

function submit(){
            let pname = document.getElementById("pname").value;
            let dob = document.getElementById("birthdate").value;
            console.log("Info:", pname, dob);

            let J = {
                preferredName: pname,
                birthdate: dob
            };
            
            fetch( document.location.pathname,
            {   method: "POST",
                body: JSON.stringify(J)
            }
            ).then( (resp) => {
                //can also use text(), blob(), or arrayBuffer()
                resp.json().then( (J) => {
                    console.log("Server said:",J);
                });
            }).catch( (err) => {
                console.log("Uh oh",err);
            })
}