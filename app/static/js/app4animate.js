/**
 * Created by lulizhou on 2015/9/5.
 */
  $(function(){
        $('.showbtn>span').click(function(){
            $(this).addClass("current");
        $('.ds-thread').show().animate({"opacity":1},1000);
    })})