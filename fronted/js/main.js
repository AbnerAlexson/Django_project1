console.log('hello friend')
console.log('hello friend3')
$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i++) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    }
})

$(document).on("click", ".js-toggle-modal", function(e) {
    e.preventDefault()
    $('.js-modal').toggleClass('hidden')
})
.on('click', '.js-submit', function(e) {
    e.preventDefault();
    const text = $(".js-post-text").val().trim()
    const $btn = $(this)
    
    if(!text.length) {
        return false
    }

    //$('.js-modal').addClass('hidden')
    //$(".js-post-text").val('')

    $btn.prop("disabled", true).text("Posting!")// disables button when posting so that the user cannot click it twice
    $.ajax({
        type: "POST",
        url: $(".js-post-text").data("post-url"), //this is where ajax can get the data to post
        data: {
            text: text // python can access this through request.post.text
        },
        success: (dataHtml) => { //dataHtml is whatever render() returns
            $('.js-modal').addClass('hidden'); // if post is successful the post modal is hidden
            $("#posts-container").prepend(dataHtml); // this prepends the html elements to the post container, for it to show instantly when the post is successful
            $btn.prop("disabled", false).text("New Post"); // button for the modal is enabled
            $(".js-post-text").val('')
        },
        error: (error) => {
            console.warn(error)
            $btn.prop("disabled", false).text("Error");
        }

    });

})
.on("click", ".js-follow", function(e) {
    e.preventDefault()
    console.log("I was clicked")
    const action = $(this).attr("data-action")
    $.ajax({
        type: "POST",
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        success: (data) => { 
            $(".js-follow-text").text(data.wording)
            if(action == 'follow') {
                //change to unfollow
                $(this).attr("data-action", "unfollow")
            } else {
                $(this).attr("data-action", "follow")
            }
        },
        error: (error) => {
            console.warn(error)
        }

    });
})
