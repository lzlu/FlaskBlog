/**
 * Created by lulizhou on 2015/9/5.
 */
  $(function(){
        $('.showbtn>span').bind({
            pan:function(){
                $('.ds-thread').slideToggle();
                },
            click:function(){
                 $('.ds-thread').slideToggle();
            }
        });
      $('.ds-thread').attr("data-url", window.location.href);
  })
