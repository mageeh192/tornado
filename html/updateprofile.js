"use strict";

console.log(document.location.pathname);

function submit(){

        let file = document.getElementById("ppic").files[0];
        if(!file){
            console.log("No file!");
            return;
        }
        let R = new FileReader();
        R.addEventListener("load", () => {

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
        };
        
        R.readAsBinaryString(file);

}