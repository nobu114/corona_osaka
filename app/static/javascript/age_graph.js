var ctx_age = document.getElementById("age_graph").getContext('2d');
var age_graph = new Chart(ctx_age, {
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
                'rgba(255, 159, 64, 0.2)',
                'rgba(255,31,233,0.2)',
                'rgba(36,255,153,0.2)',
                'rgba(3,45,255,0.2)',
                'rgba(135,199,184,0.2)',
                'rgba(111,84,199,0.2)',
                'rgba(199,32,54,0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255,31,233,1)',
                'rgba(36,255,153,1)',
                'rgba(3,45,255,1)',
                'rgba(135,199,184,1)',
                'rgba(111,84,199,1)',
                'rgba(199,32,54,1)'
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

var ctx_symptoms = document.getElementById("symptoms_graph").getContext("2d");
var symptoms_graph = new Chart(ctx_symptoms, {
    type: 'horizontalBar',
    data: {
        labels: [
            "軽症", "重症", "死亡", "無症状", "退院・解除済み", "調査中"
        ],
        datasets: [{
            label: '感染者の症状別グラフ',
            data: [
                symptoms_dict["mild_illness"], symptoms_dict["serious_illness"],
                symptoms_dict["die"], symptoms_dict["asymptomatic"], symptoms_dict["end"],
                symptoms_dict["examine"]
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
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
