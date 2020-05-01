function updateLatestStories(){
    $.get('latest/', data =>{
        data.forEach(news => {
            $('#trendingStories').append(`<li  id="trendingArticles"><a href="blogchatroom/?news=${news.title}"><section>${news.title}</section></a></li>`);
        });
    });
};

// get new stories for blog
let call_num = 1
function updateBlog(){
    $.get('update/', {call: call_num}).done(data => {
        Object.values(data).forEach(news => {
            $('.mainFeed').append(`<div  class="article">
            <a href="{% url 'chatroom' %}?news=${news.title}">
                <p class="blogText">
                    ${news.title}
                </p>
                <img src="${news.image}" height="400" width="500"/><br>
                <div class="comment blogText">
                    ${news.post}
                </div>
            </a>
        </div>`)
        });
        call_num++;
        needUpdate();
    });
}
// Update trending stories two minutes
updateLatestStories();
setTimeout(updateLatestStories, 120000);

function needUpdate(){
    $(window).on("scroll", e => {
        var scrollHeight = $(document).height();
        var scrollPosition = $(window).height() + $(window).scrollTop();
        if ((scrollHeight - scrollPosition) < scrollHeight/4) {
            $(window).off("scroll");
            updateBlog();
        }
    });
}
needUpdate();