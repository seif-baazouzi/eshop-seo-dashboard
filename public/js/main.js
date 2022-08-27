const myChart = echarts.init(document.getElementById("main"))
myChart.setOption(options)
window.onresize = () => myChart.resize()
