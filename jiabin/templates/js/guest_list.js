
function login(){
    $("#myForm").submit() ;
}
$(".click_imgs").on("click", function () {
    $("#ceng").fadeIn();
    $(".meeasge_div").css({display:"none"});
    $(this).parent().parent().parent().next("div").fadeIn().css({top:($("body").height()-$(this).parent().parent().parent().next("div").height())/2});
    $("body").addClass("bodys");
});
$(".img_divs").on("click", function () {
    $("#ceng").fadeIn();
    $(".meeasge_div").css({display:"none"});
    $(this).parent().next("div").fadeIn().css({top:($("body").height()-$(this).parent().next("div").height())/2});
    $("body").addClass("bodys");
});
$(".glyphicon-remove").click(function () {
    $(this).parent().fadeOut();
    $("#ceng").fadeOut();
    $("body").removeClass("bodys");
});
$(".img_div").hover(function(){
    $(this).find("img").eq(1).css({display:"block"});
},function(){
    $(this).find("img").eq(1).css({display:"none"});
});

//var page = 1;
//var i =3;
//$(".img-right").click(function () {
//    var $parent = $(this).parent("div");
//    var $show_ul = $parent.find(".div_show");
//    var v_width = $show_ul.width();
//    var len = $show_ul.find("li").length;
//    var page_count = Math.ceil(len/i);
//        if(page == page_count){
//            $show_ul.stop().animate({
//                left:"0px"
//            },"slow");
//            page = 1;
//        }else{
//            $show_ul.stop().animate({
//                left:'-='+v_width
//            },"slow");
//            page++;
//        }
//        $parent.find(".highlight span").eq((page-1)).addClass("cur").siblings().removeClass("cur")
//});
//
//$(".img-left").click(function () {
//    var $parent = $(this).parent("div");
//    var $show_ul = $parent.find(".div_show");
//    var v_width = $show_ul.width();
//    var len = $show_ul.find("li").length;
//    var page_count = Math.ceil(len/i);
//        if(page == 1){
//            $show_ul.stop().animate({
//                left:'-='+v_width*(page_count-1)
//            },"slow");
//            page = page_count;
//        }else{
//            $show_ul.stop().animate({
//                left:'+='+v_width
//            },"slow");
//            page--;
//        }
//    $parent.find(".highlight span").eq((page-1)).addClass("cur").siblings().removeClass("cur")
//});
//
//
//function imgleft(){
//    var $parent = $(this).parent("div");
//    var $show_ul = $parent.find(".div_show");
//    var v_width = $show_ul.width();
//    var len = $show_ul.find("li").length;
//    var page_count = Math.ceil(len/i);
//    if(page == 1){
//        $show_ul.stop().animate({
//            left:'-='+v_width*(page_count-1)
//        },"slow");
//        page = page_count;
//    }else{
//        $show_ul.stop().animate({
//            left:'+='+v_width
//        },"slow");
//        page--;
//    }
//    $parent.find(".highlight span").eq((page-1)).addClass("cur").siblings().removeClass("cur")
//}
//
