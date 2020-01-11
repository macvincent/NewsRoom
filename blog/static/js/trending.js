function updateLatestStories(){
    $.get('http://127.0.0.1:61690/latest/', data =>{
        data.forEach(news => {
            $('#trendingStories').append(`<li  id="trendingArticles"><a href="blogchatroom/?news=${news.title}"><section>${news.title}</section></a></li>`);
        });
    });
};

// Update trending stories every minute
updateLatestStories();
setTimeout(updateLatestStories, 60000);