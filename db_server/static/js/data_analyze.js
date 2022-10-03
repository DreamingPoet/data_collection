// 教师男女占比=========================================================
(function () {

  // 基于准备好的dom，初始化echarts实例
  var chartBox = $(".chart.teacher-data");
  var myChart = echarts.init(document.querySelector(".chart.teacher-data"));

  // 指定图表的配置项和数据
  var option;

  option = {
      tooltip: {
          trigger: 'item'
      },
      legend: {
          top: '5%',
          left: 'center'
      },
      series: [
          {
              name: '访问来源',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              itemStyle: {
                  borderRadius: 5,
                  borderColor: '#fff',
                  borderWidth: 2
              },
              label: {
                  show: false,
                  position: 'center'
              },
              emphasis: {
                  label: {
                      show: true,
                      fontSize: '40',
                      fontWeight: 'bold'
                  }
              },
              labelLine: {
                  show: false
              },
              data: [
                  {value: 1048, name: '搜索引擎'},
                  {value: 735, name: '直接访问'},
                  {value: 580, name: '邮件营销'},
                  {value: 484, name: '联盟广告'},
                  {value: 300, name: '视频广告'}
              ]
          }
      ]
  };
  
  option && myChart.setOption(option);
  // 使用刚指定的配置项和数据显示图表。

  $(document).ready(function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });

  window.addEventListener("resize", function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });

})();

// 班级学生男女占比=========================================================
(function () {

  // 基于准备好的dom，初始化echarts实例
  var chartBox = $(".course-data.chart");
  var myChart = echarts.init(document.querySelector(".course-data.chart"));

  // 指定图表的配置项和数据
  // 指定图表的配置项和数据
  var option;

  option = {
      tooltip: {
          trigger: 'item'
      },
      legend: {
          top: '5%',
          left: 'center'
      },
      series: [
          {
              name: '访问来源',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              itemStyle: {
                  borderRadius: 5,
                  borderColor: '#fff',
                  borderWidth: 2
              },
              label: {
                  show: false,
                  position: 'center'
              },
              emphasis: {
                  label: {
                      show: true,
                      fontSize: '40',
                      fontWeight: 'bold'
                  }
              },
              labelLine: {
                  show: false
              },
              data: [
                  {value: 1048, name: '搜索引擎'},
                  {value: 735, name: '直接访问'},
                  {value: 580, name: '邮件营销'},
                  {value: 484, name: '联盟广告'},
                  {value: 300, name: '视频广告'}
              ]
          }
      ]
  };
  
  option && myChart.setOption(option);

  $(document).ready(function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });

  window.addEventListener("resize", function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });

})();

// 班级课件数量=========================================================
(function () {

  // 基于准备好的dom，初始化echarts实例
  var chartBox = $(".chart.klass-student");
  var myChart = echarts.init(document.querySelector(".chart.klass-student"));

  // 指定图表的配置项和数据
   // 指定图表的配置项和数据
   var option;

   option = {
       tooltip: {
           trigger: 'item'
       },
       legend: {
           top: '5%',
           left: 'center'
       },
       series: [
           {
               name: '访问来源',
               type: 'pie',
               radius: ['40%', '70%'],
               avoidLabelOverlap: false,
               itemStyle: {
                   borderRadius: 5,
                   borderColor: '#fff',
                   borderWidth: 2
               },
               label: {
                   show: false,
                   position: 'center'
               },
               emphasis: {
                   label: {
                       show: true,
                       fontSize: '40',
                       fontWeight: 'bold'
                   }
               },
               labelLine: {
                   show: false
               },
               data: [
                   {value: 1048, name: '搜索引擎'},
                   {value: 735, name: '直接访问'},
                   {value: 580, name: '邮件营销'},
                   {value: 484, name: '联盟广告'},
                   {value: 300, name: '视频广告'}
               ]
           }
       ]
   };
   
   option && myChart.setOption(option);

  $(document).ready(function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });

  window.addEventListener("resize", function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });


})();

// 班级各个类型占比=========================================================
(function () {

  // 基于准备好的dom，初始化echarts实例
  var chartBox = $(".chart.klass-course");
  var myChart = echarts.init(document.querySelector(".chart.klass-course"));

  // 指定图表的配置项和数据
  var option;

  option = {
      tooltip: {
          trigger: 'item'
      },
      legend: {
          top: '5%',
          left: 'center'
      },
      series: [
          {
              name: '访问来源',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              itemStyle: {
                  borderRadius: 5,
                  borderColor: '#fff',
                  borderWidth: 2
              },
              label: {
                  show: false,
                  position: 'center'
              },
              emphasis: {
                  label: {
                      show: true,
                      fontSize: '40',
                      fontWeight: 'bold'
                  }
              },
              labelLine: {
                  show: false
              },
              data: [
                  {value: 1048, name: '搜索引擎'},
                  {value: 735, name: '直接访问'},
                  {value: 580, name: '邮件营销'},
                  {value: 484, name: '联盟广告'},
                  {value: 300, name: '视频广告'}
              ]
          }
      ]
  };
  
  option && myChart.setOption(option);

  $(document).ready(function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });

  window.addEventListener("resize", function () {
    chartBox.height(chartBox.width() * 0.617);
    myChart.resize();
  });


    

})();

