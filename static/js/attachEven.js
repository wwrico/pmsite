/**
 * Created by rico on 2014/6/26.
 */
//使JavaScript和HTML分离，当页面加载后，对事件等资源初始化
function attachEvents() {
    document.getElementById("input1").onclick = showMessage;
}
function showMessage() {
    alert('This is a button.');
}