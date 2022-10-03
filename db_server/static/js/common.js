function getUrlParam(name, bFullParam = 0) {
  var reg = new RegExp("(^|)" + name + "=([^&]*)(|$)"); //构造一个含有目标参数的正则表达式对象
  var r = window.location.search.substr(1).match(reg); //匹配目标参数
  if (r != null) return unescape(r[bFullParam ? 0 : 2]);
  return null; //返回参数值
}

for (
  var i = getUrlParam("end"),
    o = $(".timeinterval")
      .filter(function () {
        return this.id == i;
      })
      .addClass("selected");
  ;

) {
  if (!o.is("li")) break;
}

// 修改时间自动跳转
$("#time-end").change(function () {
  console.log($(this).val());

  var startValue = getUrlParam("start", true);
  var endValue = getUrlParam("end", true);

  var newlocation = window.location.href;

  newlocation = newlocation.replace(startValue, "start=" + $("#time-start").val());
  newlocation = newlocation.replace(endValue, "end=" + $(this).val());
  window.location.href = newlocation;
});

// 点击时间跳转
$("button.timeinterval").click(function () {
  var startValue = getUrlParam("start", true);
  var endValue = getUrlParam("end", true);
  var newlocation = window.location.href;

  newlocation = newlocation.replace(startValue, "start=0");
  newlocation = newlocation.replace(endValue, "end=" + $(this).attr("id"));
  window.location.href = newlocation;
});

(function () {

  // 自动添加日期
  var newlocation = window.location.href;
  // 如果没有问号
  if (newlocation.indexOf("?") < 0) {
    newlocation = newlocation + "?";
    window.location.href = window.location.href + "?start=0&end=today";
  } else {
    var startValue = getUrlParam("start");
    var endValue = getUrlParam("end");
    if (startValue == null && endValue == null) {
      window.location.href = window.location.href + "&start=0&end=today";
    }
  }

  // 设置日期输入框的日期
  $("#time-start").val(getUrlParam("start"));
  $("#time-end").val(getUrlParam("end"));

})();
