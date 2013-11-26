window.onload=function() {
    try {
        document.getElementById("id_assignees").className =
            document.getElementById("id_assignees").className.replace(/\bform-control\b/,'');
    } catch(err) {}

    try {
        document.getElementById("id_product_versions").className =
            document.getElementById("id_product_versions").className.replace(/\bform-control\b/,'');
    } catch(err) {}
}
