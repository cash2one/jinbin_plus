$("#send_message").on("click", function () {
    var company = $.trim($("#company").val().replace(/，/g, ",").split(","));
    var meeting = $.trim($("#meeting").val());
    var name = $.trim($("#name").val());
    var mobilphone = $.trim($("#mobilphone").val());
    var message = $.trim($("#message").val());
    var iphone = /^1[3-8]+\d{9}$/;
    var array =[];
    array.push(company);
    console.log(array);
    if(company==0){
        swal("error","邀请人单位不能为空哦！","error");
        $("#company").css({border:"1px solid #ec7063"});
        return false
    }else if(meeting==0){
        swal("error","主办会议名称不能为空哦！","error");
        $("#meeting").css({border:"1px solid #ec7063"});
        return false
    }
    else if(name==0){
        swal("error","联系人姓名不能为空哦！","error");
        $("#name").css({border:"1px solid #ec7063"});
        return false
    }
    else if(mobilphone==0){
        swal("error","手机号码不能为空哦！","error");
        $("#mobilphone").css({border:"1px solid #ec7063"});
        return false
    }
    else if(!iphone.test(mobilphone)){
        swal("error","手机号码有误哦！","error");
        $("#mobilphone").css({border:"1px solid #ec7063"});
        return false
    }
    else if(message==0){
        swal("error","补充信息不能为空哦！","error");
        $("#message").css({border:"1px solid #ec7063"});
        return false
    }else{
        $("#guest").submit();
        $.ajax({
            url:"/sponsor_api/claim/"+thisid+"/",
            dataType:"json",
            type:"post",
            data:{
                name:name,
                company:company,
                meeting:meeting,
                mobilphone:mobilphone,
                message:message
            },
            success: function(data){
                console.log(data);
                if(data.success==1){
                    $(".content .meeasge_form input,.content .meeasge_form textarea").val("");
                    swal("您的信息已提交成功，稍后我们将与您联系。","success")

                }
            }
        })
    }
});
$("#company").focus(function(){
    $(this).css({border:"1px solid #ddd"})
});
$("#name").focus(function(){
    $(this).css({border:"1px solid #ddd"})
});
$("#meeting").focus(function(){
    $(this).css({border:"1px solid #ddd"})
});
$("#mobilphone").focus(function(){
    $(this).css({border:"1px solid #ddd"})
});
$("#message").focus(function(){
    $(this).css({border:"1px solid #ddd"})
});
