/**
 * Created by lulizhou on 2015/10/28.
 */
$(function(){
    $(".delete").on('click',function(){
        var refresh = function(_this){
            $(_this).parents("tr").remove();
        };

        var c = confirm("确认删除？")
        if(c){
            $.ajax({
                url:$(this).attr("data-href"),
                success: refresh(this)
            })
        }
    })
})