// Model name mapping
const modelNameMapping = {
    'GPT-4o (0513)': 'GPT_4o',
    'Claude-3.5-Sonnet': 'Claude_3.5',
    'Gemini-1.5-Pro-002': 'Gemini_1.5_pro_002',
    'Gemini-1.5-Flash-002': 'Gemini_1.5_flash_002',
    'GPT-4O Mini': 'GPT_4o_mini',
    'Qwen2-VL-72B': 'Qwen2_VL_72B',
    'InternVL2-Llama3-76B': 'InternVL2_76B',
    'LLaVA-OneVision-72B': 'llava_onevision_72B',
    'Qwen2-VL-7B': 'Qwen2_VL_7B',
    'Pixtral 12B': 'Pixtral_12B',
    'InternVL2-8B': 'InternVL2_8B',
    'Phi-3.5-Vision': 'Phi-3.5-vision',
    'MiniCPM-V2.6': 'MiniCPM_v2.6',
    'LLaVA-OneVision-7B': 'llava_onevision_7B',
    'Llama-3.2-11B': 'Llama_3_2_11B',
    'Idefics3-8B-Llama3': 'Idefics3',
};

// Model order (desired display order)
const modelOrder = [
    'GPT-4o (0513)',
    'Claude-3.5-Sonnet',
    'Gemini-1.5-Pro-002',
    'Gemini-1.5-Flash-002',
    'GPT-4O Mini',
    'Qwen2-VL-72B',
    'InternVL2-Llama3-76B',
    'LLaVA-OneVision-72B',
    'Qwen2-VL-7B',
    'Pixtral 12B',
    'InternVL2-8B',
    'Phi-3.5-Vision',
    'MiniCPM-V2.6',
    'LLaVA-OneVision-7B',
    'Llama-3.2-11B',
    'Idefics3-8B-Llama3',
];

// Define a consistent color mapping for models
const modelColorMapping = {
    'GPT-4o (0513)': 'rgba(255, 99, 132, 0.6)',
    'Claude-3.5-Sonnet': 'rgba(54, 162, 235, 0.6)', 
    'Gemini-1.5-Pro-002': 'rgba(75, 192, 192, 0.6)',
    'Gemini-1.5-Flash-002': 'rgba(153, 102, 255, 0.6)', 
    'GPT-4O Mini': 'rgba(255, 159, 64, 0.6)',
    'Qwen2-VL-72B': 'rgba(255, 205, 86, 0.6)', 
    'InternVL2-Llama3-76B': 'rgba(201, 203, 207, 0.6)', 
    'LLaVA-OneVision-72B': 'rgba(140, 82, 255, 0.6)', 
    'Qwen2-VL-7B': 'rgba(255, 87, 51, 0.6)', 
    'Pixtral 12B': 'rgba(220, 220, 220, 0.6)', 
    'InternVL2-8B': 'rgba(52, 152, 219, 0.6)', 
    'Phi-3.5-Vision': 'rgba(46, 204, 113, 0.6)', 
    'MiniCPM-V2.6': 'rgba(230, 126, 34, 0.6)', 
    'LLaVA-OneVision-7B': 'rgba(231, 76, 60, 0.6)', 
    'Llama-3.2-11B': 'rgba(52, 73, 94, 0.6)', 
    'Idefics3-8B-Llama3': 'rgba(241, 196, 15, 0.6)',
};

// Dimensions for the radar charts
const dimensions = ['skills', 'input_format', 'output_format', 'input_num', 'app'];

let globalData;
let chartInstances = [];

// Fetch and load JSON data
fetch('./static/data/all_model_keywords_stats.json')
    .then(response => response.json())
    .then(data => {
        globalData = data;
        
        // Populate model select options
        const modelSelect1 = document.getElementById('model-select-1');
        const modelSelect2 = document.getElementById('model-select-2');
        
        modelOrder.forEach(modelName => {
            const option1 = document.createElement('option');
            option1.value = modelName;
            option1.textContent = modelName;
            modelSelect1.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = modelName;
            option2.textContent = modelName;
            modelSelect2.appendChild(option2);
        });

        // Add event listeners for model selection changes
        modelSelect1.addEventListener('change', updateCharts);
        modelSelect2.addEventListener('change', updateCharts);

        // Initial chart creation
        updateCharts();
    });

