var workshops_js, workshop_skillsets, workshop_to_register;
var modal, modal_workshop, open_modal_btns, close_btn, register_btn;
// var modal = document.getElementById("modalQuery");
// var modal_workshop = document.getElementById("registerConfirm");
// var open_modal_btns = document.querySelectorAll("registerBtn");
// var close_btn = document.getElementById("closeBtn");
// var register_btn = document.getElementById("finalRegsiterBtn");

window.onload = function() {
    modal = document.getElementById("modalQuery");
    modal_workshop = document.getElementById("registerConfirm");
    open_modal_btns = document.querySelectorAll("registerBtn");
    close_btn = document.getElementById("closeBtn");
    register_btn = document.getElementById("finalRegisterBtn");
    
    // Register logic
    register_btn.onclick = function() {
        // TODO: Register current user to workshop
        modal.style.display = "none";
    }

    close_btn.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

document.addEventListener('click', function(event) {
    if (event.target.classList.contains("registerBtn")) {
        // Search for the workshop
        var workshop_ids = workshops_js.replace(/['\[\]\s]+/g,"").split(",");
        var workshop_skills = workshop_skillsets.replace(/['\[\]]+/g,"").split(",");
        for (var i=0; i < workshops_js.length; i++) {
            if (event.target.id == workshop_ids[i]) {
                // Found matching workshop
                workshop_to_register = i;
                modal_workshop.innerHTML = workshop_skills[i];
                modal.style.display = "block";
            }
        }
    }
})

// document.querySelector("registerBtn").addEventListener(event => {
//     var target_id = event.target.id;
//     // Search for the workshop
//     for (var i=0; i < workshops_js.length; i++) {
//         if (target_id == workshops_js[i]["workshop_ID"]) {
//             // Found matching workshop
//             workshop_to_register = i;
//             modal_workshop.innerHTML = workshops_js[i]["skill_set_name"];
//             modal.style.display = "block";
//         }
//     }

// })