// chart
const myChart = echarts.init(document.getElementById("main"))
myChart.setOption(options)
window.onresize = () => myChart.resize()

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