function updateCharts() {
    const selectedModel1 = document.getElementById('model-select-1').value;
    const selectedModel2 = document.getElementById('model-select-2').value;
    const containerElement = document.getElementById('radar-charts-container');
    
    // Clear existing charts
    containerElement.innerHTML = '';
    chartInstances.forEach(chart => chart.destroy());
    chartInstances = [];

    // Create a chart for each dimension
    dimensions.forEach(dimension => {
        const chartContainer = document.createElement('div');
        chartContainer.className = 'chart-container';
        
        const canvas = document.createElement('canvas');
        chartContainer.appendChild(canvas);
        containerElement.appendChild(chartContainer);

        const radarData = prepareRadarData(globalData, selectedModel1, selectedModel2, dimension);
        const chart = createRadarChart(canvas, radarData, dimension);
        chartInstances.push(chart);
    });
}

function prepareRadarData(data, modelName1, modelName2, dimensionKey) {
    const radarData = {
        labels: [],
        datasets: []
    };

    const dataModelName1 = modelNameMapping[modelName1];
    const modelData1 = data[dataModelName1]?.[dimensionKey] || {};

    radarData.labels = Object.keys(modelData1).sort();

    // Normalize the data to 0-1 range if necessary
    const maxValue1 = Math.max(...radarData.labels.map(field => modelData1[field]?.average_score || 0));
    const normalizeValue = (value, maxValue) => maxValue > 1 ? value / maxValue : value;

    const dataset1 = {
        label: modelName1,
        data: radarData.labels.map(field => normalizeValue(modelData1[field]?.average_score || 0, maxValue1)),
        fill: true,
        borderColor: modelColorMapping[modelName1],
        backgroundColor: modelColorMapping[modelName1].replace('0.6', '0.2')
    };

    radarData.datasets.push(dataset1);

    if (modelName2 && modelName2 !== "") {
        const dataModelName2 = modelNameMapping[modelName2];
        const modelData2 = data[dataModelName2]?.[dimensionKey] || {};
        const maxValue2 = Math.max(...radarData.labels.map(field => modelData2[field]?.average_score || 0));

        const dataset2 = {
            label: modelName2,
            data: radarData.labels.map(field => normalizeValue(modelData2[field]?.average_score || 0, maxValue2)),
            fill: true,
            borderColor: modelColorMapping[modelName2],
            backgroundColor: modelColorMapping[modelName2].replace('0.6', '0.2')
        };

        radarData.datasets.push(dataset2);
    }

    return radarData;
}

function createRadarChart(canvas, radarData, dimension) {
    return new Chart(canvas.getContext('2d'), {
        type: 'radar',
        data: radarData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    beginAtZero: true,
                    min: 0,
                    max: 1,
                    ticks: {
                        stepSize: 0.2,
                        font: {
                            size: 12
                        }
                    },
                    pointLabels: {
                        font: {
                            size: 14
                        },
                        callback: function(label) {
                            const words = label.split(' ');
                            const lines = [];
                            let currentLine = '';

                            words.forEach(word => {
                                if (currentLine.length + word.length <= 15) {
                                    currentLine += (currentLine ? ' ' : '') + word;
                                } else {
                                    lines.push(currentLine);
                                    currentLine = word;
                                }
                            });
                            if (currentLine) {
                                lines.push(currentLine);
                            }
                            return lines;
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        font: {
                            size: 14
                        },
                        padding: 20
                    }
                },
                title: {
                    display: true,
                    text: dimension.charAt(0).toUpperCase() + dimension.slice(1).replace('_', ' '),
                    font: {
                        size: 20,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 30
                    }
                },
                tooltip: {
                    bodyFont: {
                        size: 14
                    },
                    titleFont: {
                        size: 16
                    }
                }
            },
            elements: {
                point: {
                    radius: 4,
                    hoverRadius: 6
                },
                line: {
                    borderWidth: 3
                }
            }
        }
    });
}