// chart
const chartContainer = document.getElementById("main")

const myChart = echarts.init(chartContainer)
myChart.setOption(options)
window.onresize = () => myChart.resize()

if(Object.keys(options).length === 0) {
  chartContainer.innerText = "There no data for this month"
  chartContainer.style = `
    font-size: 3rem;
    padding: 8rem 3rem 5rem;
    text-align: center;
    font-weight: bold;
    line-height: 1.25;
  `
}

// numbers animation

const numbers = document.querySelectorAll("[number-anim]")

numbers.forEach(num => {
  const number = parseInt(num.getAttribute("number-anim"))
  for (let value = 0; value <= number; value++) {
    setTimeout(() => num.innerText = value, 10*value)
  }
})

// select date

const monthForm  = document.getElementById("month-form")
const monthInput = document.getElementById("month-input")

monthInput.addEventListener("change", () => {
  console.log("ok");
  monthForm.submit()
})
