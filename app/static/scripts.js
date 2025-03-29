function toggleSenha(id, el) {
    const input = document.getElementById(id);
    if (input.type === "password") {
        input.type = "text";
        el.classList.remove("fa-eye");
        el.classList.add("fa-eye-slash");
    } else {
        input.type = "password";
        el.classList.remove("fa-eye-slash");
        el.classList.add("fa-eye");
    }
}

if (typeof flashMessages !== 'undefined' && flashMessages.length > 0) {
    flashMessages.forEach(msg => {
        Swal.fire({
            icon: msg.icon,
            title: msg.title,
            timer: 3000,
            showConfirmButton: false,
            customClass: {
                title: 'swal-custom-title'
            }
        });
    });
}