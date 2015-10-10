/**
 * Created by lulizhou on 2015/10/9.
 */
(function($){
    var $windows=$(window);
    var $document=$(document);
    function roll2load() {
        this.url = 'get_archives'
        this.id = 'sort'
        this.pagenum = 1;
        this.yearNow = 0;
        this.isEnd = false;
    }
    roll2load.prototype={
        constructor : roll2load,
        returnYear : function(data){
            return ' <li class="year"><a href="javascript:;">'+data.year+'</a></li>';
        },
        returnBody : function(data){
             return ' <li><a href="'+
            data.url+
            '">'+
            data.date+
            '&nbsp;&nbsp;&nbsp;&nbsp;'+
            data.title+
            '</a></li>'
        },
        getData : function(){
            var url = this.url
            var _this = this;
                $.get(url,
                    {page:this.pagenum},
                    function(data){
                       _this.setData(data);
                    },'json')
                },
        setData: function(data){
            var _this = this;
            if(!data['result']){
                _this.isEnd=true;
                $("#"+this.id).append("<p class='nomore'>没有更多了!<p>")
            }
            else {
                 var posts=data['posts'];
                posts.forEach(function(item,index,array){
                    if(item.year!=_this.yearNow){
                       $("#"+_this.id).append(_this.returnYear(item))
                    }
                    _this.yearNow = item.year;

                    $("#"+_this.id).append(_this.returnBody(item));

                })
          }
        },
        scollThenSet:function(){

            var _this = this;
            $(document).ready(function(){
                    _this.getData();
                    _this.pagenum++;
            });
            $(window).scroll(function(){
            // 当滚动到最底部以上100像素时， 加载新内容
            if ($(document).height() - $(this).scrollTop() - $(this).height()<10&&!_this.isEnd)
            {
                _this.getData();
                _this.pagenum++;
            };
            });
        }

    }
    var roll = new roll2load();
    roll.scollThenSet();

})(jQuery);