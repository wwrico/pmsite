/**
 * Created by rico on 2014/6/25.
 */
$('#organizeTree').tree({
    onClick: function (node) {
        alert(node.text);  // alert node text property when clicked
    }
});

//js绑定右键菜单
$(document).bind('contextmenu', function (e) {
    $('#mm').menu('show', {
        left: e.pageX,
        top: e.pageY
    });
    return false;
});

//若点击按钮触发：
<a href="#" id="aa1">ShowMenu</a>
$('#aa1').click(function () {
    $('#mm').menu('show', {
        left: 100,
        top: 200
    });
});
