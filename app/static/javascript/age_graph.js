var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: [
            "未就学児", "就学児", "10代", "20代", "30代", "40代", "50代", "60代",
            "70代", "80代", "90代", "100代"
        ],
        datasets: [{
            label: '感染者の年代ごとのグラフ',
            data: [
                people_dict["未就学児"], people_dict["就学児"], people_dict["10"],
                people_dict["20"], people_dict["30"], people_dict["40"], people_dict["50"],
                people_dict["60"], people_dict["70"], people_dict["80"], people_dict["90"],
                people_dict["100"]
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});