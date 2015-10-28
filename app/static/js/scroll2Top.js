(function($,window) {
    function scroll2Top(){}

    scroll2Top.prototype={
        init:function(){
            if(this.nowScroll()>=800){
                this.dom();
                this.animate();
            }else if (this.nowScroll()<=200){
                this.remove();
            }
        },
        nowScroll:function(){
            return $(document).scrollTop();
        },
        dom:function(){
            if(!document.getElementById('go2top')){
                 $('body').append( '<div id="go2top"></div>');
            }

        },
        animate:function(){
            var _this = this;
            $('#go2top').on('click',function(){
                $('html,body').animate({'scrollTop':0},function(){
                _this.remove();
            });
            });

        },
        remove:function(){
            $('#go2top').remove();
        }
    }
    var scroll = new scroll2Top();
    $(window).scroll(function(){
        scroll.init();
    });
})(jQuery,window);